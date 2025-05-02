import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("accidents.csv")

# Check the columns to make sure 'Crash Death Count' exists
print("DataFrame columns:", df.columns)

# Normalize column names to lowercase and strip spaces for consistency
df.columns = df.columns.str.strip().str.lower()

# Filter for fatal crashes where death count is >= 1
if 'crash death count' in df.columns:
    fatal_df = df[df['crash death count'] >= 1]

    # Export fatal crashes to a new CSV
    fatal_df.to_csv("death_analysis.csv", index=False)

    # Generate bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(['Fatal Crashes'], [len(fatal_df)])
    plt.title('Motorcycle Accidents: Fatal Crashes')
    plt.savefig("death_analysis.png")
    plt.show()
else:
    print("'Crash Death Count' column not found.")
