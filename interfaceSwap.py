
import subprocess

print("###Asap interface mode 1.0###")


mode = input("Enter the mode you would like to change to (ma/mo): ")
interface = str(input("Enter an interface: "))


if mode == 'mo':
    subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'])
    subprocess.run(['sudo', 'iw', interface, 'set', 'monitor', 'control'])
    subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'])
    print("You are now in monitor mode.")
elif mode == 'ma':
    subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'down'])
    subprocess.run(['sudo', 'iw', interface,'set', 'type', 'managed'])
    subprocess.run(['sudo', 'ip', 'link', 'set', interface, 'up'])
    print("You are now in managed mode.")

else:
    print("Enter 'ma' for managed mode or 'mo' for monitor mode.")



