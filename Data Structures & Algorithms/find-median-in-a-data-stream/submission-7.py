class MedianFinder:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        

    def findMedian(self) -> float:
        if len(self.arr)%2!=0:
            val=(((len(self.arr)//2)))
            print(f"val -> {val}")
            print(f"median -> {self.arr[val]}")
            return self.arr[val]
        else:
            index1=((len(self.arr)//2))
            print(f"index1: {index1}")
            index2=((len(self.arr)//2)-1)
            print(f"index2: {index2}")
            return (self.arr[index1]+ self.arr[index2])/2
