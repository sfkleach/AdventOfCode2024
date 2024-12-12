from pathlib import Path

def read_input(input_path: Path) -> list[str]:
    with input_path.open() as f:
        return f.read().splitlines()