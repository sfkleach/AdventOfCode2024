from day05 import *
import argparse
from pathlib import Path

class Main:

    def __init__(self):
        # Create the argument parser
        parser = argparse.ArgumentParser(description='Process some options.')
        parser.add_argument('--input', type=Path, help='Input file path')
        parser.add_argument('--debug', action='store_true', help='Enable debug mode')

        # Parse the arguments
        self._args = parser.parse_args()

    def run(self):
        ...
    
if __name__ == '__main__':
    Main().run()
