import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для Windows
init(autoreset=True)

def print_directory_structure(path: Path, indent: str = ""):
    if not path.exists():
        print(Fore.RED + "❌ Зазначений шлях не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + "❌ Це не директорія.")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + f"📂 {item.name}")
            print_directory_structure(item, indent + "  ")
        else:
            print(indent + Fore.GREEN + f"📜 {item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❗ Використання: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    print_directory_structure(directory_path)

