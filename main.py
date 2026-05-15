import sqlite3
import os
import hashlib
def create_database():
    conn = sqlite3.connect('brute_force.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL Unique,
            salt TEXT NOT NULL,
            Password_hash TEXT NOT NULL,
            failed_attempts INTEGER DEFAULT 0,
            is_locked integer DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
def registration():
    user = input("Enter username: ")
    password = input("Enter password: ")
    salt = os.urandom(16)
    password_hash = hashlib.sha256(password.encode()+ salt).hexdigest()
    conn = sqlite3.connect('brute_force.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (username, salt, password_hash) VALUES (?, ?, ?)
        ''', (user, salt.hex(), password_hash))
        conn.commit()
        print(f"User {user} registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def login():
    user = input("Enter username: ")
    password = input("Enter password: ")
    conn = sqlite3.connect('brute_force.db')
    cursor = conn.cursor()
    cursor.execute('Select salt,password_hash,failed_attempts,is_locked from users where username = ? ',(user,))
    result = cursor.fetchone()
    if result is None:
        print("User no found.")
        conn.close()
        return
    salt, password_hash, failed_attempts, is_locked = result
    cursor.execute('SELECT value FROM settings WHERE setting_name = ?', ('lockout_enabled',))
    lockout_enabled = cursor.fetchone()[0]

    if lockout_enabled and is_locked:
        print("Account is locked due to too many failed login attempts.")
        conn.close()
        return
    salt_bytes = bytes.fromhex(salt)
    computed_hash = hashlib.sha256(password.encode()+ salt_bytes).hexdigest()
    if computed_hash == password_hash:
        print("Login Sexcessfull")
        cursor.execute('Update users set failed_attempts = 0 where username =?',(user,))
    else:
        failed_attempts +=1
        print(f"Wrong Password! Attempts : {failed_attempts}/5")
        cursor.execute('update users set failed_attempts =? where username = ?',(failed_attempts,user))
        if failed_attempts>=5:
            cursor.execute('Update users set is_locked =1 where username = ?',(user,))
            print('Account Locked!')
    conn.commit()
    conn.close()
def create_settings_table():
    conn = sqlite3.connect('brute_force.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            setting_name TEXT PRIMARY KEY,
            value INTEGER DEFAULT 1
        )
    ''')
    # Default: lockout enabled
    cursor.execute('INSERT OR IGNORE INTO settings (setting_name, value) VALUES (?, ?)', 
                   ('lockout_enabled', 1))
    conn.commit()
    conn.close()
def toggle_lockout():
    conn = sqlite3.connect('brute_force.db')
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM settings WHERE setting_name = ?', ('lockout_enabled',))
    current = cursor.fetchone()[0]
    new_value = 0 if current == 1 else 1
    cursor.execute('UPDATE settings SET value = ? WHERE setting_name = ?', 
                   (new_value, 'lockout_enabled'))
    conn.commit()
    conn.close()
    print(f"Lockout Protection: {'ON' if new_value == 1 else 'OFF'}")
if __name__ == "__main__":
    create_database()
    create_settings_table()
    # registration()
    login()     
        