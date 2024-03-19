from typing import List
from decoratorFunction import decorator_function


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m, n = len(nums1), len(nums2)
#         p1, p2 = 0, 0
        
#         # Get the smaller value between nums1[p1] and nums2[p2].
#         def get_min():
#             nonlocal p1, p2
#             if p1 < m and p2 < n:
#                 if nums1[p1] < nums2[p2]:
#                     ans = nums1[p1]
#                     p1 += 1
#                 else:
#                     ans = nums2[p2]
#                     p2 += 1
#             elif p2 == n:
#                 ans = nums1[p1]
#                 p1 += 1
#             else:
#                 ans = nums2[p2]
#                 p2 += 1
#             return ans
        
#         if (m + n) % 2 == 0:
#             for _ in range((m + n) // 2 - 1):
#                 _ = get_min()
#             return (get_min() + get_min()) / 2
#         else:
#             for _ in range((m + n) // 2):
#                 _ = get_min()
#             return get_min()
        

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        max_list, min_list = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)
        for x in min_list:
            i = 0
            d = len(max_list) - 1
            # while max_list[i] != x or max_list[i - 1] < x < max_list[i + 1]:
            # while x > max_list[0] or x < max_list[len(max_list) - 1] or max_list[i] != x or max_list[i - 1] < x < max_list[i + 1]:
            while 1:
                if x <= max_list[0]:
                    max_list.insert(0, x)
                    break

                elif x >= max_list[len(max_list) - 1]:
                    max_list.append(x)
                    break

                elif max_list[i] == x or max_list[i - 1] < x < max_list[i]:
                    max_list.insert(i, x)
                    break

                if x > max_list[i]:
                    if d > 1:
                        d //= 2
                    i = i + d
                elif x < max_list[i]:
                    if d > 1:
                        d //= 2
                    i = i - d
        if len(max_list) % 2 == 0:
            return (max_list[(len(max_list) - 1)//2] + max_list[len(max_list)//2]) / 2
        else:
            return max_list[len(max_list)//2]

    
if __name__ == "__main__":
    sol = Solution()
    l1 = [4, 11, 19, 110, 123, 140, 148, 151, 166, 171, 303, 309, 312, 324, 326, 334, 354, 357, 374, 376, 379, 424, 426, 462, 480, 523, 532, 533, 534, 732, 735, 736, 739, 759, 778, 791, 890, 908, 914, 941, 942, 952, 971, 978, 981, 987, 997]
    l2 = [75, 105, 150, 200, 487]

    run_fuc = decorator_function(sol.findMedianSortedArrays)

    print(run_fuc(l1, l2))