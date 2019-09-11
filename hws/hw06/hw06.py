# Object Oriented Programming

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    "sol1 "
    def __init__(self, value=0, previous = 0):
        self.value = value
        self.previous = previous

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.value == 0:
            return Fib(1, 0)
        return Fib(self.value + self.previous, self.value)

    def __repr__(self):
        return str(self.value)

    "sol2 "
    def __init__(self):
        self.value = 0
        self.next_value = 1

    def next(self):
        b = Fib()
        b.value = self.next_value
        b.next_value = b.value + self.value
        return b

    def __repr__(self):
        return str(self.value)

    "sol3"
    def __init__(self, value=0, next_value=1):
        self.value = value
        self.next_value = next_value

    def next(self):
        return Fib(self.next_value, self.value + self.next_value)

    def __repr__(self):
        return str(self.value)


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.rest = 0
        self.balance = 0

    def restock(self, x):
        self.rest += x
        return 'Current {0} stock: {1}'.format(self.name, self.rest)

    def deposit(self, x):
        if self.rest == 0:
            return 'Machine is out of stock. Here is your ${0}.'.format(x)
        else:
            self.balance += x
            return 'Current balance: ${0}'.format(self.balance)

    def vend(self):
        if self.rest == 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price:
            more = self.price - self.balance
            return 'You must deposit ${0} more.'.format(more)
        else:
            self.balance -= self.price
            self.rest -= 1
            if self.balance == 0:
                return 'Here is your {0}.'.format(self.name)
            else:
                more = self.balance
                self.balance = 0
                return 'Here is your {0} and ${1} change.'.format(self.name, more)
