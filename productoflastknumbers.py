class ProductOfNumbers:
    numList=[]
    lastzero=None
    def __init__(self):
        self.numList.clear()

    def add(self, num):
        self.numList.append(num) 

    def getProduct(self, k):
        p=1
        for i in range(-1, (k*-1)-1, -1):
            p*=self.numList[i]
        return p
        
productOfNumbers =  ProductOfNumbers()
productOfNumbers.add(3)       
productOfNumbers.add(0)       
productOfNumbers.add(2)       
productOfNumbers.add(5)     
productOfNumbers.add(4)    
productOfNumbers.getProduct(2)
productOfNumbers.getProduct(3)
productOfNumbers.getProduct(4)
productOfNumbers.add(8)     
productOfNumbers.getProduct(2)

