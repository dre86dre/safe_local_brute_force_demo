# This file is a safe, local bruteforce tester that imports `check` from login_app.py and tries passwords from a wordlist.
# This file automates guessing using the check() function.
# This file is for learning only. Do NOT use it against other people's systems.


import time                     # Used to slow attempts (to simulate real-world delays)
from login_app import check     # We import check() function from your local file. No networking.

WORDLIST_FILE = 'wordlist.txt'   # File that contains guesses
DELAY_BETWEEN_TRIES = 0.05       # Seconds: small delay per attempt to avoid tight-loop stress
MAX_TRIES = None                 # Set to an int to limit attempts, or None for no artificial limit
VERBOSE = True                   # If set to True, it will print each attempt. Set False to reduce printed output

def try_wordlist(file_path: str):
# Reads passwords from `file_path` and trys them one by one against login_app.check().
    found = False       # Only becomes True if the password is found
    attempts = 0        # Counter for the number of tries
    try:
        with open(file_path, 'r', encoding='utf-8') as f:   # Reads each word from wordlist.txt
            for line in f:
                candidate = line.strip()    # Strips spaces/newlines
                if not candidate:
                    continue
                attempts += 1   # Increases attempt count

                if VERBOSE:
                    print(f"Trying ({attempts}): {candidate}") # Show progress if enabled

                if check(candidate):
                # Call the check() function from login_app.py
                    print('\n*** SUCCESS: password found ->', candidate, '***\n')
                    found = True    # If check() returns True (correct password), you get success
                    break           # Stop further attempts once found

                if MAX_TRIES is not None and attempts >= MAX_TRIES:
                # Respect optional limits and add a tiny delay to simulate realistic behaviour.
                    print('\nReached MAX_TRIES limit (stopping).\n')    # Stops if you set a limit
                    break
                time.sleep(DELAY_BETWEEN_TRIES) # Adds a delay to slow the loop (so it doesn't go too fast)

    except FileNotFoundError:
        print(f"Wordlist file not found: {file_path}")
    if not found:
        print('Password not found in wordlist.')
    print(f'Total attempts: {attempts}')
    # Tells you if it succeeded
    # Reports how many guesses there were

if __name__ == '__main__':
    print('*** SAFE LOCAL BRUTEFORCE DEMO (only tests the local login_app.check function) ***\n')
    print('Note: this is educational — do not use against systems you do not own.\n')
    try_wordlist(WORDLIST_FILE)
