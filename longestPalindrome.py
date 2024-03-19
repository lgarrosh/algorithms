from decoratorFunction import ExecutionTime

class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_palindrome = 0
        result = s[0]
        len_s = len(s)
        for i in range(len_s):
            j = i
            x = 0
            while j != len_s - 1 and s[i] == s[j + 1]:
                j += 1
            while i - x != 0 and j + x != len_s - 1 and s[i - x - 1] == s[j + x + 1]:
                x += 1
            if j - i + x + x > len_palindrome:
                len_palindrome = j - i + x + x
                result = s[i - x : j + x + 1]
            if j + x == len_s - 1:
                break
        return result
    

    def longestPalindrome2(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]

        return ""
    

if __name__ == "__main__":
    sol = Solution()
    time = ExecutionTime()
    str = "sfhkjlskjslyekjgwkrwlkvn,nval;ksjhfsdkbbskfbksjhfkhdkjfjh2974h4hhkj2brkjnbkfnsldhljflksnfsdjbfksjnflsn,fn"
    x, y = 3, 7

    # print(max(x, y))
    # print(str.index('d'))
    # print(str.index('a'))

    # print(sol.longestPalindrome(str))

    time.find_best_time(sol.longestPalindrome, sol.longestPalindrome2, str)
    # run_my = decorator_function(sol.longestPalindrome)
    # run_alien = decorator_function(sol.longestPalindrome2)

    # my_time = run_my(str)
    # alien_time = run_alien(str)
    # print("my function - ", my_time)
    # print("alien function - ", alien_time)
    # print("ween - ", "my" if my_time < alien_time else "alien")