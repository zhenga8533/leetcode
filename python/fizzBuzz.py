class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # Runtime: 42 ms (Beats 88.95%)
        # Memory: 17.4 MB (Beats 47.3%)
        
        arr = [str(i) for i in range (1, n + 1)]

        for i in range(1, n + 1):
            if i % 3 == 0:
                arr[i - 1] = "Fizz"
            if i % 5 == 0:
                if arr[i - 1] == "Fizz":
                    arr[i - 1] += "Buzz"
                else:
                    arr[i - 1] = "Buzz"
        
        return arr
