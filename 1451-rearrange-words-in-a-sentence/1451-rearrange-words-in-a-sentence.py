class Solution:
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.lower().split(" "), key = lambda X: len(X))).capitalize()