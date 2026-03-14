import os
import sys

class CalculatorUploader:
    def __init__(self):
        self.programs = []
        self.load_programs()

    def load_programs(self):
        # Placeholder for loading existing programs
        self.programs = ["program1.8xp", "program2.8xp", "program3.8xp"]

    def list_programs(self):
        print("Available Programs:")
        for i, program in enumerate(self.programs):
            print(f"{i + 1}. {program}")

    def view_program(self, index):
        if 0 <= index < len(self.programs):
            with open(self.programs[index], 'r') as f:
                print(f"\nContents of {self.programs[index]}:\n")
                print(f.read())
        else:
            print("Invalid program index.")

    def prepare_program(self, index):
        if 0 <= index < len(self.programs):
            print(f"Preparing {self.programs[index]} for upload...")
            # Placeholder for actual preparation logic
        else:
            print("Invalid program index.")

    def run(self):
        while True:
            self.list_programs()
            choice = input("Select a program to view (1-{len(self.programs)}) or 'q' to quit: ")
            if choice.lower() == 'q':
                break
            try:
                index = int(choice) - 1
                self.view_program(index)
                self.prepare_program(index)
            except ValueError:
                print("Please enter a valid number.")

if __name__ == '__main__':
    uploader = CalculatorUploader()
    uploader.run()