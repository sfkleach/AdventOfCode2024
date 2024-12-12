from pathlib import Path

def read_input(input_path: Path) -> tuple[int]:
    with open(input_path) as f:
        return tuple(map(int, f.read().split()))
    
def blink_stone(n: int):
    if n == 0:
        yield 1
    else:
        s = str(n)
        if (len(s) % 2) == 0:
            k = len(s) // 2
            yield int(s[:k])
            yield int(s[k:])
        else:
            yield 2024 * n
    
def blink_line(input_data: tuple[int]):
    for i in input_data:
        yield from blink_stone(i)

def blink_line_n(input_data: tuple[int], n: int):
    for n in range(n):
        # if n % 5 == 0:
        #     print(f'Iteration (n)')
        input_data = tuple(blink_line(input_data))
    return input_data