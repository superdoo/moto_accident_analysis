import sqlite3
import pandas as pd

# Path to your CSV file
csv_file = 'accidents.csv'

# Read the CSV file using pandas
df = pd.read_csv(csv_file)

# Clean column names (remove spaces and convert to lowercase with underscores)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Create a SQLite database connection
conn = sqlite3.connect("accidents.db")
cursor = conn.cursor()

# Define the table schema
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accidents (
        crash_id INTEGER,
        city TEXT,
        crash_date TEXT,
        crash_death_count INTEGER,
        weather_condition TEXT,
        vehicle_make TEXT,
        vehicle_model_name TEXT,
        vehicle_model_year INTEGER,
        person_death_count INTEGER,
        person_helmet TEXT
    )
''')

# Insert the data into the table
df.to_sql('accidents', conn, if_exists='append', index=False)

# Sample query: list all accidents where a helmet was not worn
cursor.execute('''
    SELECT crash_id, city, crash_date, vehicle_make, vehicle_model_name, person_helmet
    FROM accidents
    WHERE person_helmet LIKE '%NOT WORN%'
''')

results = cursor.fetchall()

print("\nAccidents with helmet not worn:")
for row in results:
    print(row)

# Close the connection
conn.close()
