import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("accidents.csv")

# Filter for helmet not worn (from 'Person Helmet' column)
helmet_df = df[df['Person Helmet'].astype(str).str.upper().str.contains("NOT WORN")]

# Filter for speeding-related accidents (still based on contributing factor column)
speeding_df = df[df['Contributing Factor 1 Description'].str.contains('speed', case=False, na=False)]

# Save filtered data to CSV files
helmet_df.to_csv("helmet_related_accidents.csv", index=False)
speeding_df.to_csv("speeding_related_accidents.csv", index=False)

# Plot a bar chart
plt.figure(figsize=(6, 4))
plt.bar(['Helmet Not Worn', 'Speeding Related'], [len(helmet_df), len(speeding_df)])
plt.title('Motorcycle Accidents: Helmet Not Worn vs Speeding')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.savefig("accident_analysis.png")


if __name__ == "__main__":
    analyze_data()
