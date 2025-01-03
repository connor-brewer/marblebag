import random



# This was just to answer a simple question I had about probabilites, and the
# average outcome of a specific question.
# What if you had a bag that had two colored marbles. One red, and one blue. You
# choose one at random, a 50/50 outcome, and let's say it's red. Then, we would
# add a red marble into the bag and place the orignal marble we drew (red) back
# into the bag as well. Then, the bag would have 2 red marbles and 1 blue
# marble. If we keep doing this, what is the average ratio of marbles in the bag
# as time goes on? And what if we do this process over and over again,
# restarting after a certain amount of draws?
# The specific inspiration came from Balatro, a video game. There's a "joker"
# card that duplicates one of the cards in your inventory, but it picks one at
# random. If you started with two cards in your inventory, what should you
# expect, on average, the ratio of cards to be overtime?



let_sim_and_iters_be_same = True
let_sim_and_numelems_be_same = False
numsimulations = 3163
# example inputs: 1000 3163 5000

numiters = 100
numelems = 10



if (let_sim_and_iters_be_same or numiters == 0):
    numiters = numsimulations
    
if (let_sim_and_numelems_be_same or numelems == 0):
    numelems = numsimulations

lim = numiters

largercount = []
for j in range (0, numsimulations):
    dararr = ["a", "b"]
    for i in range (0, numiters):
        idx = random.randint(0, len(dararr) - 1)
        val = dararr[idx]
        dararr.append(val)
    if dararr.count("a") > dararr.count("b"):
        largercount.append(dararr.count("a"))
    else:
        largercount.append(dararr.count("b"))
    
# print(largercount)

modelarge = max(set(largercount), key=largercount.count)
maxcount = largercount.count(modelarge)
modes = []
for element in set(largercount):
    if largercount.count(element) == maxcount:
        modes.append(element)
modesmall = lim - modelarge

sortedlargercount = sorted(largercount)
medianlarge = sortedlargercount[int(len(sortedlargercount)/2)]
mediansmall = lim - medianlarge

avglarge = sum(largercount) / len(largercount)
avgsmall = lim - avglarge

print("Testing", numsimulations, "simulations, each simulating",  numiters, "iterations.")
print("")

print("Average Split:", avglarge, "to", avgsmall)
print("Average Percentage Split:", (avglarge/lim), "to", (avgsmall/lim))

print("")

print("Median Split:", medianlarge, "to", mediansmall)
print("Median Percentage Split:", (medianlarge/lim), "to", (mediansmall/lim))

print("")

print("Mode Split:", modelarge, "to", modesmall, "   (1/" + str(len(modes)) + ")")
print("Mode Percentage Split:", (modelarge/lim), "to", (modesmall/lim))

print("")

setarr = set(sortedlargercount)
setarr = list(setarr)
elevals = []
countvals = []
for i in range(len(setarr)):
    ele = setarr[i]
    countofele = sortedlargercount.count(ele)
    elevals.append(ele)
    countvals.append(countofele)


dadict = {}
for i in range(len(elevals)):
    dadict[elevals[i]] = countvals[i]


dadictsorted = {k: v for k, v in sorted(dadict.items(), key=lambda item: item[1], reverse=True)}



parr = []

for index, (key, value) in enumerate(dadictsorted.items()):
    percval = float(int(key)/lim)
    if int(percval) == 1:
        percval = ((lim-1)/lim)
    idvstr = str(percval) + " appears " + str(value) +  " times"
    parr.append(idvstr)

if numelems > len(setarr):
    numelems = len(setarr)


printstr = "The amount of times each larger count percentage split shows up in " +  str(lim) + " larger count splits."
print(printstr)
print("This is the first", str(numelems), "entries:")

for i in range(0, numelems):
    print(parr[i])

# print("")
# print("This is the last", str(numelems), "entries:")
# for i in range(len(setarr)-1, len(setarr) - numelems - 1, -1):
#     print(parr[i])




import matplotlib.pyplot as plt

a = []
b = []

for index, (key, value) in enumerate(dadictsorted.items()):
    ball = float(int(key)/lim)
    if int(ball) == 1:
        ball = ((lim-1)/lim)
    a.append(ball)     b.append(value)

plt.scatter(a, b)
plt.title('Appearances of Larger Split Percentages')
plt.xlabel('Percentage Value')
plt.ylabel('Number of Times Percentage Appears')
plt.show()




# Results/Conclusions:
# The average of all of the simulations seems to converge around a 75% to 25%
# split as we increase the number of iterations
# Looking at the count of how many percentages appear, its hard to really tell
# how each individual simulation predictably behaves. It sometimes baloons, it
# sometimes stays around 50/50 to 60/40, and sometimes it hovers around the 75% 
# average.
# It's hard to draw any conclusions about what you should expect. The 75% average
# feels a bit misleading, considering the mode doesn't show any sort of trend at 
# all.
# In practice, people aren't that likely to experience/feel the 75% average, even
# though that's what it is.
# When you start the experiment, it's fair to have that 75% number in mind, but 
# as it goes on, you can probably tell whether or not it's going to actually 
# approach that value. If you see it getting closer and closer to one value, that
# begins to dominate. Quickly. But if it stays balanced for awhile, it's more 
# likely to stay that way longer (a tipping of the scale doesn't do as much).

# Future Considerations/Implementations:
# Possibly implement multiple colors/options. What if there were three marbles? 
# Or four? Or one hundred?







