class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0]*len(pref)
        arr[0] = pref[0]
        curr_xor = pref[0]

        for i in range(1, len(pref)):
            arr[i] = curr_xor^pref[i]
            curr_xor ^= arr[i]

        return arr