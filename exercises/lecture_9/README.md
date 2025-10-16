# Lecture 9: Generating Data and Hypotheses

In the lecture we created a dataset for investigating the QSAR between small molecules and the enzyme Acetylcholinesterase. Now, imagine that your lab is looking into small molecules as new antibiotics. As a first step to that end, you want to explore if there is any connection between molecular properties and the MIC (Minimum inhibitory concentration, lower = better). As target you choose a classic: Escherichia coli. 


## Tasks

#### Data acquisition ChEMBL
- Get data from ChEMBL: Search for "Escerichia Coli" or CHEMBL354 (as target!), then in the "activity charts" click on "MIC". In the resulting list of about 87'000 entries use a filter for a range of molecular weights from about 100 to 300. This will leave you with about 8'000 to 9'000 molecules. Export the result list as .csv file. If the filtering doesn't work, this will give you a preselction: https://www.ebi.ac.uk/chembl/explore/activities/STATE_ID:qRngqmZ7xPaj-CBZ_lNX-g%3D%3D
- Prepare the data from ChEMBL: Load the csv as DataFrame and select only the following columns: 'Molecule ChEMBL ID', 'Smiles', 'Standard Type', 'Standard Relation', 'Standard Value', 'Standard Units', 'Assay ChEMBL ID'.
- Rename the columns (e.g. avoid spaces, more convenient names). 
- You can drop all rows which contain no Smiles code (make sure to comment!).
- Select a couple of hundred entries (pseudo)randomly from the entire DataFrame. You can use a pandas function for that: 
   ```python
   df_sample = df.sample(n=300, random_state=42)
   ```
- Export this DataFrame to a .csv file.

#### Data acquisition PubChem
- To get some molecular descriptors, use the python script supplied here ("pubchem_search.py"), you may have to install the pubchempy library for this.
- Change the filenames and paths (pay attention to absolute and relative paths!) as well as the name of the "smiles"-column (see comments in the python script).
- Run the script.

#### Combining the datasets

- Proceed as in the lecture. Load the two datasets and inspect them. 
- Check for duplicates in the pubchem data: Some smiles were present more than once in the ChEMBL data, e.g. for different assays. These will result in quite a few duplicates in the combined dataframe if not removed prior to the merge. Either remove them now or after the merge (make sure to comment!)
- Merge the two dataframes. 
- You will realise that the units are different in some rows. Either convert them or drop the rows (document all manipulation).
- Perform an EDA on the resulting DataFrame and treat "bad data" as needed (always make sure to comment).
- Save the cleaned dataset as .csv file.

#### Hypothesis generation

- Based on your EDA, postulate a hypothesis that links the MIC values (lower is better!) to molecular structure (e.g. XLogP).
- Create a scatterplot for the selected features.
- Based on the plot, determine the threshold, e.g. for the log P, which divides your data in two groups to compare in the subsequent test. (You can follow the procedure as treated in the lecture).
- Run a t-test to check your hypothesis.
- Repeat the procedure but select from the DataFrame only entries whose MIC is lower than 10 ug.L-1. 
- Interpret the results!

