#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    t = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            t += int(arg)

    print(t)
