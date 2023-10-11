class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            if ":" in queryIP:
                return "Neither"
            for i in range(26):
                if chr(i + 97) in queryIP:
                    return "Neither"
            res = queryIP.split(".")
            if len(res) != 4:
                return "Neither"
            for segment in res:
                if len(segment) == 0 or len(segment) > 3 or (len(segment) != 1 and segment[0] == "0") or not(0 <= int(segment) <= 255):
                    return "Neither"
            return "IPv4"
        else:
            queryIP = queryIP.lower()
            for i in range(6, 26):
                if chr(i + 97) in queryIP:
                    return "Neither"
            res = queryIP.split(":")
            if len(res) != 8:
                return "Neither"
            for segment in res:
                if not(1 <= len(segment) <= 4):
                    return "Neither"
            return "IPv6"