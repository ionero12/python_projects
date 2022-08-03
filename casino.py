from random import randint

playerMoney = int(input("How many euros do you have?"))
print("I have "+str(playerMoney) + " euros")

while playerMoney > 0:
    luckyNumber = int(input("What number do you choose?"))
    if luckyNumber < 0 or luckyNumber > 49:
        luckyNumber = int(input("Please choose a valid number"))
    moneyBet = int(input("How much do you bet?"))
    if moneyBet < playerMoney:
        playerMoney = playerMoney-moneyBet
    else:
        print("Sorry, you lost all the money")
        quit()
    roulletteNumber = randint(0, 49)
    print("The number is " + str(roulletteNumber))
    if roulletteNumber == luckyNumber:
        playerMoney = playerMoney+moneyBet*50
        print("You won" + str(moneyBet*50) + ", now you have " + str(playerMoney) + " euros")
    else:
        print("You lost " + str(moneyBet) + ", now you have " + str(playerMoney) + " euros")
