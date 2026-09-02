import pubchempy as pcp
import pandas as pd
from tqdm import tqdm
import time

# Load your ChEMBL dataset
chembl_df = pd.read_csv(r"C:\Users\jschoer\Desktop\DSA103 Coding and Tests\DSA103\prep_lecture9\src\lecture_9_prep_material\ache_activities.csv")  # or your actual file
smiles_list = chembl_df["canonical_smiles"].dropna().tolist()

records = []

for smi in tqdm(smiles_list[:200]):  # limit to 200 compounds for testing, tqdm just adds progress bar
    try:
        compounds = pcp.get_compounds(smi, namespace='smiles') # look for each smiles-code in the list sliced from the ChEMBL data
        if not compounds:
            continue
        
        c = compounds[0]
        records.append({
            "canonical_smiles": smi,
            "CID": c.cid,
            "MolecularWeight": c.molecular_weight,
            "XLogP": c.xlogp,
            "TPSA": c.tpsa,
            "HBondDonorCount": c.h_bond_donor_count,
            "HBondAcceptorCount": c.h_bond_acceptor_count,
            "RotatableBondCount": c.rotatable_bond_count
        })
        
        # delay to avoid flooding PubChem servers
        time.sleep(0.2)
        
    except Exception as e:
        print(f"Failed for {smi[:20]}...: {e}")

pubchem_df = pd.DataFrame(records)
pubchem_df.to_csv(r"C:\Users\jschoer\Desktop\DSA103 Coding and Tests\DSA103\prep_lecture9\src\lecture_9_prep_material\ache_pubchem_descriptors.csv", index=False)
print(f"Saved {len(pubchem_df)} entries to ache_pubchem_descriptors.csv")