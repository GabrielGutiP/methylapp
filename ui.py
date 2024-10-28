from tkinter import *
from tkinter import filedialog
from easygui import exceptionbox
from functools import partial
from validations import validations
from Classes.ValidationErr import ValidationErr
from functions import *

# ------------------- TKINTER CONFRIGURATION ---------------------------------------------------------------------------------
window = Tk()
window.geometry("1250x450")                          # Main window dimension

logo = PhotoImage(file="logo.png")       # MethylApp Logo

window.iconphoto(False, logo)                       # Logo in title bar
window.title("MethylApp")                           # Title of the main window

bg = Label(window, image=logo)
bg.place(x=0, y=0, relwidth=1, relheight=1)         # Background Image bg="#ffffff"


labelWelcome = Label(window, text="Welcome to MethylApp")
labelInfo = Label(window, text="This application is designed to analyze the results obtained from SMRT (Single Molecule, RealTime) sequencing, the state-of-the-art technology for the detection of epigenetic marks by methylation in bacterial genomes.\nThe final result of a SMRT sequencing is a coordinate file with the locations, type and contexts of methylations, this file is the main input of this application.")
labelWelcome.pack(pady=50)
labelInfo.pack()
# At least one pattern must be introduced. For each pattern, it's complementary must be introduced. In complementary pattern position 0 means that the pattern is not methylated.

# Frame to organize the inputs
frameFiles = Frame(window)
frameFiles.pack(side="left", padx=20)

jobID_label = Label(frameFiles, text="Job ID (Optional): ")
jobID_label.grid(row=0, column=0)

jobID_entry = Entry(frameFiles)
jobID_entry.grid(row=0,column=1)

# Funcition to open file browser
def openfile(entryBox):
    filename = filedialog.askopenfilename()
    entryBox.delete(0, END)
    entryBox.insert(END, filename)

# SMRT file selection
met_gff_label = Label(frameFiles, text="SMRT Methylation Output (.gff): ")
met_gff_label.grid(row=1, column=0)

met_gff_entry = Entry(frameFiles)
met_gff_entry.grid(row=1, column=1)
met_gff_button = Button(frameFiles , text="Search file", command= partial(openfile,met_gff_entry))
met_gff_button.grid(row=1, column=2)

# Annotation file selection
annotation_label = Label(frameFiles, text="Genome annotation file (.gff): ")
annotation_label.grid(row=2, column=0)

annotation_entry = Entry(frameFiles)
annotation_entry.grid(row=2, column=1)
annotation_button = Button(frameFiles , text="Search file", command= partial(openfile,annotation_entry))
annotation_button.grid(row=2, column=2)

# Fasta file selection
fasta_label = Label(frameFiles, text="Genome file Fasta Format (.fasta): ")
fasta_label.grid(row=3, column=0)

fasta_entry = Entry(frameFiles)
fasta_entry.grid(row=3, column=1)
fasta_button = Button(frameFiles , text="Search file", command= partial(openfile,fasta_entry))
fasta_button.grid(row=3, column=2)

# Promoter region
prom_label = Label(frameFiles, text="Promoter region (bases before codon start): ")
prom_label.grid(row=4, column=0)

prom_entry = Entry(frameFiles)
prom_entry.grid(row=4, column=1)

# Patterns inputs
framePatterns = Frame(window)
framePatterns.pack(side="right", padx=20)

patt_label = Label(framePatterns, text="Patterns")
patt_label.grid(row=0, column=0)

patt1_entry = Entry(framePatterns)
patt1_entry.grid(row=1, column=0)

patt2_entry = Entry(framePatterns)
patt2_entry.grid(row=2, column=0)

patt3_entry = Entry(framePatterns)
patt3_entry.grid(row=3, column=0)

patt4_entry = Entry(framePatterns)
patt4_entry.grid(row=4, column=0)

patt5_entry = Entry(framePatterns)
patt5_entry.grid(row=5, column=0)

patt6_entry = Entry(framePatterns)
patt6_entry.grid(row=6, column=0)

## Patterns methylation position
patt_label = Label(framePatterns, text="Met.Pos.")
patt_label.grid(row=0, column=1)

pos_patt1_entry = Entry(framePatterns, width=5)
pos_patt1_entry.grid(row=1, column=1, padx=2)

pos_patt2_entry = Entry(framePatterns, width=5)
pos_patt2_entry.grid(row=2, column=1, padx=2)

