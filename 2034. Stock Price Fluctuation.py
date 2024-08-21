class StockPrice:

    def __init__(self):
        self.dic=collections.defaultdict(int)
        self.latesttime = 0
        #use heap so search will be o(log(n)) and total time complexity will be o(nlogn). If we use array, it will be o(n^2)
        #We need 2 heaps, one for min pricem one for max price
        self.minpriceheap = [] 
        self.maxpriceheap = []
         
    def update(self, timestamp: int, price: int) -> None:
        self.dic[timestamp] = price
        self.latesttime = max(self.latesttime, timestamp)
        heappush(self.minpriceheap , (price ,timestamp))
        heappush(self.maxpriceheap , (-price ,timestamp))
        
    def current(self) -> int:
        return self.dic[self.latesttime]
        
    def maximum(self) -> int:
        price , time = self.maxpriceheap[0]
        while self.dic[time] != -price : 
            heappop(self.maxpriceheap)
            price , time = self.maxpriceheap[0]
        return -price
        

    def minimum(self) -> int:
        price , time = self.minpriceheap[0]
        while self.dic[time] !=price : 
            heappop(self.minpriceheap)
            price , time = self.minpriceheap[0]
        return price


        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
