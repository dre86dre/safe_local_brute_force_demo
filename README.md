# Safe Local Brute Force Demo

This repository demonstrates how a basic brute-force and dictionary attack wokrs in a completely safe and offline environment. It is intended for learning and cybersecurity awareness.

Do NOT use this code on systems you do not own or without explicit permission.
This project is designed for local ethical experiments only.

---

## How It Works

- `login_app.py` contains a simple passsword check function (`check()`).
- `bruteforce.py` imports the `check()` function and tries multiple passwords from a wordlist (`wordlist.txt`).
- The test runs **locally only** - no network communication or external access.
- This simulates how attackers use brute-force/dictionary attacks.
- Includes safety features like delay and optional max attempts.

---

## Usage

1. Clone the repo

```
git clone https://github.com/dre86dre/safe_local_brute_force_demo.git
cd safe_local_brute_force_demo
```

2. Create a virtual environment (Optional)

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. Run the brute force tester

```
python bruteforce.py
```
