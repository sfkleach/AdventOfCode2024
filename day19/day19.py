from pathlib import Path

def read_input(file: Path) -> tuple[tuple[str], tuple[str]]:
    with open(file, 'r') as f:
        towels = tuple(next(f).rstrip().split(', '))
        next(f)
        targets = tuple(map(lambda x: x.strip(), f))
        return towels, targets