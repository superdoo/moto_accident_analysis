import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('accidents.db')

# Load data from the 'accidents' table
df = pd.read_sql_query("SELECT * FROM accidents", conn)

# Close the DB connection
conn.close()

# Replace 'Person Helmet' and any other column names as needed
helmet_stats = df['Person Helmet'].value_counts()
# Assuming there is a 'Speeding' column (update if needed)
speeding_stats = df[df['Speeding'] == True]

# Export results to CSV
helmet_stats.to_csv("helmet_report.csv")
speeding_stats.to_csv("speeding_report.csv")

# Plot helmet usage
helmet_stats.plot(kind="bar", title="Helmet Use")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("helmet_use.png")
