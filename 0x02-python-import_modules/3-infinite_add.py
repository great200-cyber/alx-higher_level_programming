#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__"
    """Print the adition of all arguments."""
=======
if __name__ == "__main__":
    """Print the addition of all arguments."""
>>>>>>> b654c02450ef75ed160d8688ae1558cfdf7ad7e8
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
