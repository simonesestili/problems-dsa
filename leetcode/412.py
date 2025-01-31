class Solution:
    def fizzBuzz(self, n):
        x = lambda i: 'FizzBuzz' if not i % 15 else 'Fizz' if not i % 3 else 'Buzz' if not i % 5 else str(i)
        return [x(i + 1) for i in range(n)]
