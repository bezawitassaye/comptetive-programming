class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        column = len(image[0])
        for i in range(row):
            image[i].reverse()
            for j in range(column):
                image[i][j]=1-image[i][j]
        return image    
        