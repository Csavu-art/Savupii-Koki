import mysql.connector
from geopy.distance import geodesic

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "admin",
    "password": "KiraTina9_DB",
    "database": "flight_game"
}

def get_coordinates(connection, icao):
    query = f"""
        SELECT latitude_deg, longitude_deg
        FROM flight_game.airport
        WHERE ident = "{icao}"
    """
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    return row

def main():
    connection = mysql.connector.connect(**DB_CONFIG)

    icao1 = input("Enter first ICAO-code: ")
    icao2 = input("Enter second ICAO-code: ")

    coord1 = get_coordinates(connection, icao1)
    coord2 = get_coordinates(connection, icao2)

    if coord1 == None or coord2 == None:
        print("Airport not found")
    else:
        distance_km = geodesic(coord1, coord2).kilometers
        print(f"Distance: {distance_km:.2f} km")

    connection.close()

main()
