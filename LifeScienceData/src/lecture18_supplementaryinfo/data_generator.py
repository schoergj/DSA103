import numpy as np
import pandas as pd

RNG = np.random.default_rng(0)  # reproducible RNG


# Synthetic enzyme kinetics plot
substrates = np.concatenate([np.linspace(0.01, 10, 12), np.linspace(0.05, 8, 12)])  # two series lengths combined
substrates = np.sort(substrates)

# Michaelis-Menten type curves with noise
def mm_rate(S, Vmax, Km):
    return Vmax * S / (Km + S)

# create measurements for two enzymes across substrate concentrations at replicates
enzymes = []
rows = []
for enzyme_id, (Vmax, Km) in enumerate([(120, 2.5), (80, 1.2)], start=1):
    for rep in range(4):  # 4 replicates
        noise = RNG.normal(0, 4, size=substrates.shape)  # measurement noise
        rate = mm_rate(substrates, Vmax, Km) + noise
        # introduce a few missing values
        mask = RNG.choice([True, False], size=substrates.shape, p=[0.95, 0.05])
        rate[~mask] = np.nan
        for S, r in zip(substrates, rate):
            rows.append({'enzyme': f'Enzyme_{enzyme_id}', 'replicate': rep+1, 'substrate_mM': float(S), 'rate': float(r)})
enzyme_kinetics_df = pd.DataFrame(rows)
# enzyme_kinetics_df.head()
enzyme_kinetics_df.to_csv("enzyme_kinetics_df.csv", index=False)


# Protein melting curves (synthetic)
temps = np.linspace(20, 95, 30)
proteins = ['WT', 'MutA', 'MutB']
rows = []
for p in proteins:
    Tm = {'WT': 55, 'MutA': 48, 'MutB': 62}[p]
    for rep in range(5):
        # sigmoidal melting curve with noise
        slope = RNG.normal(0.2, 0.02)
        baseline = RNG.normal(100, 5)
        amplitude = RNG.normal(-80, 5)
        fluorescence = baseline + amplitude / (1 + np.exp((temps - Tm) / slope))
        fluorescence += RNG.normal(0, 3, size=temps.shape)
        # random NaNs to simulate missing timepoints
        nan_mask = RNG.choice([1, 0], size=temps.shape, p=[0.96, 0.04]).astype(bool)
        fluorescence[~nan_mask] = np.nan
        for T, f in zip(temps, fluorescence):
            rows.append({'protein': p, 'replicate': rep+1, 'temp_C': float(T), 'fluorescence': float(f)})
protein_melting_df = pd.DataFrame(rows)
# protein_melting_df.head()
protein_melting_df.to_csv("protein_melting.csv", index=False)

