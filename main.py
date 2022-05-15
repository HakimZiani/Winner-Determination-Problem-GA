from Genetic import Genetic
import random

# Potentil buyers bids 
# Key is the buyer ID, Value is tuple(bid ammount,products)
# Exemple : 
#   bids = [(50,["ID1","ID3"]),(35,["ID1"]),(50,["ID2","ID3"])]

p=["ID"+str(i) for i in range(100)]
bids=[(random.randint(1,1000),random.choices(p,k=random.randint(1,10))) for i in range(10)]



m = Genetic(maxGen=1000,bids=bids,verbose=False)
a = m.solve()
print(m.solution)
