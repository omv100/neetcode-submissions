class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in range(len(strs)):
            #sort it for sure
            key = "".join(sorted(strs[i]))
            if key in hashmap:
                hashmap[key].append(strs[i])
            else:
                hashmap[key] = [strs[i]]
        return list(hashmap.values())
        