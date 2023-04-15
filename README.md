# FCK-FCEBKNGA 
Facebook Brute Force Script

This is a Python script to demonstrate a brute force attack on a Facebook account using a wordlist. The script is for educational purposes only, and should be used to understand the security risks associated with weak passwords. Unauthorized access to someone's account is a violation of privacy and should not be attempted.
Prerequisites

    Python 3.x

Usage

    Clone the repository or copy the script to your local machine.

    Prepare a wordlist containing possible passwords (one password per line). Wordlists can be found online or generated using various tools.

    Run the script in a terminal:

    python3 fb_brute_force.py

    Follow the prompts to enter the Facebook username, email, or phone number, and the wordlist's path.

    The script will attempt to log in to the target account using each password in the wordlist. When a matching password is found, the script will display the result and exit.

Limitations

    The script relies on the wordlist's quality; if the target's password is not in the wordlist, the attack will fail.
    The target account may have additional security measures in place, such as two-factor authentication, which will prevent a successful login even if the correct password is found.
    Facebook may block repeated login attempts or flag them as suspicious, rendering this script ineffective.

Disclaimer

This script is for educational purposes only. Unauthorized access to someone's account is a violation of privacy and should not be attempted. The script's author and contributors are not responsible for any misuse of this script or any consequences resulting from its use.
