import os
import sys
from tivars import TIProgram


class CalculatorUploader:

    def __init__(self):
        self.repo_dir = os.path.dirname(os.path.abspath(__file__))
        self.src_dir = os.path.join(self.repo_dir, "src")
        self.build_dir = os.path.join(self.repo_dir, "build")

        self.programs = {}

        os.makedirs(self.src_dir, exist_ok=True)
        os.makedirs(self.build_dir, exist_ok=True)

        self.load_programs()

    def load_programs(self):
        """Load program source files"""

        for file in os.listdir(self.src_dir):

            if not file.endswith(".txt"):
                continue

            prog_name = file.replace(".txt", "")

            path = os.path.join(self.src_dir, file)

            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.programs[prog_name] = f.read()
            except Exception as e:
                print(f"Skipping {file}: {e}")

    def list_programs(self):

        if not self.programs:
            print("No programs found in src/")
            return

        print("\nAvailable Programs:\n")

        for name in sorted(self.programs):
            print(name)

        print()

    def view_program(self, prog):

        if prog not in self.programs:
            print("Program not found")
            return

        print("\n" + prog)
        print("-" * 40)
        print(self.programs[prog])
        print()

    def convert_program(self, prog):

        if prog not in self.programs:
            print("Program not found")
            return

        code = self.programs[prog]

        program = TIProgram()
        program.name = prog[:8]  # TI program name limit
        program.set_text(code)

        output = os.path.join(self.build_dir, prog + ".8xp")

        program.save(output)

        print("Created:", output)

    def build_all(self):

        if not self.programs:
            print("No programs to build")
            return

        for prog in self.programs:
            self.convert_program(prog)

    def show_help(self):

        print("""
Calculator Uploader CLI

Commands

list
    List programs

view NAME
    View program source

convert NAME
    Convert one program

build
    Convert all programs

Example

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
            print("Specify program name")
            return

        uploader.view_program(sys.argv[2])

    elif cmd == "convert":

        if len(sys.argv) < 3:
            print("Specify program name")
            return

        uploader.convert_program(sys.argv[2])

    elif cmd == "build":
        uploader.build_all()

    else:
        uploader.show_help()


if __name__ == "__main__":
    main()