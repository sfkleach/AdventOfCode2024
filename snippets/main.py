import argparse

def run_main_process(args):
    ...

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=str, help='Input file path')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    # Parse the arguments
    args = parser.parse_args()

    # Run the main process.
    run_main_process(args)
    
if __name__ == '__main__':
    main()
