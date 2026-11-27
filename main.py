"""main.py - Menu program for the Cellphone Load Wallet.
Run with: python main.py
"""

from load_wallet import LoadWallet


def read_amount(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def read_mobile(prompt):
    """Keep asking until the user enters an 11-digit number starting with 09."""
    while True:
        number = input(prompt).strip()
        if number.isdigit() and len(number) == 11 and number.startswith("09"):
            return number
        print("Invalid number. Use 11 digits starting with 09 (e.g., 09171234567).")


def create_wallet():
    print("=== Create Your Load Wallet ===")
    name = input("Owner name: ").strip() or "Subscriber"
    number = read_mobile("Mobile number: ")
    network = input("Your network (e.g., Globe, Smart): ").strip() or "Globe"
    while True:
        balance = read_amount("Starting balance: P")
        try:
            return LoadWallet(name, number, balance, network)
        except ValueError as error:
            print(error)


def main():
    wallet = create_wallet()
    menu = """
===== LOAD WALLET MENU =====
1. Top up load
2. Send load (same network)
3. Send load with fee (different network)
4. Check balance
5. Exit"""
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            wallet.top_up(read_amount("Amount to top up: P"))
        elif choice == "2":
            number = read_mobile("Recipient number: ")
            wallet.send_load(number, read_amount("Amount to send: P"))
        elif choice == "3":
            number = read_mobile("Recipient number: ")
            wallet.send_with_fee(number, read_amount("Amount to send: P"))
        elif choice == "4":
            wallet.show_balance()
        elif choice == "5":
            print("Thank you for using Load Wallet. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
