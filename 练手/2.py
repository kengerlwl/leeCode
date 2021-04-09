class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        layer = min([xPos, num - xPos - 1, yPos, num - yPos - 1])  # 位于第几圈
        v = (num*layer*4 - layer*layer*4) % 9  # 前几圈有多少个元素

        start, end = layer, num - layer

        if xPos == start:
            return (v + yPos - start) % 9 + 1

        if yPos == end - 1:
            return (v + end - start - 1 + xPos - start) % 9 + 1

        if xPos == end - 1:
            return (v + (end - start)*2 - 2 + end - yPos - 1) % 9 + 1

        if yPos == start:
            return (v + (end - start)*3 - 3 + end - xPos - 1) % 9 + 1

        return 0

