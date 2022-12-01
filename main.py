from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
import subprocess
import getpass
import shodan

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
            self.shodan_menu()
        else:
            self.console.print(self.option, "is not an option, exiting...")
            exit()
    """ 
    Is there a way to remove all this junk?, If statements look a bit outdated.
    """

    def rockwell_automation(self):
        table = Table(title="Nmap results for Rockwell Automation Systems")
        table.add_column("TCP")
        table.add_column("UDP")
        with self.console.status("Scanning...") as status:
            subprocess.run(['clear'])
            self.console.log(table.add_row(subprocess.Popen(['nmap', '--script', 'enip-info', '-Pn', '-p', '44818', self.IP, '-oN', self.IP + '_TCP_SCAN.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8'), subprocess.Popen(['nmap', '--script', 'enip-info', '-sU', '-Pn', '-p', '44818', self.IP, '-oN', self.IP + '_UDP_SCAN.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')))
        self.console.print(table)
        self.shodan_menu()

    def niagara_fox(self):
        table = Table(title="NMAP RESULTS")
        table.add_column("Nmap results for Niagara Fox System")
        with self.console.status("Scanning...") as status:
            subprocess.run(['clear'])
            table.add_row(subprocess.Popen(['nmap', '-Pn', '-sT', '--script', 'fox-info.nse', '-p', '1911,4911', self.IP, '-oN', self.IP + '_TCP.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8'))
        self.console.print(table)
        self.shodan_menu()

    def shodan_menu(self):
        sho = Prompt.ask("Run shodan scan on IP? Y/N")
        if sho.upper == 'YES' or sho.upper() == 'Y':
            self.shodan_scan()
            self.output_format()
        elif sho.upper == 'NO' or sho.upper() == 'N':
            print('Exiting...')
        else:
            print('Exiting....')

    def shodan_scan(self):
        api = shodan.Shodan('')
        host = api.host(self.IP)
        self.ip, self.banner, self.port, self.city, self.domains, self.asn = [],[],[],[],[],[]
        for items in host['data']:
            self.ip.append(items['ip_str'])
            self.banner.append(items['data'])
            self.port.append(items['port'])
            self.city.append(host.get('city', 'n/a'))
            self.domains.append(host.get('domain', 'n/a'))
            self.asn.append(items['asn'])

        #print(len(self.ip), len(self.city), len(self.port), len(self.domains), len(self.asn)) # Verifying that they all match
    def output_format(self):
        table = Table(title="Shodan results")
        table = Table(show_lines = True)

        table.add_column("IP", justify="right", style="green", no_wrap=True)
        table.add_column("Banner", justify="right", style="white")
        table.add_column("Port", style="red")
        table.add_column("City", justify="right", style="green")
        table.add_column("Domains", style="red")
        table.add_column("ASN", style="Cyan")
        
        for index, (a, b, c, d, e, f) in enumerate(zip(self.ip, self.banner, self.port, self.city, self.domains, self.asn)):
            table.add_row(str(a), str(b), str(c), str(d), str(e), str(f))
        
        self.console.print(table)

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
        table.add_column(header="2.", justify="middle", no_wrap=True)
        table.add_column(header="3.", justify="right", no_wrap=True)
        table.add_row(Panel.fit("Rockwell Automation port 44818"), Panel.fit("Niagara Fox port 1911 or 4199"), Panel.fit("Shodan Scan Results"))
        self.console.print(table)
    
    def IP_menu(self):
        table = Table(title="[bold red]IP address information", title_style="bold magenta")
        table = Table()
        table.add_column(header="1. IP Address information", justify="left", no_wrap=True)
        table.add_row(Panel.fit("Enter the IP address of the target you want to scan."))
        self.console.print(table)
        self.IP_address = Prompt.ask("Enter IP address")

    def get_root(self):
        self.console = Console()
        if getpass.getuser() == 'root':
            pass
        else:
            try:
                self.console.print("⚠️[bold red] Root needed for nmap, would you like to run as root?⚠️")
                root_priv = Prompt.ask("[bold green]Y/N")
                if root_priv.upper() == "Y" or root_priv.upper() == "YES":
                    subprocess.run(['clear'])
                    subprocess.run(['sudo', 'python3', 'main.py'])
                elif root_priv.upper() == "N" or root_priv.upper() == "NO":
                    self.console.print("[bold red]Exiting...")
                    self.console.print("[bold red]Root privileges required.")
                    exit()
                exit()
            except KeyboardInterrupt:
                self.console.print("\nExiting...")
                exit()

if __name__ == '__main__':
    start = startProgram()
    start.get_root()
    start.run_program()
