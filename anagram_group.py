import collections

def anagram_grp(nums):
    ans = collections.defaultdict(list)
    for s in nums:
        ans[tuple(sorted(s))].append(s)
    return ans.values()

print(anagram_grp(['ate','eat','bat','ea']))
