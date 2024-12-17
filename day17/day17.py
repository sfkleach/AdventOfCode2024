import re
from pathlib import Path


class ABCRegisterMachine:

    def __init__(self, program, A=0, B=0, C=0):
        self.A = A
        self.B = B
        self.C = C
        self.pc = 0
        self.program = tuple(program)
        self.output = []

    def clone(self):
        '''Return a copy of this machine but with the output reset'''
        return ABCRegisterMachine(self.program, A=self.A, B=self.B, C=self.C)

    def run_carefully(self):
        # print(f'Running with A={self.A}')
        while 0 <= self.pc < len(self.program):
            self.execute_instruction()
            if self.output and self.output[-1] != self.program[len(self.output) - 1]:
                # print(f'Output mismatch: {self.output} vs {self.program}')
                return False
        # print(f"Output : {self.output} vs {self.program}, {self.pc}" )
        return len(self.program) == len(self.output) and tuple(self.output) == self.program

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
        # print(f'pc: {self.pc}, program: {self.program}')
        # print(f'A: {self.A}, B: {self.B}, C: {self.C}, PC: {self.pc}, Output: {self.output}')
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
            self.B = self.A >> self.combo(operand)
        elif opcode == 7:   # CDV = C shift right
            self.C = self.A >> self.combo(operand)
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

def read_input(file_path: Path) -> ABCRegisterMachine:
    with open(file_path) as file:
        text = file.read()
        text = re.sub(r'[^-\d]', ' ', text).split()
        numbers = [int(x) for x in text]
        A = numbers[0]
        B = numbers[1]
        C = numbers[2]
        program = numbers[3:]
    return ABCRegisterMachine(program, A=A, B=B, C=C)
