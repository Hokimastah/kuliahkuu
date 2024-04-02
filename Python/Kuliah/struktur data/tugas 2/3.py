class Solution :
    def finalPrices(self, price: list[int]):
        for i,x in enumerate(price):
            for j in range((i+1),len(price)):
                if x >= price[j] :
                    price[i] = price[i] - price[j]
                    break
        return price