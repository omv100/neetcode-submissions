class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        #makes the frequencies in the hashmap
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
            #now I can sort them?
        pairs = [[]]
        for i in frequency:
            pairs.append([frequency[i], i])

        # Sort from highest to lowest frequency
        pairs.sort(reverse=True)

        # Get the top k numbers
        result = []
        for i in range(k):
            result.append(pairs[i][1])

        return result
            
        #somehow print the list of k numbers
            
        