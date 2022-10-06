class Solution:
    def compress(self, chars: List[str]) -> int:
        length = 0
        curr = chars[0]
        counter = 0
        for i in range(len(chars)):
            if chars[i] == curr:
                counter += 1
            else:
                if counter == 1:
                    chars[length] = curr
                    length += 1
                else:
                    chars[length] = curr
                    length += 1
                    for j in str(counter):
                        chars[length] = j
                        length += 1
                curr = chars[i]
                counter = 1
        chars[length] = curr
        length += 1
        if counter != 1:
            for j in str(counter):
                chars[length] = j
                length += 1
        return length