import os
import sys

class CalculatorUploader:
    def __init__(self):
        self.repo_dir = os.path.dirname(os.path.abspath(__file__))
        self.programs = {}
        self.load_programs()

    def load_programs(self):
        """Load all PROG files from the repository"""
        for i in range(1, 5):
            prog_name = f"PROG{i:02d}"
            prog_path = os.path.join(self.repo_dir, prog_name)
            if os.path.exists(prog_path):
                with open(prog_path, 'r') as f:
                    self.programs[prog_name] = f.read()

    def list_programs(self):
        """List all available calculator programs"""
        print("\n=== Available Calculator Programs ===\n")
        if not self.programs:
            print("No programs found!")
            return
        
        for i, prog in enumerate(sorted(self.programs.keys()), 1):
            print(f"{i}. {prog}")
        print()

    def view_program(self, prog_name):
        """Display the code for a specific program"""
        if prog_name not in self.programs:
            print(f"Program '{prog_name}' not found!")
            return
        
        print(f"\n=== {prog_name} Code ===\n")
        print(self.programs[prog_name])
        print()

    def prepare_program(self, prog_name):
        """Prepare program for copying to TI Connect CE"""
        if prog_name not in self.programs:
            print(f"Program '{prog_name}' not found!")
            return
        
        code = self.programs[prog_name]
        print(f"\n=== Ready to Copy for TI Connect CE ===\n")
        print("Copy the code below and paste into TI Connect CE:\n")
        print("-" * 60)
        print(code)
        print("-" * 60)
        print("\nSteps:")
        print("1. Copy the code above (Ctrl+A then Ctrl+C)")
        print("2. Open TI Connect CE")
        print("3. Create a new program or paste into existing program")
        print("4. Connect your TI-84 and transfer to calculator")
        print()

    def show_help(self):
        """Display help information"""
        print("""
=== Calculator Uploader CLI ===

Usage: python calculator-uploader.py [command] [program]

Commands:
  list              - Show all available programs
  view [PROG##]     - View a specific program (e.g., view PROG01)
  prepare [PROG##]  - Prepare program for TI Connect CE upload
  help              - Show this help message

Examples:
  python calculator-uploader.py list
  python calculator-uploader.py view PROG01
  python calculator-uploader.py prepare PROG02
        """)

def main():
    uploader = CalculatorUploader()
    
    if len(sys.argv) < 2:
        uploader.show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'list':
        uploader.list_programs()
    elif command == 'view':
        if len(sys.argv) < 3:
            print("Error: Please specify a program (e.g., view PROG01)")
            return
        prog_name = sys.argv[2].upper()
        uploader.view_program(prog_name)
    elif command == 'prepare':
        if len(sys.argv) < 3:
            print("Error: Please specify a program (e.g., prepare PROG01)")
            return
        prog_name = sys.argv[2].upper()
        uploader.prepare_program(prog_name)
    elif command == 'help':
        uploader.show_help()
    else:
        print(f"Unknown command: {command}")
        print("Type 'python calculator-uploader.py help' for usage information")

if __name__ == '__main__':
    main()