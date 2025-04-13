import subprocess
import time
import os

os.system("")
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RED = "\033[91m"
RESET = "\033[0m"

print(f"{CYAN}Welcome to Auto-WiFi Tool{RESET}")
print("-" * 50)

def get_info_wifi():
    user_input = input(f'\n{YELLOW}Enter prompt here or "Q" to quit or "help" to see the commands:{RESET} ')

    if user_input.upper() == "Q":
        print(f"{RED}Exiting the program...{RESET}")
        time.sleep(1)
        return False  

    if user_input.lower() == "help":
        print(f"\n{CYAN}Available Commands:{RESET}\n")
        print(f'{GREEN}1.{RESET} Write: "{YELLOW}show wifi name{RESET}" to view saved Wi-Fi/SSID names.')
        print(f'{GREEN}2.{RESET} Write: "{YELLOW}show wifi pass{RESET}" to get the password of a saved network.')
        print(f'{GREEN}3.{RESET} Enter "{YELLOW}Q{RESET}" to exit the program.')
        print(f'{GREEN}4.{RESET} Enter "{YELLOW}help{RESET}" to show this list again.\n')
        return True

    elif user_input.lower() == "show wifi name":
        print(f"{CYAN}Opening CMD to show Wi-Fi names...{RESET}")
        time.sleep(2)
        subprocess.Popen('start cmd /k "color 02 & netsh wlan show profiles & pause"', shell=True)
        return True

    elif user_input.lower() == "show wifi pass":
        ssid = input(f"{YELLOW}Enter Wi-Fi/SSID name: {RESET}")
        print(f"{CYAN}Opening CMD to show password for '{ssid}'...{RESET}")
        time.sleep(2)
        subprocess.Popen(f'start cmd /k "color 02 & netsh wlan show profile name=\\"{ssid}\\" key=clear & pause"', shell=True)
        return True

    else:
        print(f"{RED}Invalid Input! Type 'help' to see available commands.{RESET}")
        return True

if __name__ == "__main__":
    while True:
        if not get_info_wifi():
            break
