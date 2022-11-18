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
        for argv in argv: # Provide the user to save the output to a file, that code will go here
            self.option = argv
        if self.option == '1':
            self.rockwell_automation()
        elif self.option == '2':
            self.niagara_fox()
        else:
            self.console.print(self.option, "is not an option, exiting...")
            exit()
    """ 
    Is there a way to remove all this junk?, If statements look a bit outdated.
    """

    def rockwell_automation(self):
        table = Table(title="Nmap results")
        table.add_column("Nmap results for rockwell automation systems")
        table.add_row(str(subprocess.run(['nmap', '--script', 'enip-info', '-sU', '-Pn', '-p', '44818', self.IP], capture_output=True)))
        self.console.print(table)
    
    def niagara_fox(self):
        table = Table(title="NMAP RESULTS")
        table.add_column("Nmap results for Niagara Fox System")
        table.add_row(subprocess.Popen(['nmap', '-Pn', '-sT', '--script', 'fox-info.nse', '-p', '1911,4911', self.IP], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8'))
        self.console.print(table)

    def atg(self):
        pass
        # To-do: Fix the orginal nse script, doesn't work becasue the code version is deprecated
        # Also note I tried using the nmap python API but it doesn't provide custom scripts

class startProgram:
    console = Console()
    def run_program(self):
        try:
            self.console = Console()
            self.IP_menu()
            subprocess.run(['clear'])
            self.scada_menu()
            SCAN = scanner(self.IP_address)
            SCAN.scada_selection(Prompt.ask("Enter the ICS Product you want to scan"))
        except KeyboardInterrupt:
                self.console.print("[bold red]Exiting...")
                exit()

    def scada_menu(self):
        table = Table(title="[bold red] Scada Scans available ", title_style="bold magenta")
        table.add_column(header="1.", justify="left", no_wrap=True)
        table.add_column(header="2.", justify="right", no_wrap=True)
        table.add_row(Panel.fit("Rockwell Automation port 44818"), Panel.fit("Niagara Fox port 1911 or 4199"))
        self.console.print(table)
    
    def IP_menu(self):
        table = Table(title="[bold red]IP address information", title_style="bold magenta")
        table.add_column(header="1.", justify="left", no_wrap=True)
        table.add_row(Panel.fit("Enter the IP address of the target you want to scan."))
        self.console.print(table)
        self.IP_address = Prompt.ask("Enter IP address")

    def get_root(self):
        self.console = Console()
        if getpass.getuser() == 'root':
            pass
        else:
            try:
                self.console.print("Root needed for nmap, would you like to run as root?")
                root_priv = Prompt.ask("Y/N")
                if root_priv.upper() == "Y" or root_priv.upper() == "YES":
                    subprocess.run(['clear'])
                    subprocess.run(['sudo', 'python', 'main.py'])
                elif root_priv.upper() == "N" or root_priv.upper() == "NO":
                    self.console.print("Root privileges required.")
                    exit()
                exit()
            except KeyboardInterrupt:
                self.console.print("\nExiting...")
                exit()

start = startProgram()
start.get_root()
start.run_program()
