#Tänne kaikki funktion kutsunnat
import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='lauri1',
    password='Kukkokiekuu1',
    autocommit=True
    )


def main():
