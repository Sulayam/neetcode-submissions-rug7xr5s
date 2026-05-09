class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:

        n = len(self.arr)

        if n % 2 != 0:
            return self.arr[n // 2]

        else:
            index1 = (n // 2) - 1
            index2 = (n // 2)

            return (self.arr[index1] + self.arr[index2]) / 2