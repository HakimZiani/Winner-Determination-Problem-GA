from Genetic import Genetic
import random

# Potentil buyers bids 
# Key is the buyer ID, Value is tuple(bid ammount,products)
# Exemple : 
#   bids = [(50,["ID1","ID3"]),(35,["ID1"]),(50,["ID2","ID3"])]
number_products=10000
number_buyers=10
p=["ID"+str(i) for i in range(number_products)]
bids=[(random.randint(1,1000),random.choices(p,k=random.randint(1,100))) for i in range(number_buyers)]



m = Genetic(maxGen=25,bids=bids,verbose=False)
a = m.solve(showProfit=1)
print(m.solution)
