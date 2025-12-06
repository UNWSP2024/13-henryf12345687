#Henry Forst
#Week 13
#12/05/2025
import sqlite3

def main():
    # Connect to (or create) the database
    conn = sqlite3.connect('phonebook.db')
    curs = conn.cursor()

    # Drop the table if it exists
    curs.execute('DROP TABLE IF EXISTS Entries')

    # Create the Entries table
    curs.execute('''
        CREATE TABLE Entries (
            EntryID INTEGER PRIMARY KEY NOT NULL,
            Name TEXT,
            Phone TEXT
        )
    ''')

    # Insert sample rows
    entries = [
        (1, 'Ace Jones', '507-512-1234'),
        (2, 'Tim Smith', '507-555-5678'),
        (3, 'Hank Davis', '507-505-8721'),
        (4, 'Daniel Moon', '507-851-4321'),
        (5, 'Everett Johnson', '507-555-2562'),
        (6, 'Blaine Adams', '507-555-1357'),
        (7, 'Carter Wilson', '507-321-9993'),
        (8, 'Henry Clark', '507-550-8642'),
        (9, 'Ivy Herro', '507-276-7531'),
        (10, 'Jack Janicki', '507-766-6420')
    ]

    for row in entries:
        curs.execute('INSERT INTO Entries (EntryID, Name, Phone) VALUES (?, ?, ?)', row)

    # Commit changes
    conn.commit()

    # Display the table contents
    print("Contents of phonebook.db / Entries table:")
    print(f"{'ID':<5}{'Name':20}{'Phone':15}")
    curs.execute('SELECT * FROM Entries')
    results = curs.fetchall()
    for row in results:
        print(f"{row[0]:<5}{row[1]:20}{row[2]:15}")

    # Close connection
    conn.close()

if __name__ == "__main__":
    main()