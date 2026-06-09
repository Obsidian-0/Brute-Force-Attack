# Brute Force Attack & Prevention Simulation

A Python-based security project demonstrating brute force attacks and prevention mechanisms using salted hashing, account lockout, and dictionary attacks.

---

## Project Overview

This project simulates both sides of a brute force attack scenario:
- **Defense Side:** Secure user registration and login system with salted SHA-256 hashing and account lockout
- **Offense Side:** Dictionary-based brute force attack using the rockyou.txt wordlist

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| SQLite | Lightweight database |
| hashlib (SHA-256) | Password hashing |
| os.urandom | Cryptographic salt generation |
| rockyou.txt | Real-world password wordlist |

---

## Project Structure

```
brute_force_project/
├── main.py          # Core application
├── header.py        # ASCII art intro
├── attack_log.txt   # Generated after attack
├── brute_force.db   # Generated on first run
└── rockyou.txt      # Wordlist (download separately)
```

---

## Setup & Installation

**1. Clone the repository:**
```bash
git clone https://github.com/yourusername/brute_force_project
cd brute_force_project
```

**2. Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

**3. Install dependencies:**
```bash
pip install pyinstaller
```

**4. Download rockyou.txt:**
```bash
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

**5. Run:**
```bash
python main.py
```

---

## Features

### User Panel
- **Register** — Create account with salted SHA-256 hashed password
- **Login** — Authenticate with automatic failed attempts tracking

### Admin/Demo Panel
- **Toggle Lockout Protection** — Enable/disable account lockout for demonstration
- **Launch Attack** — Dictionary attack on target user
- **Unlock User** — Reset locked accounts

---

## How It Works

### Password Storage
```
User enters password → Random salt generated (os.urandom)
                     → SHA-256(password + salt) computed
                     → username, salt, hash stored in SQLite
```

### Login Verification
```
User enters password → Salt fetched from database
                     → SHA-256(input + salt) computed
                     → Compared with stored hash
                     → 5 failed attempts → Account locked
```

### Brute Force Attack
```
Target username selected → Salt + Hash extracted from database
                        → rockyou.txt loaded
                        → Each word hashed with same salt
                        → Compared with stolen hash
                        → Match found → Password cracked
```

---

## Security Concepts Demonstrated

### Salted Hashing
Without salt — two users with same password have identical hashes, enabling rainbow table attacks.
With salt — each user has unique hash even with identical passwords, forcing per-user attacks.

### Account Lockout
After 5 failed login attempts, the account is locked — preventing automated brute force on the login interface.

### Lockout Toggle (Demo Feature)
- **Lockout ON** → Attack limited to 5 attempts
- **Lockout OFF** → Unlimited attempts, demonstrates full dictionary attack

### Weak vs Strong Password
- `pakistan123` → Found in rockyou.txt → Cracked in seconds
- `obsidian` → Not in rockyou.txt → Dictionary attack fails

---

## Attack Log Sample
```
Target: bilal, Password: pakistan123, Attempts: 1243, Time: 3.2 seconds
Target: ahmed, Password: NOT FOUND, Attempts: 14344391, Time: 847.3 seconds
```

---

## Disclaimer
This project is built for educational purposes only as part of an Information Security course. All attacks are performed in a controlled, simulated environment on self-created data.

---

## Author
**Bilal Rafiq**
BS Computer Science — 4th Semester
Information Security Project
