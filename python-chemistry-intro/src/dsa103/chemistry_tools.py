from rdkit import Chem
from rdkit.Chem import rdMolDescriptors


def calculate_molecular_formula(smiles: str) -> float:
    """Calculates the molecular formula for a given molecule. The molecule is expected to be a Smiles string."""
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid Smiles string. Could not parse molecule.")
    
    return rdMolDescriptors.CalcMolFormula(mol)

def calculate_molecular_weight(molecule: str) -> float:
    """Calculates the molecular weight of a molecule given its string. outputs the monoisotopic mass"""

    mol = Chem.MolFromSmiles(molecule)

    if mol is None:
        raise ValueError("Invalid Smiles string. Could not parse molecule.")
    
    return rdMolDescriptors.CalcExactMolWt(mol)
