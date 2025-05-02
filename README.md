# 🎲 Coin Flip App

This is a basic command-line Python game that simulates flipping a coin and betting on the result. It was one of the first Python apps I built, and it helped me learn about functions, conditionals, and handling user input.

## 💡 Features

- Starts with a virtual wallet of $100.
- Lets you bet any amount on **Heads** or **Tails**.
- Flips a virtual coin and tells you if you won or lost.
- Updates your balance after each flip.

## 🧪 How It Works

1. You are asked how much you'd like to bet.
2. You choose between `"heads"` or `"tails"`.
3. The app flips a virtual coin using Python's `random.randint(1, 2)`.
4. If your guess is correct, your bet is added to your balance.
5. If your guess is wrong, your bet is subtracted from your balance.
6. Your new balance is shown.

## 🖥️ Example

```bash
How much would you like to bet?: $20
Heads or Tails?: heads
You guessed correctly! heads: Your bet: $20 You now have: $120
```

## 📂 Files

- `coin_flip.py` — Main and only file. Contains all the game logic.

## 🚀 How to Run

Make sure you have Python installed, then run:

```bash
python3 coin_flip.py
