import random
global money
money = 100
num = random.randint(1, 2)
heads = 1 
tails = 2



def coin_flip(num):
  global money
  num = random.randint(1, 2)
  a = int(input("How much would you like to bet?: $"))
  b = input("Heads or Tails?: ")
  

  if b == "heads" and num == 1 or b == "tails" and num == 2:
    money += a
    return "You guessed correctly! " + str(b) + ": Your bet: $" + str(a) + " You now have: $" + str(money) 
  

  elif b == "heads" and num == 2 or b == "tails" and num == 1:
    money += -a
    return "Sorry! You owe: $" + str(a) + " You now have: $" + str(money) 

  else:
   money += -a
   return "Sorry! It was Heads: You owe: $" + str(a) + " You now have: $" + str(money)

     
  coin_flip(num)
  #print(coin_flip(num))
