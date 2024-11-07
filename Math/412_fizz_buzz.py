class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numbs = []

        for n in range(1, n+1):
            if (n % 3 == 0) and (n % 5 == 0):
                numbs.append("FizzBuzz")
            elif (n % 3 == 0):
                numbs.append("Fizz")
            elif (n % 5 == 0):
                numbs.append("Buzz")
            else:
                numbs.append(str(n))
        return numbs
