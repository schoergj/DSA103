# LifeScienceData: Molecular representations


## Task 1:
- To get familiar with 3D structure descriptions, inspect the 1PEN.pdb file. Which data types can you identify? Inspect the structure information in more detail. What do you observe?

## Task 2:
- Use any of the datasets from previous exercises (pubchem, ChEMBL). Use slicing or the sample method to create a small DataFrame (<100 rows) that is convenient to work with.
- Use rdkit to convert the SMILES string from the original data into a canonical SMILES.
- Use the SMILES column to display the structure of the molecule in the DataFrame (Hint: There is a very convenient option in the rdkit)

## Task 3:
- Write a script that extracts the distance of the alkyne bond in the calculation input file from the lecture (yne.gjf). No worries about elegance, e.g. you can hardcode the atom numbers of the two carbon atoms if needed. (Hint: There are different solutions possible, with and without rdkit. For the latter, the split() method might be useful - and you might want to have a look at how to open textfiles :) )
- Use a suitable molecular viewer to verify your result.
