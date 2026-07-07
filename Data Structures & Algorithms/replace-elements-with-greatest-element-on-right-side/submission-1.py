class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        for i in range(len(arr)-1,-1,-1):
            current = arr[i]
            arr[i] = current_max
            current_max = max(current,arr[i])
        return arr

