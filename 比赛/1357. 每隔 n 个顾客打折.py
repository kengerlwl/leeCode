class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        self.products = products
        self.f ={}
        for i in range(len(self.products)):
            self.f[self.products[i]] = i
        self.prices = prices
        self.cnt = 1

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        ans = 0
        for i in range(len(amount)):
            ans += self.prices[self.f[product[i]]] * amount[i]
        print(self.cnt)
        if self.cnt % self.n == 0:
            ans *= (1 - self.discount / 100)
        self.cnt += 1

        return ans

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)