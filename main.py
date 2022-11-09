from rich.console import Console
from rich.table import Table
from sys import exit
import shodan 
import nmap3

class scanner:
    def __init__(self, *argv):
        for argv in argv:
            self.option = argv
            print("Working " + self.option)

    def nmap_scanning(self):
        pass

    def output_data(self):
        pass

console = Console()
SCAN = scanner(console.input("[bold red]Enter the ICS product you want to scan: "))
