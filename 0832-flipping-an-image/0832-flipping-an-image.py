class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            curr = []
            for j in range(len(image[i]) - 1, -1, -1):
                if image[i][j] == 1:
                    curr.append(0)
                else:
                    curr.append(1)
            image[i] = curr
        return image