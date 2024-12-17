
# 2,4     BST 4: B = A & 0b111
# 1,5,    BXL 1: B = B ^ 0b101
# 7,5,    CDV 5: C = A >> B
# 0,3,    ADV 3: A = A >> 3
# 4,0,    BXC:   B = B ^ C
# 1,6     BXL 6: B = B ^ 0b110 
# 5,5     OUT 5: OUT B 
# 3,0     JNZ 0: LOOP UNLESS A == 0

from collections import deque


def block(a, b, c):
    b = a & 0b111
    b = b ^ 0b101
    c = a >> b
    a = a >> 3
    b = b ^ c
    b = b ^ 0b110
    return a, b

# 2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0

program = ( 2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0 )   
rprogram = program[::-1]

class TimeReversal:

    def __init__(self, output):
        self.sofar = [0]
        self.output = output
        self.N = 0

    def execute(self):
        new_sofar = []
        self.N += 1
        target = self.output[-self.N]
        for A in self.sofar:
            for i in range(0, 8):
                prevA = (A << 3) | i
                currA, currB = block(prevA, 0, 0)
                currB = currB & 0b111
                print(f'i = {i}, A = {A}, B = {currB}, target = {target}')
                if currA == A and currB == target:
                    new_sofar.append(prevA)
        self.sofar = new_sofar          

TR = TimeReversal(program)
for n in range(0, len(program)):
    TR.execute()
    print(TR.sofar)
print(min(TR.sofar))
    





# print('Round 1')

# for i in range(0, 8):
#     print(block(i, 0, 0))

# print()

# print('Round 2')

# for i in range(0, 8):
#     a = (3 << 3) | i
#     b = 0
#     c = 0
#     print('A =', a)
#     output = deque([])
#     for _ in range(0,2):
#         _, (a, b, c) = block(a, b, c)
#         output.append(b & 0b111)
#         print('x', (a, b, c))
#     print(i, (a, b, c))
#     print(output)

# print()

# print('Round 3')
# sofar = [24, 25, 29, 31]
# for x in sofar:
#     for i in range(0, 8):
#         a = (x << 3) | i
#         b = 0
#         c = 0
#         print('A =', a)
#         output = deque([])
#         for _ in range(0,3):
#             _, (a, b, c) = block(a, b, c)
#             output.append(b & 0b111)
#             print('x', (a, b, c))
#         print(i, (a, b, c))
#         print(output)

# print()
