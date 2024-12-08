from typing import Generator
from pathlib import Path

class Calculate:

    def __init__(self, operators):
        self.operators = operators

    def calculate(self, running_value, values):
        if values:
            next_value = values[0]
            remaining = values[1:]
            for operator in self.operators:
                yield from self.calculate(operator(running_value, next_value), remaining)
        else:
            yield running_value


def concat(a: int, b: int) -> int:
    return int(f'{a}{b}')

CALCULATE1 = Calculate([lambda a, b: a + b, lambda a, b: a * b])
CALCULATE2 = Calculate([concat, lambda a, b: a + b, lambda a, b: a * b])

def calculate1(running_value, values):
    return CALCULATE1.calculate(running_value, values)

def calculate2(running_value, values):
    return CALCULATE2.calculate(running_value, values)

class Equation:

    def __init__(self, target, values):
        self.target = target
        self.values = values

    def __str__(self):
        return f'{self.target} -> {self.values}'
    
    def __repr__(self):
        return str(self)
    
    def has_solution1(self):
        return any(x == self.target for x in calculate1(self.values[0], self.values[1:]))
    
    def has_solution2(self):
        return any(x == self.target for x in calculate2(self.values[0], self.values[1:]))
    

def parseInput(input: Path) -> Generator[Equation, None, None]:
    with input.open() as file:
        for line in file:
            lhs, rhs = line.split(':')
            target = int(lhs.strip())
            values = tuple(int(x) for x in rhs.split())
            yield Equation(target, values)

def readEquations(input: Path) -> tuple[Equation]:
    return tuple(parseInput(input))
