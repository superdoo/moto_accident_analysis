import pandas as pd
import matplotlib.pyplot as plt

# List of motorcycle makes to include
motorcycle_makes = [
    "HARLEY-DAVIDSON", "HONDA", "YAMAHA", "SUZUKI", "KAWASAKI", "DUCATI",
    "BMW", "KTM", "TRIUMPH", "APRILIA", "MOTO GUZZI", "ROYAL ENFIELD",
    "HUSQVARNA", "INDIAN", "CAN-AM", "GASGAS", "BENELLI", "BETA",
    "MV AGUSTA", "URAL"
]

# Read the dataset
df = pd.read_csv("accidents.csv")

# Optional: Print column names for debugging
print("Available columns:", df.columns.tolist())

# Normalize make column values (if it exists)
if 'Vehicle Make' in df.columns:
    df['Vehicle Make'] = df['Vehicle Make'].astype(str).str.strip().str.upper()

# Filter for fatal crashes (Crash Death Count >= 1) and valid motorcycle makes
if 'Crash Death Count' in df.columns and 'Vehicle Make' in df.columns:
    fatal_motorcycles_df = df[
        (df['Crash Death Count'] >= 1) &
        df['Vehicle Make'].isin(motorcycle_makes)
    ]

    # Export filtered data
    fatal_motorcycles_df.to_csv("death_analysis.csv", index=False)

    # Generate bar chart
    plt.figure(figsize=(8, 4))
    plt.bar(['Fatal Motorcycle Crashes'], [len(fatal_motorcycles_df)])
    plt.title('Fatal Motorcycle Crashes by Selected Makes')
    plt.savefig("death_analysis.png")
    plt.show()
else:
    print("Required columns ('Crash Death Count' and/or 'Vehicle Make') not found.")