pos_patt3_entry = Entry(framePatterns, width=5)
pos_patt3_entry.grid(row=3, column=1, padx=2)

pos_patt4_entry = Entry(framePatterns, width=5)
pos_patt4_entry.grid(row=4, column=1, padx=2)

pos_patt5_entry = Entry(framePatterns, width=5)
pos_patt5_entry.grid(row=5, column=1, padx=2)

pos_patt6_entry = Entry(framePatterns, width=5)
pos_patt6_entry.grid(row=6, column=1, padx=2)


## Complementary patterns inputs
comp_patt_label = Label(framePatterns, text="Complementary")
comp_patt_label.grid(row=0, column=2)

comp_patt1_entry = Entry(framePatterns)
comp_patt1_entry.grid(row=1, column=2)

comp_patt2_entry = Entry(framePatterns)
comp_patt2_entry.grid(row=2, column=2)

comp_patt3_entry = Entry(framePatterns)
comp_patt3_entry.grid(row=3, column=2)

comp_patt4_entry = Entry(framePatterns)
comp_patt4_entry.grid(row=4, column=2)

comp_patt5_entry = Entry(framePatterns)
comp_patt5_entry.grid(row=5, column=2)

comp_patt6_entry = Entry(framePatterns)
comp_patt6_entry.grid(row=6, column=2)

### Complementary patterns methylation position
patt_label = Label(framePatterns, text="Met.Pos.")
patt_label.grid(row=0, column=3)

pos_comp_patt1_entry = Entry(framePatterns, width=5)
pos_comp_patt1_entry.grid(row=1, column=3, padx=2)

pos_comp_patt2_entry = Entry(framePatterns, width=5)
pos_comp_patt2_entry.grid(row=2, column=3, padx=2)

pos_comp_patt3_entry = Entry(framePatterns, width=5)
pos_comp_patt3_entry.grid(row=3, column=3, padx=2)

pos_comp_patt4_entry = Entry(framePatterns, width=5)
pos_comp_patt4_entry.grid(row=4, column=3, padx=2)

pos_comp_patt5_entry = Entry(framePatterns, width=5)
pos_comp_patt5_entry.grid(row=5, column=3, padx=2)

pos_comp_patt6_entry = Entry(framePatterns, width=5)
pos_comp_patt6_entry.grid(row=6, column=3, padx=2)

# Main function: calls validations and main functions
def __main__():
    try:
        # Transform Promoter Region in Integer if not void
        if not prom_entry.get() is "":
            prom = int(prom_entry.get())

        # Dictionary for Patterns = {Pattern (String): Methylated Position (Integer)}
        patternsDict, compPattDict = createPatternsDict(patt1_entry.get(), pos_patt1_entry.get(), patt2_entry.get(), pos_patt2_entry.get(), patt3_entry.get(), pos_patt3_entry.get(), 
                                                        patt4_entry.get(), pos_patt4_entry.get(), patt5_entry.get(), pos_patt5_entry.get(), patt6_entry.get(), pos_patt6_entry.get(),
                                                        comp_patt1_entry.get(), pos_comp_patt1_entry.get(), comp_patt2_entry.get(), pos_comp_patt2_entry.get(), comp_patt3_entry.get(), 
                                                        pos_comp_patt3_entry.get(), comp_patt4_entry.get(), pos_comp_patt4_entry.get(), comp_patt5_entry.get(), pos_comp_patt5_entry.get(), 
                                                        comp_patt6_entry.get(), pos_comp_patt6_entry.get())
        
        # Filter of empty patterns

        # Call to validations.py to check all input
        validations(met_gff_entry.get(),fasta_entry.get(),annotation_entry.get(),int(prom_entry.get()),patternsDict,compPattDict)
        print("Funciono 1")
    except ValidationErr:
        exceptionbox(ValidationErr.__str__)
    # Capture Exception for transforming in Integer
    except ValueError:
        exceptionbox("\n -> Positions or Promoter Region are not integer.\n")
    except:
        exceptionbox()

# Button for starting app
start_button = Button(window , text="Get Excel", command= __main__)
start_button.place(relx=0.5, rely=0.8, anchor=CENTER)

window.mainloop()                                   # "Log" de sucesos en la ventana
# ------------------- END OF TKINTER ------------------------------------------------------------------------------------------