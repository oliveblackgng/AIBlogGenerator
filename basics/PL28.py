class Item:
    def __init__(self, price):
        self._price = price

    @property  # alternative for calling function
    def price(self):           # Getter
        return self._price

    @price.setter
    def price(self, value):    # Setter
        if value >= 0:
            self._price = value
        else:
            print("Invalid price!")