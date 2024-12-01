# Common code will go here.

def parse_input(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Convert the lines to integers
    numbers = [line.split() for line in lines]
    L1 = sorted([int(x[0]) for x in numbers])
    L2 = sorted([int(x[1]) for x in numbers])

    return (L1, L2)