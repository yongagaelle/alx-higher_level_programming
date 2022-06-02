#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc - 1))

    for i, argument in enumerate(argv):
        if i > 0:
            print("{}: {}".format(i, argument))
