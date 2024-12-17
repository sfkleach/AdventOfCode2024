from day17 import *
import argparse
from pathlib import Path


class ABCRegisterMachine:

    def __init__(self, program, A=0, B=0, C=0):
        self.A = A
        self.B = B
        self.C = C
        self.pc = 0
        self.program = tuple(program)
        self.output = []

    def run(self):
        '''Accumulate the virtual output in self.output'''
        while 0 <= self.pc < len(self.program):
            self.execute_instruction()
        return self.output

    def execute_instruction(self):
        '''Execute the instruction at the current program counter'''
        opcode = self.program[self.pc]
        operand = self.program[self.pc + 1]
        # print(f'Opcode: {opcode}, Operand: {operand}')
        # print(f'A: {self.A}, B: {self.B}, C: {self.C}, PC: {self.pc}')
        if opcode == 0:     # ADV = A shift right
            self.A >>= self.combo(operand)
        elif opcode == 1:   # BXL = B XOR literal operand
            self.B ^= operand
        elif opcode == 2:   # BST = B set to combo
            self.B = self.combo(operand) & 0x7
        elif opcode == 3:   # JNZ = jump if not zero
            if self.A:
                self.pc = operand
                return
        elif opcode == 4:   # BXC = B XOR C
            self.B ^= self.C
        elif opcode == 5:   # OUT
            self.output.append(self.combo(operand) & 0x7)
        elif opcode == 6:   # BDV = B shift right
            self.B >>= self.combo(operand)
        elif opcode == 7:   # CDV = C shift right
            self.B >>= self.combo(operand)
        else:
            raise ValueError(f'Invalid opcode: {opcode}')
        self.pc += 2
        
    def combo(self, operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        elif operand == 6:
            return self.C
        else:
            raise ValueError(f'Invalid combo operand: {operand}')

def run(args):
    ...

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
