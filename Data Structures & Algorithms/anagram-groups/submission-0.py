class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} #key should be sorted string value is list of words
        for i in strs:
            key = "".join(sorted(i))
            if key in hashmap:
                hashmap[key].append(i)
            else:
                hashmap[key] = [i]
        return list(hashmap.values())

        