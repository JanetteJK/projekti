from rich.console import Console
from rich.table import Table

table = Table(title="Maat joihin voit matkustaa")

table.add_row("Meksiko", "Kreikka", "Suomi")

console = Console()
console.print(table)