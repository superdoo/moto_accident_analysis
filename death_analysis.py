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

# Normalize column names to lowercase and strip spaces
df.columns = df.columns.str.strip().str.lower()

# Normalize make column values (if it exists)
if 'make' in df.columns:
    df['make'] = df['make'].astype(str).str.strip().str.upper()

# Filter for fatal crashes (Crash Death Count >= 1) and valid motorcycle makes
if 'crash death count' in df.columns and 'make' in df.columns:
    fatal_motorcycles_df = df[
        (df['crash death count'] >= 1) &
        (df['Vehicle Make'].isin([Vehicle Make.upper() for Vehicle Make in motorcycle_makes]))
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
    print("Required columns ('Crash Death Count' and/or 'Make') not found.")
