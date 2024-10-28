from validations import validatePattern
# Function to create dictionaries for patterns
#
# Inputs: Patterns and positions
#
# Outputs: 2 dictionaries (Patterns (String): Positions (Integer))
def createPatternsDict(pat1, pos1, pat2, pos2, pat3, pos3, pat4, pos4, pat5, pos5, pat6, pos6, cpat1, cpos1, cpat2, cpos2, cpat3, cpos3, cpat4, cpos4, cpat5, cpos5, cpat6, cpos6):
    pattDict = {}
    compPattDict = {}

    if validatePattern(pat1) is "Filled":
        pattDict[pat1] = int(pos1)

    if validatePattern(pat2) is "Filled":
        pattDict[pat2] = int(pos2)

    if validatePattern(pat3) is "Filled":
        pattDict[pat3] = int(pos3)

    if validatePattern(pat4) is "Filled":
        pattDict[pat4] = int(pos4)

    if validatePattern(pat5) is "Filled":
        pattDict[pat5] = int(pos5)

    if validatePattern(pat6) is "Filled":
        pattDict[pat6] = int(pos6)

    if validatePattern(cpat1) is "Filled":
        compPattDict[cpat1] = int(cpos1)

    if validatePattern(cpat2) is "Filled":
        compPattDict[cpat2] = int(cpos2)

    if validatePattern(cpat3) is "Filled":
        compPattDict[cpat3] = int(cpos3)

    if validatePattern(cpat4) is "Filled":
        compPattDict[cpat4] = int(cpos4)

    if validatePattern(pat5) is "Filled":
        compPattDict[cpat5] = int(cpos5)

    if validatePattern(cpat6) is "Filled":
        compPattDict[cpat6] = int(cpos6)

    return pattDict, compPattDict

# Main function to call all the others in order
#
# Inputs: Job ID name (String), methylation gff file path (String), fasta file path (String), annotation gff file path (String),
#           promoter region (Integer), patterns 1 to 4 (String), positions for methylations in patterns 1 to 4 (Integer),
#           complementary patterns 1 to 4 (String), positions in complementary patterns 1 to 4 (Integer)
#
# Output: Excel file with all data requested
def mainFunction(jobID, met_gff, fasta, annotation_gff, promoter, p1, p2, p3, p4, p5, p6, pos1, pos2, pos3, pos4, pos5, pos6, 
                 cp1, cp2, cp3, cp4, cp5, cp6, posc1, posc2, posc3, posc4, posc5, posc6):
    return