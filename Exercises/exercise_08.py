"""
Exercise 8


1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float

2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 exercise_08.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 exercise_08.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument

"""
import sys
import argparse
def compute(**kwargs):
    data = kwargs.get('input', False)
    if not all(isinstance(i, int) for i in data):
        return False
    if kwargs.get('return_float', False):
        data = float(data)
    if kwargs.get('action', False) is 'sum':
        ret = sum(data)
    elif kwargs.get('action', False) is 'mean':
        ret = sum(data)/len(data)
    else:
        return False

    return ret
    quitter = 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='computes a sum or multiplies depending on given arguments')
    parser.add_argument('-m', '--multiply', help='print the remainder values multiplied by -m value', type=int)
    parser.add_argument('-s', '--sum', help='print the sum of the arguments', action='store_true')
    parser.add_argument('remainder', help='arguments to be summed or multiplied by', nargs=argparse.REMAINDER)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)
    if args.multiply:
        print([args.multiply * int(value) for value in args.remainder])
    elif args.sum:
        print(sum(map(int, args.remainder)))
    else:
        parser.print_help()
        sys.exit(1)
