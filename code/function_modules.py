def hello(name):
    print(f"Hi, {name}")

def Power(base, exp=2):
    return base ** exp

def Concatenate(*args):
    r = ""
    for a in args:
        r = r + a
    return r

