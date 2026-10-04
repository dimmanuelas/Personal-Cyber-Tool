import os

def start(a):
    os.system('cls')
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
