class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dist = set()
        for email in emails:
            local_name = ""
            i = 0
            while i < len(email):
                if email[i] == "@":
                    dist.add(local_name + email[i:])
                    break
                if email[i] != ".":
                    if email[i] == "+":
                        dist.add(local_name + email[email.find("@"):])
                        break
                    local_name += email[i]
                i += 1
        return len(dist)