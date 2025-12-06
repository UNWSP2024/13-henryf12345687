#Henry Forst
#Week 13
#12/05/2025
import sqlite3

def main():
    conn = sqlite3.connect('cities.db')
    curs = conn.cursor()
    curs.execute('Select * From Cities')
    results = curs.fetchall()

    print("Contenets of cities.db / Cities table:")
    print(f"{'ID':<5}{'City Name':20}{'Population':>15}")
    for row in results:
        city_id, city_name, population = row
        print(f"{city_id:<5}{city_name:20}{population:15,.0f}")
    conn.close()
if __name__ == "__main__":
    main()