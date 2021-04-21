import random
#if tails, wakeup monday, forget monday, wakeup tuesday
#if heads, wakeup monday
#what is the probablity of heads

#https://www.youtube.com/watch?v=zL52lG6aNIY


numberTrials = 100
headCounter = 0
tailsCounter = 0
coin = ["coinHeads", "coinTails"]
days = ["headsMonday","tailsMonday", "tailsTuesday"]


for j in range(0,numberTrials):
    wakeupDay = random.choice(days)
    coinResult = random.choice(coin)
    #print(wakeupDay)
    #P(Heads)

    if coinResult == "coinHeads" and wakeupDay == "headsMonday":
        #sleepings guess of heads
        headCounter = headCounter + 1
    elif coinResult == "coinTails" and days == "tailsMonday" or "tailsTuesday":
        tailsCounter = tailsCounter + 1

    

print(tailsCounter)
print(headCounter)
print((numberTrials-(tailsCounter-headCounter))/numberTrials)

