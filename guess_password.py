import random

easy_words = ["easy","girl","food","train","metro","sync"]
medium_words = ["medium","bucket","magnet","cheeze","slipper","tomato"]
hard_words = ["hard","blanket","momento","glasses","cutting","cyclinder"]


print("Word Guessing Game")
print("choose difficulty level (easy,medium,hard) : ")

level = input('Enter difficulty : ').lower()
if level == "easy":
   secret = random.choice(easy_words)
elif level == "medium":
   secret = random.choice(medium_words)
elif level == "hard":
   secret = random.choice(hard_words)
else:
   print("Invalid Choice. Default level - Easy")
   secret = random.choice(easy_words)

attempts = 0
print("---Guess the secret word---")

while True:
    guess = input("enter your guess : ").lower()
    attempts += 1

    if guess == secret:
      print(f"Congrulations you guess the word in {attempts} attempts")
      break

    hint = ""
   
    for i in range(len(secret)):
       if i < len(guess) and guess[i] == secret[i]:
         hint += guess[i]
       else:
         hint += "_"
    print("hint : ",hint)

print("Game Over")