import pandas as pd
import matplotlib.pyplot as plt

# List of motorcycle makes to include (already in uppercase)
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

# Debugging: print unique values in 'Vehicle Make' column
print("Unique Vehicle Makes in CSV:")
print(df['Vehicle Make'].unique())  # Assuming 'Vehicle Make' is the correct column name after lowercase normalization

# Ensure 'Vehicle Make' column values are properly stripped of spaces (no need for uppercase conversion)
if 'Vehicle Make' in df.columns:
    df['Vehicle Make'] = df['Vehicle Make'].astype(str).str.strip()  # Strip spaces

    # Filter for valid motorcycle makes in 'Vehicle Make' column
    fatal_motorcycles_df = df[
        df['Vehicle Make'].isin(motorcycle_makes)  # Direct comparison since both are already uppercase
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
    print("Required 'Vehicle Make' column not found.")
