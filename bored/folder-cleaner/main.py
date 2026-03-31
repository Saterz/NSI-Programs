import os, sys

welcome = "Welcome to the folder cleaner program"
separator = "-"
RED = '\033[31m'
RESET = '\033[0m'

def len_separator(text: str) -> str:
    return len(text)*separator

def print_error(e: Exception, exit: bool = True) -> None:
    print("\n" + RED + "An unexpected error occured!")
    print(f"More info:\n{e}" + RESET)
    if exit:
        sys.exit()

if __name__ == "__main__":
    print(len_separator(welcome))
    print(welcome)
    print(len_separator(welcome))

    print(r"Please enter the absolute path of the folder you wish to clean (e.g., C:\Users\<user>\path\to\folder).")
    path = input()

    try:
        os.chdir(path)
    except Exception as e:
        print_error(e)
    
