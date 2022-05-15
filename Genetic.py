import random
from numpy import product
import matplotlib.pylab as plt
from sqlalchemy import null, true
class Genetic:
    solution = list()
    def __init__(self,maxGen,bids,population_size=10,verbose=0) -> None:
        self.maxGen = maxGen
        self.population_size = population_size
        self.bids = bids
        self.population = list()
        self.verbose=verbose
    # validBid a function to verify if a bid is correct
    # a bid is correct if it doesn't contains contraditions
    # a contradition is two buyers buying the same product
    def validBid(self,bid):
        products = []
        for i in range(len(bid)):
            if(bid[i]==1):
                products.extend(self.bids[i][1])
        #print(products)
        if len(products)==len(set(products)):
            return True
        else:
            return False
    # Init the Population with random population
    def initPopulation(self):
        self.population = [[random.randint(0,1) for _ in range(len(self.bids))] \
        for _ in range(self.population_size)]
    # the fitness calculate the profit for each chromosome
    def fitness(self):
        Gen =[]
        for chromosome in self.population:
            profit =0 
            for i in range(len(chromosome)):
                if chromosome[i]==1:
                    profit+= self.bids[i][0]
            Gen.append((chromosome,profit)) 
        return Gen 
    def fitnessChromosome(self,chromosome):
        # the fitness calculate the profit for a certain chromosome
        profit =0 
        for i in range(len(chromosome)):
            if chromosome[i]==1:
                profit+= self.bids[i][0]
        return profit    
    # Selection using Roulette wheel
    def Selection(self,GF, k=5):
        sumOFfitnesses = sum([el[1] for el in GF ])
        selected =[]
        proba = [(el[0],el[1]/sumOFfitnesses) for el in GF]
        cumulative = []
        cumulative.append(proba[0])
        for i in range(1,len(proba)):
            cumulative.append((proba[i][0],proba[i][1]+cumulative[i-1][1]))
        for i in range(k):
            r = random.random()
            for c in cumulative:
                if c[1]>r:
                    selected.append(c[0])
                    break
        return selected
    def CrossOver(self,gen):
        Crossed = []
        for i in range(len(gen)):
            for j in range(len(gen)):
                first = gen[i]
                second = gen[j]

                if i!=j:
                    r1 = random.randint(0,len(first))
                    v = first[0:r1]
                    v.extend(second[r1:])
                    
                    Crossed.append(v)
                    break
        return Crossed
    def Mutation(self,gen):
        for el in gen:
            while(self.validBid(el) ==False):               
                r = random.randint(0,len(el)-1  )
                if el[r]==1:
                    el[r] = 0
                else: 
                    el[r]=1
        return gen
    # To get the best chromosome in the generation 
    def getBestGen(self,gen):
        max =0
        for el in gen:
            if el[1]>max:
                max = el[1]
                best = el[0]
        return best
    # main function
    def solve(self,showProfit=0):
        self.initPopulation()
        gen =1
        profits=[]
        while(gen<self.maxGen):
            # GenerationFitness is dict containing for each chromosome its fitness score
            GenerationFitness = self.fitness()
            self.solution  = self.getBestGen(GenerationFitness)
            p = list(zip(*self.fitness()))[1]
            profits.append(sum(p)/len(p))
            if self.verbose==1:
                print("Gen ",gen,": ",self.solution,"Profit:",self.fitnessChromosome(self.solution))
            SelectedGen = self.Selection(GenerationFitness)
            Crossed = self.CrossOver(SelectedGen)
            Mutated = self.Mutation(Crossed)
            self.population = Mutated
            gen+=1
        if showProfit==1:
            plt.plot(range(1,len(profits)),profits[1:])
            plt.xlabel("Generation")
            plt.ylabel("Mean Profit")
            plt.show()
        return self.solution
