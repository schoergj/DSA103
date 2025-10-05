# Test molecular formula calculation
from dsa103.chemistry_tools import calculate_molecular_formula

# Calculate molecular formula of water (Smiles: O)
formula_water = calculate_molecular_formula("O")
print(f"Molecular formula of water: {formula_water}")

# Calculate molecular formula of caffeine (Smiles: CN1C=NC2=C1C(=O)N(C(=O)N2C)C)
formula_caffeine = calculate_molecular_formula("CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
print(f"Molecular formula of caffeine: {formula_caffeine}")
