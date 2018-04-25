# Fibonacci.py
"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in
the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def fib(num):
    if num == 1:
        return [1]
    if num == 2:
        return [1, 1]
    else:
        x = 1
        p = 1
        l = [1, 1]
        for _ in range(2, num):
            t = p
            p = x
            x += t
            l.append(x)
        return l


a1 = fib(1)
a2 = fib(2)
a3 = fib(6)
a4 = fib(20)

print("Fib 1:", a1)
print("Fib 2:", a2)
print("Fib 6:", a3)
print("Fib 20:", a4)
