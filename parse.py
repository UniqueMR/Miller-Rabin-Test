import argparse

def parse():
    parser = argparse.ArgumentParser(
        prog='MillerRabin',
        description='Execute Miller Rabin Test',
        epilog='Text at the bottom of help'
    )
    parser.add_argument('-n','--number',default=7,type=int)
    parser.add_argument('-k','--times',default=5,type=int)
    args = parser.parse_args()
    return args