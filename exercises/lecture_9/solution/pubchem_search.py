import pubchempy as pcp
import pandas as pd
from tqdm import tqdm
import time

# Load your ChEMBL dataset
chembl_df = pd.read_csv(r"C:[path]\antibio_chembl_mics.csv")  # use your actual filename and path
smiles_list = chembl_df["smiles"].dropna().tolist() # use the column tag with the "smiles"

records = []

for smi in tqdm(smiles_list):  # tqdm adds progress bar
    try:
        compounds = pcp.get_compounds(smi, namespace='smiles') # look for each smiles-code in the list sliced from the ChEMBL data
        if not compounds:
            continue
        
        c = compounds[0]
        records.append({
            "smiles": smi, # make sure that the column name for the smiles code matches the chembl dataframe!
            "CID": c.cid,
            "MolecularWeight": c.molecular_weight,
            "XLogP": c.xlogp,
            "TPSA": c.tpsa,
            "HBondDonorCount": c.h_bond_donor_count,
            "HBondAcceptorCount": c.h_bond_acceptor_count,
            "RotatableBondCount": c.rotatable_bond_count,
            "HeavyAtomCount": c.heavy_atom_count
        })
        
        # delay to avoid flooding PubChem servers
        time.sleep(0.2)
        
    except Exception as e:
        print(f"Failed for {smi[:20]}...: {e}")

pubchem_df = pd.DataFrame(records)
pubchem_df.to_csv(r"[path]\antibio_pubchem_descr.csv", index=False) # use your path and specified filename
print(f"Saved {len(pubchem_df)} entries.")