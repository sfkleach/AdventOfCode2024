from typing import Tuple


def translate_dirn(dirn: str) -> Tuple[int, int]:
    if dirn == '^':
        return -1, 0
    if dirn == 'v':
        return 1, 0
    if dirn == '<':
        return 0, -1
    if dirn == '>':
        return 0, 1
    raise ValueError('Invalid direction:', dirn)
