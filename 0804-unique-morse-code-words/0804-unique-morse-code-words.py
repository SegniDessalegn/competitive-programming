class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        unique = set()
        for word in words:
            morse_code = ""
            for char in word:
                morse_code += code[ord(char) - 97]
            unique.add(morse_code)
        
        return len(unique)