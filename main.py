from MillerRabin import MillerRabin
from parse import parse

if __name__ == "__main__":
    args = parse()
    test = MillerRabin(n=args.number,k=args.times)
    res = test.function()
    print(res)
    print("test finished!")