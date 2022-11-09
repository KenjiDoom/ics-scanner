from rich.console import Console
from rich.table import Table
from sys import exit
import shodan

class scanner:
    console = Console()
    def __init__(self, *argv):
        for argv in argv:
            self.option = argv

    def rockwell_automation(self):
        print("You chose rockwell")
    
    def niagara_fox(self):
        print("You chose niagara")
    
    def atg(self):
        print("You chose atg")

    def output_data(self):
        pass

class startProgram:
    def run_program(self):
        console = Console()
        self.scada_selection()
        SCAN = scanner(console.input("[bold red]Enter the ICS product you want to scan: "))

    def scada_selection(self):
        console  = Console()
        """
Going a bit old school with this apporach, please don't bash me. Possible UI in the future.
Huge thanks to digital bond for providing these scripts.
        """
        console.print("[bold blue][-] AVAILABLE SCADA SCRIPTS [-]")
        console.print("[bold white][1]. Rockwell Automation, port 44818")
        console.print("[bold white][2]. Niagara Fox, Port 1911")
        console.print("[bold white][3]. ATG, Port 10001")


start = startProgram()
start.run_program()
