from dsa103.chemistry_tools import calculate_molecular_formula


def test_calculate_molecular_formula():
    """Tests for calculate_molecular_formula."""

    formula_water = calculate_molecular_formula("O")
    assert formula_water == "H2O"

    formula_caffeine = calculate_molecular_formula("CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
    assert formula_caffeine == "C8H10N4O2"
