from pathlib import Path

def read_input(file: Path) -> tuple[tuple[str], tuple[str]]:
    with open(file, 'r') as f:
        towels = tuple(next(f).rstrip().split(', '))
        next(f)
        targets = tuple(map(lambda x: x.strip(), f))
        return towels, targets
    
def iter_len(iterable):
    n = 0
    for match in iterable:
        print("Match found:") 
        for i, group in enumerate(match.groups(), start=1): 
            print(f" Group {i}: {group}")
            n += 1
    return n