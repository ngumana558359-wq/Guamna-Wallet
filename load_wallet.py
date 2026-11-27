"""load_wallet.py - Class definition for the Cellphone Load Wallet."""


class LoadWallet:
    """Manages a subscriber's prepaid load balance."""

    SERVICE_FEE = 2.00  # flat fee (in pesos) for sending to a different network

    def __init__(self, owner_name, mobile_number, starting_balance, network):
        # Public attributes
        self.owner_name = owner_name
        self.mobile_number = mobile_number
        self.network = network
        # Private attribute (encapsulation): balance can only change via methods
        self.__balance = 0.0
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative.")
        self.__balance = float(starting_balance)

    def get_balance(self):
        """Read-only access to the private balance."""
        return self.__balance

    def top_up(self, amount):
        """Add load to the wallet. Rejects zero or negative amounts."""
        if amount <= 0:
            print("Top-up failed: amount must be greater than 0.")
            return False
        self.__balance += amount
        print(f"Top-up successful! Added P{amount:.2f}.")
        return True

    def send_load(self, recipient_number, amount):
        """Send load to a number on the SAME network (no fee)."""
        if amount <= 0:
            print("Transfer failed: amount must be greater than 0.")
            return False
        if recipient_number == self.mobile_number:
            print("Transfer failed: you cannot send load to your own number.")
            return False
        if amount > self.__balance:
            print(f"Transfer failed: insufficient balance (P{self.__balance:.2f}).")
            return False
        self.__balance -= amount
        print(f"Sent P{amount:.2f} to {recipient_number}.")
        return True

    def send_with_fee(self, recipient_number, amount):
        """Send load to a DIFFERENT network. A service fee is charged on top."""
        if amount <= 0:
            print("Transfer failed: amount must be greater than 0.")
            return False
        if recipient_number == self.mobile_number:
            print("Transfer failed: you cannot send load to your own number.")
            return False
        total = amount + self.SERVICE_FEE
        if total > self.__balance:
            print(f"Transfer failed: you need P{total:.2f} "
                  f"(amount + P{self.SERVICE_FEE:.2f} fee) but have P{self.__balance:.2f}.")
            return False
        self.__balance -= total
        print(f"Sent P{amount:.2f} to {recipient_number} "
              f"(service fee: P{self.SERVICE_FEE:.2f}, total deducted: P{total:.2f}).")
        return True

    def show_balance(self):
        """Display the wallet details and current balance."""
        print(f"Owner  : {self.owner_name}")
        print(f"Number : {self.mobile_number} ({self.network})")
        print(f"Balance: P{self.__balance:.2f}")
