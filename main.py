from Utils import *
from Poll import Poll

df= loadAndCleanData("2020nominee.csv")
#df= normalizeData("2020nominee.csv")
pollNames= pd.unique(df["Poll"])
print(pollNames)

polls=[]
for name in pollNames:
    poll=Poll(name,df)
    polls.append(poll)
#print(polls)
    print(poll.outlet)
    print(poll.getMostRecentPoll())
    print(str(poll.countPoll()))
    print("Change in poll for sanders" + str(poll.changeInPoll("Sanders")))
    print(poll.avgInPoll("Sanders"))
    print(poll.plotCandidate("Sanders"))
