from Classes.ValidationErr import *

# Validation: Ensure files are in the correct format
#
# Input: File paths (String)
#
# Output: String with posible errors
def val_gff(met_gff, fasta, anot_gff):
    error = ""
    if not met_gff.endswith(".gff"):
        error = error + "-> SMRT Methylation file is not a .gff\n"
    elif not anot_gff.endswith(".gff"):
        error = error + "-> Genome annotation file is not a .gff\n"
    elif not fasta.endswith(".fasta"):
        error = error + "-> Genome file is not in .fasta\n"
    return error

# Validation:
#   - Pattern empty
#   - If not empty, follows IUPAC:"ACGTURYSWKMBDHVN"
#
# Input: Pattern (string)
#
# Output: Message or Exception
def validatePattern(string):
    # Ensure string is not empty
    if not string is "":
        for i in string:
            # IUPAC Validation
            if not i in "ACGTURYSWKMBDHVN":
                raise ValidationErr("Pattern incorrect, no correct IUPAC values.")
        return "Filled"
    # If empty, give a message to indicate so
    else:
        return "None"

# Validation: 
#   - Ensure promoter region and positions are integer.
#   - Promoter and positions can't be lower than 0.
#   - Pattern follows IUPAC rules: "ACGTURYSWKMBDHVN"
#   - Position in pattern index
#   - 
#
# Input: Promoter region (integer) and positions (2 dictionaries (pattern: position))
#
# Output: Errors (string)
def val_promoter_patterns(prom, pattDict, compPattDict):
    error = ""

    # Promoter not null and integer
    if not "" and not isinstance(prom, int):
        error = f"-> {prom} is not Integer.\n"
    # Promoter not lower than 0
    elif prom < 0:
        error = f"-> Promoter Region cannot be negative.\n"
    
    # Validations for patterns
    for pat in pattDict:
        try:
            # Position not null and is integer
            if not "" and not isinstance(pattDict[pat],int):
                error = error + f"-> {pat}: {pattDict[pat]} is not Integer.\n"
        except SyntaxError:
            error = error + f"-> {pattDict[pat]} is not Integer.\n"
    return error

# Main validation function to call others and catch all errors
#
# Inputs: Methylation gff file path (String), fasta file path (String), annotation gff file path (String),
#           promoter region (Integer), patterns 1 to 4 (String), positions for methylations in patterns 1 to 4 (Integer),
#           complementary patterns 1 to 4 (String), positions in complementary patterns 1 to 4 (Integer)
#
# Output: String array with all errors captured
def validations(met_gff, fasta, anot_gff, prom, pattDict, compPattDict):
    errors = []
    errors.append(val_gff(met_gff, fasta, anot_gff))
    errors.append(val_promoter_patterns(prom, pattDict, compPattDict))

    if errors!=["",""]:
        raise ValidationErr(errors)