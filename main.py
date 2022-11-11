from rich.console import Console
from rich.table import Table
import subprocess

# How to get IP address at the top of the code?
class scanner:
    console = Console()
    def __init__(self, *argv):
        for argv in argv:
            self.IP = argv
    def scada_selection(self, *argv):
        for argv in argv:
            self.option = argv
        if self.option == '1':
            self.rockwell_automation()
        elif self.option == '2':
            self.niagara_fox()
        elif self.option == '3':
            self.atg()
    """ 
    Is there a way to remove all this junk?, If statements look a bit outdated.
    """

    def rockwell_automation(self):
        rock_scan = subprocess.run(['nmap', '--script', 'enip-info', '-sU', '-Pn', '-p', '44818', self.IP])
    
    def niagara_fox(self):
        nia_scan = subprocess.run(['nmap', '-Pn', '-sT', '--script', 'fox-info.nse', '-p', '1911,4911', self.IP])
    
    def atg(self):
        print("You chose atg")

    def output_data(self):
        pass 

class startProgram:
    def run_program(self):
        self.console = Console()
        self.scada_display()
        SCAN = scanner(self.console.input("[bold cyan]Enter IP address: "))
        SCAN.scada_selection(self.console.input("[bold cyan]Enter the ICS Product you want to scan:"))

    def scada_display(self):
        """
Going a bit old school with this apporach, please don't bash me. Possible UI in the future.
Huge thanks to digital bond for providing these scripts.
[New Note] Use the rich libary to output this information onto the middle of the sceen using a box like format.
        """
        self.console.print("[bold blue][-] AVAILABLE SCADA SCRIPTS [-]")
        self.console.print("[bold white][1]. Rockwell Automation, port 44818")
        self.console.print("[bold white][2]. Niagara Fox, Port 1911")
        self.console.print("[bold white][3]. ATG, Port 10001")


start = startProgram()
start.run_program()
