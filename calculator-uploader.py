import os
import sys
from tivars import TIProgram

class CalculatorUploader:
    def __init__(self):
        self.repo_dir = os.path.dirname(os.path.abspath(__file__))
        self.src_dir = os.path.join(self.repo_dir, "src")
        self.build_dir = os.path.join(self.repo_dir, "build")

        # Create folders if missing
        os.makedirs(self.src_dir, exist_ok=True)
        os.makedirs(self.build_dir, exist_ok=True)

        self.programs = {}
        self.load_programs()

    def load_programs(self):
        """Load all program files from src/ (ignore .bak and .8xp)"""
        for file in os.listdir(self.src_dir):
            # Only process files starting with PROG
            if not file.startswith("PROG"):
                continue
            # Skip backup and compiled files
            if file.endswith(".bak") or file.endswith(".8xp"):
                continue

            path = os.path.join(self.src_dir, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.programs[file] = f.read()
            except Exception as e:
                print(f"Skipping {file}: {e}")

    def list_programs(self):
        if not self.programs:
            print("No programs found in src/")
            return
        print("\nAvailable Programs:")
        for name in sorted(self.programs):
            print(name)
        print()

    def view_program(self, prog_name):
        if prog_name not in self.programs:
            print(f"Program '{prog_name}' not found!")
            return
        print(f"\n=== {prog_name} ===")
        print("-" * 40)
        print(self.programs[prog_name])
        print("-" * 40 + "\n")

    def convert_program(self, prog_name):
        if prog_name not in self.programs:
            print(f"Program '{prog_name}' not found!")
            return

        code = self.programs[prog_name]

        # Convert text to TI program
        program = TIProgram.from_source(code)
        program.name = prog_name[:8]  # TI-84 program name limit

        output = os.path.join(self.build_dir, prog_name + ".8xp")
        program.save(output)

        print("Created:", output)

    def build_all(self):
        if not self.programs:
            print("No programs to build!")
            return
        for prog in self.programs:
            self.convert_program(prog)

    def show_help(self):
        print("""
Calculator Uploader CLI

Commands:

list
    List all available programs

view PROG##
    View the code of a program

convert PROG##
    Convert a single program to .8xp

build
    Convert all programs to .8xp

help
    Show this help message

Example:

python calculator-uploader.py build
""")

def main():
    uploader = CalculatorUploader()

    if len(sys.argv) < 2:
        uploader.show_help()
        return

    cmd = sys.argv[1].lower()

    if cmd == "list":
        uploader.list_programs()
    elif cmd == "view":
        if len(sys.argv) < 3:
            print("Specify program name (e.g., PROG01)")
            return
        uploader.view_program(sys.argv[2])
    elif cmd == "convert":
        if len(sys.argv) < 3:
            print("Specify program name (e.g., PROG01)")
            return
        uploader.convert_program(sys.argv[2])
    elif cmd == "build":
        uploader.build_all()
    elif cmd == "help":
        uploader.show_help()
    else:
        print(f"Unknown command '{cmd}'\n")
        uploader.show_help()

if __name__ == "__main__":
    main()