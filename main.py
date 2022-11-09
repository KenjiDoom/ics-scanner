from rich.console import Console
from rich.table import Table
from sys import exit
import shodan

class scanner:
    console = Console()
    def __init__(self, *argv):
        for argv in argv:
            self.option = argv
            print("Working " + self.option)

    def nmap_scanning(self):
        console.print("[bold green] Starting nmap scan on this device")

    def output_data(self):
        pass



class startProgram:
    def run_script(self):
        console  = Console()    
        scada_selection()
        SCAN = scanner(console.input("[bold red]Enter the ICS product you want to scan: "))

    def scada_selection(self):
        console  = Console()
        """
Going a bit old school with this apporach, please don't bash me. Possible UI in the future.
Huge thanks to digital bond for providing these scripts.
        """
        console.print("[bold blue][-] AVAILABLE SCADA SCRIPTS [-]")
        console.print("[bold white][1] Rockwell Automation, port 44818")
        console.print("[bold white][2]. Niagara Fox, Port 1911")
        console.print("[bold white][3]. ATG, Port 10001")


start = startProgram()
start.scada_selection()
