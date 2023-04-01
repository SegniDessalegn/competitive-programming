class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        for char in address:
            if char != ".":
                defanged += char
            else:
                defanged += "[.]"
        
        return defanged