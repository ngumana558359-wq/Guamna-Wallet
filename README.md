# Cellphone Load Wallet

A small OOP program (Python) that manages a subscriber's prepaid load balance.

## Files
- `load_wallet.py` - the `LoadWallet` class (private balance, `top_up()`, `send_load()`, `send_with_fee()`, `show_balance()`)
- `main.py` - the menu program that imports `LoadWallet`

## How to run
```
python main.py
```

## OOP concepts used
- **Class & objects**: `LoadWallet` instance created from user input
- **Encapsulation**: the balance is private (`__balance`) and only changed through methods
- **Validation**: rejects negative amounts, insufficient balance, and sending to your own number
- Sending to a different network costs a P2.00 service fee (`SERVICE_FEE`)
