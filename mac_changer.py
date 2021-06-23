import subprocess
import optparse

def change_mac(interface,new_mac):
    print("[*]Changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])




def get_arguments():
    whoistcp=optparse.OptionParser()
    whoistcp.add_option("-i","--i",dest="interface",help="interface to change MAC address...")
    whoistcp.add_option("-m","--mac", dest="new_mac",help="New mac address")
    (options, arguments) = whoistcp.parse_args()
    if not options.interface:
        whoistcp.error("[-] specify an interface ,use -h or --help for help")
    if not options.new_mac:
        whoistcp.error("[-] specify an new MAC ,use -h or --help for help")
    else:
        return options


options =get_arguments()
change_mac(options.interface,options.new_mac)



