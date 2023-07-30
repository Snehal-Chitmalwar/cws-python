def totalMarks(physics, chemistry, english, sst, computer):
    t = physics+chemistry+english+sst+computer
    print(f"You scored {t}")

# named parameters
# totalMarks(physics=45, computer=90, chemistry=44, english=98, sst=30)

# default parameter
# required parameters are to be written at front


def add(a: int, b="", c=0):
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    add = a+b+c
    return add


y = add(30)
print(y)

# def add(parameter)-> return type


def add(a: int, c: int, b=0) -> int:
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    return a+b+c


add(50, 30, b=20,)
