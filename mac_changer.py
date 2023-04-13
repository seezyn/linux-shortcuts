import subprocess

interface = input("Enter an interface: ")
new_mac = input("Enter your new MAC address: ")

print("[+] Changing MAC address to  " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

