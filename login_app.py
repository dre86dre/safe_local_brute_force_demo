# This file is a minimal, local-only "login" checker.
# This file defines a CORRECT password and a check() function.
# Run it directly to test the CLI: `python login_app.py`
# DO NOT use this against any external system. Only on files/VMs you own.


CORRECT = "G0d$3cur3P@ss"  # change this to try different scenarios (keep it local!)
# This is the password your code is protecting.

def check(password: str) -> bool:
    return password == CORRECT
# If guessed password matches "CORRECT", return True.

if __name__ == '__main__':
    p = input('Enter password: ')
    if check(p):
        print('Access granted')
    else:
        print('Access denied')
# This makes the script runnable if you execute it directly(python login_app.py).