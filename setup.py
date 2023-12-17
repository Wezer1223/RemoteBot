import time
from tqdm import tqdm
from colorama import init, Fore

init(autoreset=True)

def simulate_save():
    for _ in tqdm(range(4), desc="Saving"):
        time.sleep(0.5)

def ask_question(question):
    return input(question + " ")

def write_config_file(answers):
    with open('config.py', 'w') as config_file:
        config_file.write(f'token = "{answers[0]}"\n')
        config_file.write(f'admin = {answers[1]}\n')

def main():
    
    print(Fore.LIGHTCYAN_EX + "  ██▀███  ▓█████  ███▄ ▄███▓ ▒█████  ▄▄▄█████▓▓█████     ██▓███   ▄████▄  ")   
    print(Fore.LIGHTCYAN_EX + " ▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒▓  ██▒ ▓▒▓█   ▀    ▓██░  ██▒▒██▀ ▀█  ")  
    print(Fore.LIGHTCYAN_EX + " ▓██ ░▄█ ▒▒███   ▓██    ▓██░▒██░  ██▒▒ ▓██░ ▒░▒███      ▓██░ ██▓▒▒▓█    ▄ ")  
    print(Fore.LIGHTCYAN_EX + " ▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒██   ██░░ ▓██▓ ░ ▒▓█  ▄    ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒")  
    print(Fore.LIGHTCYAN_EX + " ░██▓ ▒██▒░▒████▒▒██▒   ░██▒░ ████▓▒░  ▒██▒ ░ ░▒████▒   ▒██▒ ░  ░▒ ▓███▀ ░")  
    print(Fore.LIGHTCYAN_EX + " ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░   ▒ ░░   ░░ ▒░ ░   ▒▓▒░ ░  ░░ ░▒ ▒  ░")  
    print(Fore.LIGHTCYAN_EX + "   ░▒ ░ ▒░ ░ ░  ░░  ░      ░  ░ ▒ ▒░     ░     ░ ░  ░   ░▒ ░       ░  ▒   ")  
    print(Fore.LIGHTCYAN_EX + "   ░░   ░    ░   ░      ░   ░ ░ ░ ▒    ░         ░      ░░       ░        ")  
    print(Fore.LIGHTCYAN_EX + "    ░        ░  ░       ░       ░ ░              ░  ░            ░ ░      ") 
    print(Fore.LIGHTCYAN_EX + "                                                                 ░\n\n\n\n\n\n")  
                                                                                                                         

    print("Program for setting up a configuration file")
    
    answer1 = ask_question("Enter the token for your bot:")
    answer2 = ask_question("Enter your ID (it will be used to manage the computer):")

    answers = [answer1, answer2]

    write_config_file(answers)

    simulate_save()
    print("The answers have been successfully recorded, enjoy your use.")

if __name__ == "__main__":
    main()