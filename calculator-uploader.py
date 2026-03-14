import os
import sys
from tivars import TIProgram


class CalculatorUploader:

    def __init__(self):
        self.repo_dir = os.path.dirname(os.path.abspath(__file__))
        self.programs = {}
        self.load_programs()

    def load_programs(self):
        """Load all PROG files from the repository"""

        for file in os.listdir(self.repo_dir):

            if file.startswith("PROG") and "." not in file:

                path = os.path.join(self.repo_dir, file)

                with open(path, "r") as f:
                    self.programs[file] = f.read()

    def list_programs(self):
        """List all available calculator programs"""

        print("\nAvailable Programs\n")

        if not self.programs:
            print("No programs found")
            return

        for name in sorted(self.programs.keys()):
            print(name)

        print()

    def view_program(self, prog_name):
        """Show program source"""

        if prog_name not in self.programs:
            print("Program not found")
            return

        print("\n" + prog_name)
        print("-" * 40)
        print(self.programs[prog_name])
        print()

    def convert_program(self, prog_name):
        """Convert a program to .8xp"""

        if prog_name not in self.programs:
            print("Program not found")
            return

        code = self.programs[prog_name]

        program = TIProgram()
        program.name = prog_name
        program.set_text(code)

        output_path = os.path.join(self.repo_dir, prog_name + ".8xp")

        program.save(output_path)

        print("Created:", prog_name + ".8xp")

    def convert_all(self):
        """Convert all programs"""

        if not self.programs:
            print("No programs to convert")
            return

        for prog in self.programs:
            self.convert_program(prog)

    def show_help(self):

        print("""
Calculator Uploader CLI

Commands

list
    Show all available programs

view PROG##
    View program source

convert PROG##
    Convert a program to .8xp

build
    Convert all programs to .8xp

help
    Show this help message

Examples

python calculator-uploader.py list
python calculator-uploader.py view PROG01
python calculator-uploader.py convert PROG01
python calculator-uploader.py build
""")


def main():

    uploader = CalculatorUploader()

    if len(sys.argv) < 2:
        uploader.show_help()
        return

    command = sys.argv[1].lower()

    if command == "list":
        uploader.list_programs()

    elif command == "view":

        if len(sys.argv) < 3:
            print("Specify program like PROG01")
            return

        uploader.view_program(sys.argv[2].upper())

    elif command == "convert":

        if len(sys.argv) < 3:
            print("Specify program like PROG01")
            return

        uploader.convert_program(sys.argv[2].upper())

    elif command == "build":
        uploader.convert_all()

    elif command == "help":
        uploader.show_help()

    else:
        print("Unknown command")
        uploader.show_help()


if __name__ == "__main__":
    main()