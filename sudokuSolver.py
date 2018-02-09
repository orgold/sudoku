import csv
import sys


def main(args):
    with open(args[0]) as f:
        reader = csv.reader(f.readlines())
        board = [r for r in reader]
    print('{}'.format(board))


if __name__ == '__main__':
    main(sys.argv[1:])
