import os
import win32api
import subprocess
import time
import random
import string
from Chromify import *
from colorama import just_fix_windows_console
just_fix_windows_console()
def create_appdata_directory(new_dir_name):
    appdata_dir = os.getenv('APPDATA')

    new_dir_path = os.path.join(appdata_dir, new_dir_name)

    if not os.path.exists(new_dir_path):
        os.makedirs(new_dir_path)
        return new_dir_path
    else:
        return new_dir_path

appdata_path = os.getenv("APPDATA")
folder_path = os.path.join(appdata_path, "System32-WINx64")
new_directory_name = "SystemCache"
directory = create_appdata_directory(new_directory_name)

def generate_numbers(length):
    if length <= 0:
        raise ValueError("Length must be a positive integer")
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def generate_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

try:
    os.makedirs(folder_path)

    win32api.SetFileAttributes(folder_path, 2) 
except Exception as Error:
    print("Checking Serials...")

with open(f'{folder_path}/SystemDRV32.bat', "w") as f:
    f.write(f'@echo off\n\ncd {folder_path}\n\nAMIDEWINx64.exe /BS 210{generate_numbers(12)} > nul\nAMIDEWINx64.exe /SU AUTO > nul\nAMIDEWINx64.exe /PSN {generate_string(13)} > nul\nAMIDEWINx64.exe /SS {generate_string(13)} > nul\nAMIDEWINx64.exe /CS "Default string" > nul\n\nnet stop winmgmt /y > nul\ntimeout /t 2 /nobreak > nul\nnet start winmgmt /y > nul\nexit')

def SerialChecker():
    bios = (subprocess.run('wmic bios get serialnumber', shell= True, capture_output= True).stdout.decode(errors='ignore')).strip().split('\r\n\r\n')[0]
    bios = bios.split()[-1]
    smbios = (subprocess.run('wmic csproduct get uuid', shell= True, capture_output= True).stdout.decode(errors='ignore')).strip().split('\r\n\r\n')[0]
    smbios = smbios.split()[-1]
    cpu = (subprocess.run('wmic cpu get serialnumber', shell= True, capture_output= True).stdout.decode(errors='ignore')).strip().split('\r\n\r\n')[0]
    cpu = cpu.split()[-1]
    baseboard = (subprocess.run('wmic baseboard get serialnumber', shell= True, capture_output= True).stdout.decode(errors='ignore')).strip().split('\r\n\r\n')[0]
    SerialChecker_Return = { "Bios": bios, "SMBIOS": smbios, "CPU": cpu, "BaseBoard": baseboard}
    return SerialChecker_Return
import subprocess

myStartingColor = Color("#0800ff")
myEndingColor = Color(0, 255, 0)
Console = gradient(myStartingColor, myEndingColor, f'''
     _                       __  _     ___   ____ _  _______ ____  
    / \   ___ _   _ ___     / / | |   / _ \ / ___| |/ / ____|  _ \ 
   / _ \ / __| | | / __|   / /  | |  | | | | |   | ' /|  _| | | | |
  / ___ \\__ \ |_| \__ \  / /   | |__| |_| | |___| . \| |___| |_| |
 /_/   \_\___/\__,_|___/ /_/    |_____\___/ \____|_|\_\_____|____/ 
                                                                   
Spoof Completed, Thank you for using Joony Perm V1.
Getting Serials & Checking...
''', background=False)
import subprocess

def get_mac_addresses():
    try:
        output = subprocess.check_output(["wmic", "nic", "get", "MACAddress"])
        lines = output.decode("utf-8").split('\n')
        mac_addresses = [line.strip() for line in lines if line.strip()]
        mac_addresses = [mac for mac in mac_addresses if mac != "MACAddress"]
        return ', '.join(mac_addresses)
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve MAC addresses.")
        return None

mac_addresses = get_mac_addresses()
time.sleep(10)
Serial_Dict = SerialChecker()
print(Console)
myStartingColor = Color("#FF0000")
myEndingColor = Color(0, 255, 0)
print(gradient(myStartingColor, myEndingColor, f'BASEBOARD/MOTHERBOARD', background=False))
myStartingColor = Color("#3483eb")
myEndingColor = Color("#34ebde")
print(gradient(myStartingColor, myEndingColor, f'{Serial_Dict["BaseBoard"]}\n', background=False))
myStartingColor = Color("#FF0000")
myEndingColor = Color(0, 255, 0)
print(gradient(myStartingColor, myEndingColor, f'CPU', background=False))
myStartingColor = Color("#3483eb")
myEndingColor = Color("#34ebde")
print(gradient(myStartingColor, myEndingColor, f'{Serial_Dict["CPU"]}\n', background=False))
myStartingColor = Color("#FF0000")
myEndingColor = Color(0, 255, 0)
print(gradient(myStartingColor, myEndingColor, f'SMBIOS', background=False))
myStartingColor = Color("#3483eb")
myEndingColor = Color("#34ebde")
print(gradient(myStartingColor, myEndingColor, f'{Serial_Dict["SMBIOS"]}\n', background=False))
myStartingColor = Color("#FF0000")
myEndingColor = Color(0, 255, 0)
print(gradient(myStartingColor, myEndingColor, f'MAC ADDRESS', background=False))
myStartingColor = Color("#3483eb")
myEndingColor = Color("#34ebde")
print(gradient(myStartingColor, myEndingColor, f'{mac_addresses}\n', background=False))
time.sleep(10)