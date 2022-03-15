
import subprocess as su
command = su.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifi_name = [all.split(":")[1][1:-1] for all in command if "All User Profile" in all]
count = len(wifi_name)
print("\n  All number of wifi networks in your computer is", count)
print("-------------------------------------------------------")
print("Name of Wifi                    |  Wifi Password\n")

for all in wifi_name:
    try:
        results = su.check_output(['netsh', 'wlan', 'show', 'profile', all, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    except UnicodeDecodeError:
        continue
    try:
        print(" {:<30}==>  {:<}".format(all, results[0]))

    except IndexError:
        print(" {:<30}==>   contain is with no passward  {:<}".format(all, ""))

input()
