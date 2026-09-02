import numpy as np

def read_coordinates(filename):
    """Read an XYZ file and return atom symbols and coordinates."""
    with open(filename) as f:
        lines = f.readlines()[7:]  # omit lines 1-6 (header)
    atoms, coords = [], []
    for line in lines:
        parts = line.split()
        if len(parts) == 4:
            atoms.append(parts[0])
            coords.append([float(x) for x in parts[1:4]])
    return atoms, np.array(coords)

def bond_distance(coords, i, j):
    """Compute distance between atoms i and j (0-indexed)."""
    return np.linalg.norm(coords[i] - coords[j])

# Example:
atoms, coords = read_coordinates(r"C:\Users\jschoer\Desktop\DSA103 Coding and Tests\DSA103\exercises\lectures_11-12\yne.gjf")
print("Atoms:", atoms)
print("Coordinates:", coords)

# Compute distance between atom 0 and 1
d = bond_distance(coords, 0, 1)
print(f"Distance between {atoms[0]}-{atoms[1]}: {d:.3f} Å")
