from venv import create
from rich.theme import Theme
from rich.console import Console
from rich.table import Table

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="niittykuja4MAR",
        database="flight_game",
        collation='latin1_swedish_ci',
        autocommit=True
    )

custom_theme = Theme({"gre" : "red"})
table = Table(title="Matkatoimisto")

console = Console(theme=custom_theme)

table.add_column("Maat joihin voit matkustaa", style='gre')
table.add_row("Meksiko")
table.add_row("")
table.add_row("Islanti")
table.add_row("Islanti")
table.add_row("Islanti")

console.print(table)

