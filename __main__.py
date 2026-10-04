import os
import platform

def start(a):

    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

    import PCT
    if a=="menu":
        try:
            PCT.main()
        except KeyboardInterrupt:
            start("menu")
    elif a=="start":
        try:
            PCT.load()
        except KeyboardInterrupt:
            start("menu")
            
if __name__ == "__main__":
    start("start")
