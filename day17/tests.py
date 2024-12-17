from part1 import ABCRegisterMachine

def test1():
    abc = ABCRegisterMachine([2, 6], C=9)
    abc.run()
    assert(abc.B == 1)

def test2():
    #If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
    abc = ABCRegisterMachine([5, 0, 5, 1, 5, 4], A=10)
    output = abc.run()
    assert(output == [0, 1, 2])

def test3():
    # If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
    abc = ABCRegisterMachine([0, 1, 5, 4, 3, 0], A=2024)
    out = abc.run()
    print(out)
    assert(out == [4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0])
    assert(abc.A == 0)

def test4():
    # If register B contains 29, the program 1,7 would set register B to 26.
    abc = ABCRegisterMachine([1, 7], B=29)
    abc.run()
    assert(abc.B == 26)

def test5():
    # If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354
    abc = ABCRegisterMachine([4, 0], B=2024, C=43690)
    abc.run()
    assert(abc.B == 44354)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()