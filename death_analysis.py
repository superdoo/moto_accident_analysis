import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Motorcycle brands to include
motorcycle_makes = [
    "HARLEY-DAVIDSON", "HONDA", "YAMAHA", "SUZUKI", "KAWASAKI", "DUCATI",
    "BMW", "KTM", "TRIUMPH", "APRILIA", "MOTO GUZZI", "ROYAL ENFIELD",
    "HUSQVARNA", "INDIAN", "CAN-AM", "GASGAS", "BENELLI", "BETA",
    "MV AGUSTA", "URAL"
]

# Load data
df = pd.read_csv("accidents.csv")

# Normalize data
df['Vehicle Make'] = df['Vehicle Make'].astype(str).str.upper().str.strip()
df['Crash Death Count'] = pd.to_numeric(df['Crash Death Count'], errors='coerce').fillna(0).astype(int)
df['Person Helmet'] = df['Person Helmet'].astype(str).str.upper().str.strip()

# Filter for fatal motorcycle crashes
fatal_motorcycles_df = df[
    (df['Crash Death Count'] >= 1) &
    (df['Vehicle Make'].isin(motorcycle_makes))
]

# Save the filtered dataset
fatal_motorcycles_df.to_csv("death_analysis.csv", index=False)

# ---- Chart 1: Fatalities by Make ----
death_counts = fatal_motorcycles_df.groupby('Vehicle Make').size().reset_index(name='Fatal Crashes')
death_counts = death_counts.sort_values(by='Fatal Crashes', ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(data=death_counts, x='Vehicle Make', y='Fatal Crashes', palette='magma')
plt.xticks(rotation=45, ha='right')
plt.title('Fatal Motorcycle Crashes by Vehicle Make')
plt.xlabel('Motorcycle Make')
plt.ylabel('Number of Fatal Crashes')
plt.tight_layout()
plt.savefig("death_by_make.png")
plt.close()

# ---- Chart 2: Helmet Use by Make ----
# Normalize helmet status
def normalize_helmet(status):
    if "NOT WORN" in status:
        return "Not Worn"
    elif "WORN" in status:
        return "Worn"
    else:
        return "Unknown"

fatal_motorcycles_df['Helmet Status'] = fatal_motorcycles_df['Person Helmet'].apply(normalize_helmet)

# Group by make and helmet use
helmet_counts = fatal_motorcycles_df.groupby(['Vehicle Make', 'Helmet Status']).size().unstack(fill_value=0)

# Sort by total crashes per make
helmet_counts = helmet_counts.loc[helmet_counts.sum(axis=1).sort_values(ascending=False).index]

# Plot stacked bar chart
helmet_counts.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='coolwarm')
plt.title('Helmet Use in Fatal Motorcycle Crashes by Make')
plt.xlabel('Motorcycle Make')
plt.ylabel('Number of Fatal Crashes')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Helmet Status')
plt.tight_layout()
plt.savefig("helmet_use_by_make.png")
plt.close()
