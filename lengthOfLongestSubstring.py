from decoratorFunction import decorator_function

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_length_temp = 0
        substring_length = 0
        substring = []
        for i in range(len(s)):
            j = i
            while j < len(s) and (s[j] not in substring):
                substring.append(s[j])
                substring_length_temp += 1
                j+=1
            if substring_length < substring_length_temp:
                substring_length = substring_length_temp
            substring_length_temp = 0
            substring = []
        return substring_length


if __name__ == "__main__":
    sol = Solution()
    str = "d2d3d44dsdfgb4kfyyy12 3"

    run_fuc = decorator_function(sol.lengthOfLongestSubstring)

    print(run_fuc(str))
