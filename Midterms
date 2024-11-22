from abc import ABC, abstractmethod

class Wallet(ABC):
    def __init__(self, owner, __balance=0.0):
        self.owner = owner
        self._balance = __balance

    @property
    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def transaction(self, amount, transaction_type):
        pass

class BitcoinWallet(Wallet):
    def __init__(self, owner, __balance=0.0):
        super().__init__(owner, __balance)

    @property
    def balance(self):
        return self._balance

    def transaction(self, amount, transaction_type):
        if transaction_type == "buy":
            self._balance += amount
        elif transaction_type == "sell":
            if amount > self._balance:
                print("Insufficient balance.")
            else:
                self._balance -= amount
        return self._balance

class EthereumWallet(Wallet):
    def __init__(self, owner, __balance=0.0):
        super().__init__(owner, __balance)

    @property
    def balance(self):
        return self._balance

    def transaction(self, amount, transaction_type):
        if transaction_type == "buy":
            self._balance += amount
        elif transaction_type == "sell":
            if amount > self._balance:
                print("Insufficient balance.")
            else:
                self._balance -= amount
        return self._balance

# Operations
alice_wallet = BitcoinWallet("Alice", 0.5)
print(f'''Bitcoin Wallet for {alice_wallet.owner} 
Initial Balance: {alice_wallet.balance} BTC''')
alice_wallet.transaction(0.2, "buy")
print(f'''Performing Transaction: Buy 0.2 BTC 
New Balance: {alice_wallet.balance} BTC''')
print()
bob_wallet = EthereumWallet("Bob", 2)
print(f'''Ethereum Wallet for {bob_wallet.owner} 
Initial Balance: {bob_wallet.balance} ETH''')
bob_wallet.transaction(1, "sell")
print(f'''Performing Transaction: Sell 1 
ETH New Balance: {bob_wallet.balance} ETH''')
