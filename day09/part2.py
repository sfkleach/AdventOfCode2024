from day09 import *
import argparse
from pathlib import Path
from typing import Generator


class Disk:

    def __init__(self, free_list: dict[int, int], used_list: dict[int, tuple[int, int]]):
        self.free_list = free_list
        self.used_list = used_list

    def try_move_id(self, id):
        (used_start, used_count) = self.used_list[id]
        for free_start in sorted(self.free_list.keys()):
            if free_start > used_start:
                # Free store to the right will not do.
                print('Cannot move id', id, 'to', free_start)
                break
            free_count = self.free_list[free_start]
            if free_count >= used_count:
                print(f'Can move {id}: moving {used_count} blocks to {free_start} from {used_start}')
                self.used_list[id] = (free_start, used_count)
                del self.free_list[free_start]
                if free_count > used_count:
                    self.free_list[free_start + used_count] = free_count - used_count                    
                break
        print('Failed to move id', id)

    def rearrange(self):
        for id in reversed(range(self.max_id() + 1)):
            self.try_move_id(id)

    def max_id(self) -> int:
        return max(self.used_list.keys())

    def factors(self) -> Generator[int, None, None]:
        for id, (start, count) in self.used_list.items():
            for n in range(start, start + count):
                yield (n, id)

    def sum(self) -> int:
        return sum(n* id for n, id in self.factors())


def parseInput(inputPath: Path) -> list[int|None]:
    with open(inputPath, 'r') as file:
        text = file.read().strip()
    free_list = {}
    used_list = {}
    posn = 0
    for n, ch in enumerate(text):
        id = n // 2
        count = int(ch)
        is_free = (n % 2) == 1
        if is_free:
            free_list[posn] = count
        else:
            used_list[id] = (posn, count)
        posn += count
    return free_list, used_list


def run(args):
    d = Disk(*parseInput(args.input))
    d.rearrange()
    print(d.sum())

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Process some options.')
    parser.add_argument('--input', type=Path, help='Input file path')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')

    # Parse the arguments
    args = parser.parse_args()

    run(args)
    
if __name__ == '__main__':
    main()

