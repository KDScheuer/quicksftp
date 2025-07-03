import secrets
import random
import os
from datetime import datetime


class SFTPServer:
    def __init__(self):
        self.username = randomString(strLength=16, symbols=False)
        self.password = randomString()
        self.listenAddr = "127.0.0.1"
        self.listenPort = "2022"
        self.timeoutMin = 30
        self.whenStarted = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    def display_connection_information(self):
        GREEN = "\033[32m"
        RESET = "\033[0m"
        os.system('cls' if os.name == 'nt' else 'clear')
        print(fr"""{GREEN}
======================================================================
              
 ██████╗ ██╗   ██╗██╗ ██████╗██╗  ██╗███████╗███████╗████████╗██████╗ 
██╔═══██╗██║   ██║██║██╔════╝██║ ██╔╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗
██║   ██║██║   ██║██║██║     █████╔╝ ███████╗█████╗     ██║   ██████╔╝
██║▄▄ ██║██║   ██║██║██║     ██╔═██╗ ╚════██║██╔══╝     ██║   ██╔═══╝ 
╚██████╔╝╚██████╔╝██║╚██████╗██║  ██╗███████║██║        ██║   ██║     
 ╚══▀▀═╝  ╚═════╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝        ╚═╝   ╚═╝     

======================================================================{RESET}""")
        print(f"{GREEN}SFTP Service Started at [{RESET}{self.whenStarted}{GREEN}]{RESET}")
        print(f"{GREEN}Username:{RESET}  {self.username}")
        print(f"{GREEN}Password:{RESET}  {self.password}")
        print(f"{GREEN}SFTP listening on:{RESET}  {self.listenAddr}:{self.listenPort}")
        print(f"{GREEN}SFTP URI:{RESET}  sftp://{self.username}@{self.listenAddr}:{self.listenPort}")
        print(f"{GREEN}Server will terminate in:{RESET}  {self.timeoutMin}m")


def randomString(strLength:int = 36, upper:bool = True, lower:bool = True, number:bool = True, symbols:bool = True) -> str:
    upperSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if upper   else ""
    lowerSet = "abcdefghijklmnopqrstuvwxyz" if lower   else ""
    numberSet = "0123456789"                if number  else ""
    symbolSet = "!@#$%^&*()_+-={}[]:;.,?/"  if symbols else ""

    masterSet = upperSet + lowerSet + numberSet + symbolSet
    if not masterSet:
        raise ValueError("At least one character set must be enabled.")
    
    passwordLength = strLength
    passwordChars = []

    for _ in range(passwordLength):
        passwordChars.append(secrets.choice(masterSet))

    random.SystemRandom().shuffle(passwordChars)
    return ''.join(passwordChars)


def main() -> None:
    server = SFTPServer()
    server.display_connection_information()


if __name__=="__main__":
    main()
