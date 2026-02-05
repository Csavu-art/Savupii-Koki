import mysql.connector

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "KiraTina9_DB",
    "database": "flight_game"
}

def get_airport_counts(connection, country_code):
    query = f"""
        SELECT type, COUNT(*) 
        FROM flight_game.airport
        WHERE iso_country = "{country_code}"
        GROUP BY type
    """
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

def print_rows(rows):
    if rows == None or len(rows) == 0:
        print("Not found")
        return

    for row in rows:
        print(row[0], row[1])

def main():
    connection = mysql.connector.connect(**DB_CONFIG)

    country_code = input("Enter country code (e.g. FI): ")
    rows = get_airport_counts(connection, country_code)
    print_rows(rows)

    connection.close()

main()
