import sqlite3
import csv

def create_database():
    conn = sqlite3.connect('stations_data.db')
    conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key constraints
    conn.close()

def create_tables():
    conn = sqlite3.connect('stations_data.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS stations (
                        station_id TEXT PRIMARY KEY,
                        latitude REAL,
                        longitude REAL,
                        elevation REAL,
                        name TEXT,
                        country TEXT,
                        state TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS measurements (
                        station_id TEXT,
                        date TEXT,
                        precip REAL,
                        tobs REAL,
                        FOREIGN KEY (station_id) REFERENCES stations(station_id)
                    )''')

    conn.commit()
    conn.close()

def insert_stations():
    conn = sqlite3.connect('stations_data.db')
    cursor = conn.cursor()

    with open('C:\Data_Science\Python\DemoEnv\Module_6\clean_stations.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            cursor.execute("INSERT INTO stations VALUES (?, ?, ?, ?, ?, ?, ?)", row)

    conn.commit()
    conn.close()

def insert_measurements():
    conn = sqlite3.connect('stations_data.db')
    cursor = conn.cursor()

    with open('C:\Data_Science\Python\DemoEnv\Module_6\clean_measure.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            cursor.execute("INSERT INTO measurements VALUES (?, ?, ?, ?)", row)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    create_tables()
    insert_stations()
    insert_measurements()

    conn = sqlite3.connect('stations_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stations LIMIT 5")
    result = cursor.fetchall()
    print(result)

    conn.close()