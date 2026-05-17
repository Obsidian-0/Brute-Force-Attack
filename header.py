import time
import os
import sys

# ─── ANSI CODES ───────────────────────────────────────────────
GREEN       = "\033[92m"
DARK_GREEN  = "\033[32m"
DIM_GREEN   = "\033[2;32m"
BOLD        = "\033[1m"
DIM         = "\033[2m"
RESET       = "\033[0m"
CLEAR_LINE  = "\r\033[K"


def clear():
    import subprocess
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def type_print(text, color=GREEN, delay=0.03):
    """Print text character by character like typing effect."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def print_header():
    clear()

    ascii_art = f"""
{GREEN}{BOLD}
██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
{RESET}"""

    print(ascii_art)

    divider = DARK_GREEN + "═" * 88 + RESET
    print(divider)

    # Centered subtitle lines
    print(f"{DIM_GREEN}{'[ INFORMATION SECURITY PROJECT ]':^88}{RESET}")
    print(f"{DIM_GREEN}{'// trying every key until the door opens //':^88}{RESET}")

    print(divider)
    print()


def boot_sequence():
    """Animated boot lines before the header appears."""
    lines = [
        "[root@brute ~]$ ./launch --project brute_force --mode attack",
        "[root@brute ~]$ loading modules.................. OK",
        "[root@brute ~]$ initializing attack engine....... OK",
        "[root@brute ~]$ access granted. welcome.",
    ]

    for line in lines:
        type_print(line, color=GREEN, delay=0.025)
        time.sleep(0.15)

    time.sleep(0.4)
    clear()
    print_header()

    # Status bar after header
    status = (
        f"{DIM_GREEN}  [●] STATUS: ACTIVE"
        f"{'MODULE: PASSWORD CRACKING':^50}"
        f"ATTEMPTS: ∞  {RESET}"
    )
    print(status)
    print()

    # Blinking prompt simulation
    for _ in range(3):
        sys.stdout.write(f"{GREEN}[root@brute ~]$ {RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(CLEAR_LINE)
        time.sleep(0.3)

    print(f"{GREEN}[root@brute ~]$ {DIM_GREEN}starting brute force...{RESET}")
    print()
    time.sleep(0.5)


# ─── USAGE ────────────────────────────────────────────────────
# Just call show_intro() at the top of your main.py
def show_intro():
    boot_sequence()
