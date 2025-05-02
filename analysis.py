import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    df = pd.read_csv("accidents.csv")
    helmet_df = df[df['Contributing Factor 1 Description'].str.contains('helmet', case=False, na=False)]
    speeding_df = df[df['Contributing Factor 1 Description'].str.contains('speed', case=False, na=False)]

    helmet_df.to_csv("helmet_related_accidents.csv", index=False)
    speeding_df.to_csv("speeding_related_accidents.csv", index=False)

    plt.figure(figsize=(6,4))
    plt.bar(['Helmet Related', 'Speeding Related'], [len(helmet_df), len(speeding_df)])
    plt.title('Motorcycle Accidents: Helmet vs Speeding')
    plt.savefig("accident_analysis.png")

if __name__ == "__main__":
    analyze_data()
