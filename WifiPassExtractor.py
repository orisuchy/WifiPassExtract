import subprocess
from pathlib import Path

text_file = open("MyWifis.txt", "w")

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]
# print(' --------- My Wifi Passwords --------- \n\n')
text_file.write(' --------- My Wifi Passwords --------- \n\n')
print("Creating file: 'MyWifis.txt' at ", Path().absolute())
for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        # print(f'Name: {wifi}\nPassword: {results[0]}\n\n')
        text_file.write(f'Name: {wifi}\nPassword: {results[0]}\n\n')
    except IndexError:
        # print(f'Name: {wifi}\nPassword: !!! Cannot be read !!!\n\n')
        text_file.write(f'Name: {wifi} \nPassword: !!! Cannot be read !!!\n\n')
text_file.close()
