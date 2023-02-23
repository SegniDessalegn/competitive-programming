class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        char_shifts = [0 for _ in range(len(s) + 1)]
        for shift in shifts:
            char_shifts[shift[0]] += 1 if shift[2] == 1 else -1
            char_shifts[shift[1] + 1] += -1 if shift[2] == 1 else 1
        
        char_shifts.pop()
        pref = [0]
        for n in char_shifts:
            pref.append(pref[-1] + n)
        
        shifted = []
        for i in range(len(s)):
            shifted.append(chr(((ord(s[i]) - 97 + pref[i + 1]) % 26) + 97))
        
        return "".join(shifted)