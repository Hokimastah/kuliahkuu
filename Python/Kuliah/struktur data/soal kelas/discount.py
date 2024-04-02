class solution :
    def finalprices(self, price: list[int]):
        discount = price.copy()
        for i,x in enumerate(price):
            for j,y in enumerate(discount):
                if x >= y and i<j:
                    discount[i] = price[i] - price[j]
                    break
        print(discount)