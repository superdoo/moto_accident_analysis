import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("accidents.csv")

# Filter for helmet-related records where helmet was not worn (code 1)
helmet_df = df[df['Person Helmet'].str.startswith('1')]

# Since no 'speed' column is present, we skip the speeding-related analysis
# Optionally, you could add logic here if speeding is represented another way

# Export helmet-related accidents
helmet_df.to_csv("helmet_not_worn_accidents.csv", index=False)

# Generate bar chart
plt.figure(figsize=(6, 4))
plt.bar(['Helmet Not Worn'], [len(helmet_df)])
plt.title('Motorcycle Accidents: Helmet Not Worn')
plt.savefig("accident_analysis.png")


if __name__ == "__main__":
    analyze_data()
