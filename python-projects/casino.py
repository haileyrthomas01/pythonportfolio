import random

symbols = ['🍒','🍇', '🍉', '7️⃣ ']

results = random.choices(symbols, k=3)
print(' | '.join(results))

if all(symbol == '7️⃣' for symbol in results):
  print("Jackpot! 💰")
else:
  print("Thanks for playing!")