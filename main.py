from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
import subprocess
import getpass

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
        # To-do: Fix the orginal nse script, doesn't work becasue the code version is deprecated
        pass 

class startProgram:
    def run_program(self):
        self.console = Console()
        self.scada_display()
        SCAN = scanner(Prompt.ask("Enter IP address"))
        SCAN.scada_selection(self.console.input("Enter the ICS Product you want to scan:"))

    def scada_display(self):
        table = Table(title="[bold red] Scada Scans available ", title_style="bold magenta")
        table.add_column(header="1.", justify="left", no_wrap=True)
        table.add_column(header="2.", justify="right", no_wrap=True)
        table.add_row(Panel.fit("Rockwell Automation port 44818"), Panel.fit("Niagara Fox port 1911 or 4199"))
        self.console.print(table)
     
    def get_root(self):
        if getpass.getuser() == 'root':
            pass
        else: 
            try:
                print("Root needed for nmap. Please run as root")
                print("Would you like to run as root?")
                root_priv = input("Y/N: ")
                if root_priv.upper() == "Y" or root_priv.upper() == "YES":
                    print("Running as root")
                    subprocess.run(['sudo', 'python', 'main.py'])
                elif root_priv.upper() == "N" or root_priv.upper() == "NO":
                    print("Exiting program.. Root priv required.")
                    exit()
                exit()
            except KeyboardInterrupt:
                print("Exiting program")
                exit()

start = startProgram()
start.get_root()
start.run_program()
