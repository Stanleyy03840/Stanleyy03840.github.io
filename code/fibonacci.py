def fib(n):
    if n <= 0:
        return [0]
    seq = [0,1]
    while len(seq) < n:
        yeah = len(seq)
        new = seq[yeah - 1] + seq[yeah - 2]
        seq.append(new)
    return seq


def tester():
    n = int(input("Enter a number for Fibonacci Sequence: "))
    # check if the number is negative
    if n < 0:
        print("Please enter a positive integer")
    else:
        print("The first", n, "terms of the Fibonacci Sequence is", fib(n))

if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    tester()