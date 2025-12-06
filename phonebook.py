#Henry Forst
#Week 13
#12/05/2025
import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    curs = conn.cursor()

    while True:
        print("\nPhonebook Menu")
        print("1. View all entries")
        print("2. Update an entry")
        print("3. Delete an entry")
        print("4. Quit")
        choice = input("Enter choice (1-4):")

        if choice == "1":
            view_entries(curs)
        elif choice == "2":
            update_entry(curs, conn)
        elif choice == "3":
            delete_entry(curs, conn)
        else:
            print("Invalid. Try again.")
    conn.close()
def view_entries(curs):
    curs.execute("SELECT * FROM Entries")
    results = curs.fetchall()
    print("\nContents of phonebook.db / Entries table:")
    print(f"{'ID':<5}{'Name':20}{'Phone':15}")
    for row in results:
        print(f"{row[0]:<5}{row[1]:20}{row[2]:15}")
def update_entry(curs, conn):
    entry_id = input("Enter the ID of the entry to update: ")
    new_name = input("Enter new name (leave blank to keep current name): ")
    new_phone = input("Enter new phone number (leave blank to keep current phone number): ")
    curs.execute("SELECT Name, Phone FROM Entries WHERE EntryID=?", (entry_id,))
    row = curs.fetchone()
    if row is None:
        print("Entry not found.")
        return
    name = new_name if new_name else row[0]
    phone = new_phone if new_phone else row[1]

    curs.execute("UPDATE Entries SET Name=?, Phone=? WHERE EntryID=?",(name, phone, entry_id))
    conn.commit()
    print("Entry updated successfully.")
def delete_entry(curs, conn):
    entry_id = input("Enter the ID of the entry to delete: ")
    curs.execute("DELETE FROM Entries WHERE EntryID=?", (entry_id,))
    conn.commit()
    print("Entry deleted.")
if __name__ == "__main__":
    main()
