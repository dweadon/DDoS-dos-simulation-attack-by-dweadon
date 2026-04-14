import os
import time
import sys
import random
import webbrowser
import subprocess


def clear_screen():
    os.system('cls')


def print_banner():
    banner = r"""
    ██████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
    ██║  ██║██║  ██║██║   ██║███████╗
    ██║  ██║██║  ██║██║   ██║╚════██║
    ██████╔╝██████╔╝╚██████╔╝███████║
    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝

          DDoS Visual Simulator v1.4
    """
    print(banner)


def loading_animation(text, duration=2):
    spinner = ['|', '/', '-', '\\']
    for _ in range(int(duration * 10)):
        sys.stdout.write(f'\r{text} {spinner[_ % 4]}')
        sys.stdout.flush()
        time.sleep(0.1)
    print()


def ddos_visual_attack(target="example.com", packets=10000, duration=12):
    print(f"\n[+] Targeting: {target}")
    print(f"[+] Flooding with {packets:,} packets...\n")

    start_time = time.time()
    sent = 0
    bar_width = 60

    while time.time() - start_time < duration:
        batch = random.randint(300, 800)
        sent += batch
        progress = min(int((sent / packets) * bar_width), bar_width)
        percent = min(int((sent / packets) * 100), 100)

        bar = '█' * progress + '░' * (bar_width - progress)
        flood = " ".join([f"[{random.randint(10000, 99999)}]" for _ in range(5)])

        sys.stdout.write(f"\r[{bar}] {percent:3}% | Sent: {sent:,} | {flood}")
        sys.stdout.flush()

        if random.random() < 0.25:
            print(f"\n[!] Flooding {target} → Burst {random.randint(100, 999)}")

        time.sleep(0.13)

    print(f"\n\n[✔] Simulation completed!")
    print(f"    Packets sent: {sent:,}")
    print(f"    Target status: Overwhelmed (simulation) \n")


def main():
    clear_screen()
    print_banner()

    print("⚠")

    target = input("Enter target (default: example.com): ").strip() or "example.com"

    try:
        packets = int(input("Number of packets (default 10000): ") or 10000)
    except ValueError:
        packets = 10000

    print("\n[+] Launching attack threads...")
    loading_animation("Spawning botnet...", 2.5)

    ddos_visual_attack(target, packets)

    loading_animation("Cleaning traces...", 2)

    print("\n" + "=" * 70)
    print("   ")
    print("=" * 70 + "\n")

    print("")
    time.sleep(1)
    funny_link = "https://www.youtube.com/watch?v=z-3Cnrqe_uA"

    try:
        webbrowser.open(funny_link, new=2)
    except:
        input("\nPress Enter to close this window...")


# ====================== AUTO OPEN NEW CMD (Fixed & Simple) ======================
if __name__ == "__main__":
    if os.name == 'nt':
        if "LAUNCHED_DDOS_VISUAL" not in os.environ:
            print("O")
            time.sleep(1)

            python_exe = sys.executable.replace("python.exe", "pythonw.exe")  # avoid console flash
            script_path = os.path.abspath(sys.argv[0])

            # Much cleaner command
            command = f'set LAUNCHED_DDOS_VISUAL=1 && "{sys.executable}" "{script_path}"'

            try:
                # This is the most reliable way on Windows
                subprocess.Popen(f'start "DDoS Visual Simulator" cmd /k "{command}"', shell=True)
            except Exception as e:

                main()

            sys.exit(0)
        else:
            # Running inside the new CMD window
            main()
    else:
        main()