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

**1. Clone the repo**

```
git clone https://github.com/coder0name0dre/safe_local_brute_force_demo.git
cd safe_local_brute_force_demo
```

**2. Create a virtual environment (optional)**

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

**3. Run the brute force tester**

```
python bruteforce.py
```

**4. Test password manually (optional)**

```
python login_app.py
```

---

## Customisation & Experiments

| Experiment               | How to do it                                   | What it shows                 |
| ------------------------ | ---------------------------------------------- | ----------------------------- |
| Instant success          | Move correct password to top of `wordlist.txt` | Fast dictionary attack        |
| Harder brute-force       | Change `CORRECT` value in `login_app.py`       | Strong password effects       |
| Add lockout              | Set `MAX_TRIES = 3` in `bruteforce.py`         | Account protection            |
| Remove delay             | Set `DELAY_BETWEEN_TRIES = 0`                  | Speed of uncontrolled attacks |
| Use long random password | `CORRECT="hG38&ks91!b"`                        | Brute-force impracticality    |

---

## Code Safety Features

- Fully offline
- No networking
- Local function testing only
- Delay between attempts
- Configurable attempt limit
- Clear warning in code and README

---

## Learning Outcomes

By using this project, you will learn:
- How brute-force and dictionary attacks work
- Importance of strong passwords
- Role of delay, lockout, and security mechanisms
- Why authentication systems should **never** store plain-text passwords
- How to perform ethical cybersecurity testing

---

## Legal Disclaimer

**You must NOT use this code to attack real systems, accounts, devices, websites, or networks. Doing so is illegal and unethical. Use only in controlled environments you own.**

---

## Contributing

Contributions, imporovements, and educational extensions are welcome! Just ensure all additions remain **ethical and safe.**

---

## License

This project is licensed under the [MIT License](https://github.com/coder0name0dre/safe_local_brute_force_demo/blob/main/LICENSE).
