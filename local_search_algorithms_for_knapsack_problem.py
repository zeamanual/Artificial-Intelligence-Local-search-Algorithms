from ast import arguments
import math
import random
import argparse


class HillClimbing:
    def __init__(self,items,weight):
        self.items_detail = items.copy()
        self.list_of_items= list(self.items_detail.keys())
        self.first_solution=[]
        self.weight = weight

        has_free_space=True
        while has_free_space:
            random_index = random.randint(0,len(self.list_of_items)-1)
            self.first_solution.append(self.list_of_items[random_index])
            temp_duplicate_count = self.get_max_item_occurance(self.first_solution)
            while temp_duplicate_count >3:
                self.first_solution.pop()
                random_index = random.randint(0,len(self.list_of_items)-1)
                self.first_solution.append(self.list_of_items[random_index])
                temp_duplicate_count = self.get_max_item_occurance(self.first_solution)           
            temp_weight=self.get_solution_weight(self.first_solution)
            if(temp_weight>self.weight):
                self.first_solution.pop()
                has_free_space=False

    def get_max_item_occurance(self,solution):
        max_duplicate_count=0
        for i in range(len(solution)):
            temp_duplicate_count=0
            for j in range(len(solution)):
                if(solution[i]==solution[j]):
                    temp_duplicate_count+=1
            if(temp_duplicate_count > max_duplicate_count):
                max_duplicate_count=temp_duplicate_count
        return max_duplicate_count
            
    def get_solution_value(self,solution):
        value = 0
        weight=0
        max_duplicate_count = self.get_max_item_occurance(solution)
        if(max_duplicate_count >3):
            return 0
        for item in solution:
            value+=self.items_detail[item][1]
            weight+=self.items_detail[item][0]
        if(weight>self.weight):
            return 0
        else:
            return value
    
    def get_solution_weight(self,solution):
        weight=0
        for item in solution:
            weight+=self.items_detail[item][0]
        return weight
         
    def get_best_solution(self,solutions):
        best_solution=None
        best_solution_value=0
        for solution in solutions:
            value = self.get_solution_value(solution)
            if(value > best_solution_value):
                best_solution=solution
                best_solution_value=value
        return best_solution
                
    def get_alternative_solutions(self,solution):
        alternative_solutions = []
        items_size = len(self.list_of_items)
        for i in range(items_size*20):
        # for i in range(1000):
            one_solution =solution.copy()
            weight =0
            count =0
            running=True
            while running:
                rand_index = random.randint(0,items_size-1)
                rand_soln_index = random.randint(0,len(one_solution)-1)
                one_solution[rand_soln_index]= self.list_of_items[rand_index]
                count+=1
                if(count>5):
                    one_solution.append(self.list_of_items[rand_index])
                weight=self.get_solution_weight(one_solution)
                while weight>self.weight:
                    one_solution.pop()
                    weight=self.get_solution_weight(one_solution)
                    running=False
            alternative_solutions.append(one_solution)
        
        return alternative_solutions    
        
    def start(self):
        self.best_solution = self.first_solution
        self.best_solution_value = self.get_solution_value(self.best_solution)
        running = True
        while running:
            alternative_solutions = self.get_alternative_solutions(self.best_solution)
            temp_best_solution = self.get_best_solution(alternative_solutions)
            temp_best_soluion_value = self.get_solution_value(temp_best_solution)
            # print('temp best solution ------',temp_best_solution,temp_best_soluion_value)
            if(self.best_solution_value < temp_best_soluion_value):
                self.best_solution=temp_best_solution
                self.best_solution_value=temp_best_soluion_value
            else:
                running= False
        return self.best_solution,self.best_solution_value
     
     
class SimulatedAnnealing:
    def __init__(self,items,weight):
        self.temprature=1000
        self.final_temprature=100
        self.items_detail = items.copy()
        self.list_of_items= list(self.items_detail.keys())
        self.first_solution=[]
        self.weight = weight

        has_free_space=True
        while has_free_space:
            random_index = random.randint(0,len(self.list_of_items)-1)
            self.first_solution.append(self.list_of_items[random_index])
            temp_duplicate_count = self.get_max_item_occurance(self.first_solution)
            while temp_duplicate_count >3:
                self.first_solution.pop()
                random_index = random.randint(0,len(self.list_of_items)-1)
                self.first_solution.append(self.list_of_items[random_index])
                temp_duplicate_count = self.get_max_item_occurance(self.first_solution)           
            temp_weight=self.get_solution_weight(self.first_solution)
            if(temp_weight>self.weight):
                self.first_solution.pop()
                has_free_space=False

    def get_max_item_occurance(self,solution):
        max_duplicate_count=0
        for i in range(len(solution)):
            temp_duplicate_count=0
            for j in range(len(solution)):
                if(solution[i]==solution[j]):
                    temp_duplicate_count+=1
            if(temp_duplicate_count > max_duplicate_count):
                max_duplicate_count=temp_duplicate_count
        return max_duplicate_count
           
    def get_solution_value(self,solution):
        value = 0
        weight=0
        max_duplicate_count = self.get_max_item_occurance(solution)
        if(max_duplicate_count >3):
            return 0
        for item in solution:
            value+=self.items_detail[item][1]
            weight+=self.items_detail[item][0]
        if(weight>self.weight):
            return 0
        else:
            return value
    
    def get_solution_weight(self,solution):
        weight=0
        for item in solution:
            weight+=self.items_detail[item][0]
        return weight
         
    def get_best_solution(self,solutions):
        best_solution=None
        best_solution_value=0
        for solution in solutions:
            value = self.get_solution_value(solution)
            if(value > best_solution_value):
                best_solution=solution
                best_solution_value=value
        return best_solution
                
    def get_alternative_solutions(self,solution):
        alternative_solutions = []
        items_size = len(self.list_of_items)
        for i in range(items_size*20):
            one_solution =solution.copy()
            weight =0
            count =0
            running=True
            while running:
                rand_index = random.randint(0,items_size-1)
                rand_soln_index = random.randint(0,len(one_solution)-1)
                one_solution[rand_soln_index]= self.list_of_items[rand_index]
                count+=1
                if(count>5):
                    one_solution.append(self.list_of_items[rand_index])
                weight=self.get_solution_weight(one_solution)
                # print('weigt in each solution',weight)
                while weight>self.weight:
                    one_solution.pop()
                    weight=self.get_solution_weight(one_solution)
                    running=False
            alternative_solutions.append(one_solution)
        
        return alternative_solutions    
    
    def start(self):
        self.best_solution = self.first_solution
        self.best_soluion_value = self.get_solution_value(self.best_solution)
        running = True
        iteration_count=1
        while running:
            alternative_solutions = self.get_alternative_solutions(self.best_solution)
            temp_best_solution = self.get_best_solution(alternative_solutions)
            temp_best_solution_value = self.get_solution_value(temp_best_solution)
            solution_value_diffrence = temp_best_solution_value-self.best_soluion_value
            acceptance_probablity = math.exp(solution_value_diffrence//self.temprature)
            if(
                solution_value_diffrence > 0
                or
                random.random() < acceptance_probablity
            ):
                self.best_solution=temp_best_solution
                self.best_soluion_value=temp_best_solution_value
            if(self.temprature<self.final_temprature):
                running=False
            
            self.temprature/=iteration_count*0.5
            self.temprature=round(self.temprature,3)
            iteration_count+=1
        return self.best_solution,self.best_soluion_value
     
            
            
class GeneticAlgorithm:
    def __init__(self,items,weight,generation_count,population_size):
        self.generation_count= generation_count
        self.population_size=population_size
        self.items_detail = items.copy()
        self.list_of_items= list(self.items_detail.keys())
        self.weight = weight
        

    def create_initial_population(self,size):
        initial_population = []
        for count in range(size):
            solution =[]
            has_free_space=True
            while has_free_space:
                random_index = random.randint(0,len(self.list_of_items)-1)
                solution.append(self.list_of_items[random_index])
                temp_duplicate_count = self.get_max_item_occurance(solution)
                while temp_duplicate_count >3:
                    solution.pop()
                    random_index = random.randint(0,len(self.list_of_items)-1)
                    solution.append(self.list_of_items[random_index])
                    temp_duplicate_count = self.get_max_item_occurance(solution)           
                temp_weight=self.get_solution_weight(solution)
                if(temp_weight>self.weight):
                    solution.pop()
                    has_free_space=False
            initial_population.append(solution)
        return initial_population
       
    def get_max_item_occurance(self,solution):
        max_duplicate_count=0
        for i in range(len(solution)):
            temp_duplicate_count=0
            for j in range(len(solution)):
                if(solution[i]==solution[j]):
                    temp_duplicate_count+=1
            if(temp_duplicate_count > max_duplicate_count):
                max_duplicate_count=temp_duplicate_count
        return max_duplicate_count
          

    def get_fitness_score(self,solution):
        value = 0
        weight=0
        if(self.get_max_item_occurance(solution) > 3):
            return 0
        for item in solution:
            value+=self.items_detail[item][1]
            weight+=self.items_detail[item][0]
        if(weight>self.weight):
            return 0
        else:
            return value

    def get_solution_weight(self,solution):
        weight=0
        for item in solution:
            weight+=self.items_detail[item][0]
        return weight
 
    def cross_over(self,parents):
        parent_one=parents[0]
        parent_two=parents[1]
        solution_length = len(parent_one)
        offspring1=parent_one[:solution_length//2]
        offspring2 = parent_two[:solution_length//2]
        
        for gene in parent_two:
            if gene not in offspring1:
                offspring1.append(gene)
        for gene in parent_one:
            if gene not in offspring2:
                offspring2.append(gene)
        return [offspring1,offspring2]

    def mutate_solution(self,solution):
        solution_length=len(solution)
        rand_index_one = random.randint(0,solution_length-1)
        rand_index_two = random.randint(0,len(self.list_of_items)-1)
        solution[rand_index_one]= self.list_of_items[rand_index_two]
        
        return solution     
        
    def start(self):
        temprature = 60
        final_temprature=10
        self.best_solution=None
        self.best_solution_fitness_score = 0
        
        population = self.create_initial_population(self.population_size)
        for count in range(self.generation_count):
            tested_population_detail = []
            for solution in population:
                score = self.get_fitness_score(solution)
                tested_population_detail.append([score,solution])
            tested_population_detail.sort()
            
            top_solutions_detail = tested_population_detail[-100:]
            temp_best_solution=top_solutions_detail[-1]
            
            if(temp_best_solution[0]>self.best_solution_fitness_score):
                self.best_solution=temp_best_solution[1]
                self.best_solution_fitness_score=temp_best_solution[0]
                temprature=60
            else:
                temprature-=10
                if(temprature<10):
                    break
    
            best_solutions = []
            for solution in top_solutions_detail:
                best_solutions.append(solution[1])
            
            population=[]
            for size in range(self.population_size//2):
                parent_one = best_solutions[ random.randint(0,len(best_solutions)-1)]
                parent_two = best_solutions[ random.randint(0,len(best_solutions)-1)]
                
                offsprings = self.cross_over([parent_one,parent_two])
                offsprings[0]=self.mutate_solution(offsprings[0])
                offsprings[1]=self.mutate_solution(offsprings[1])
                population.append(offsprings[0])
                population.append(offsprings[1])

        return self.best_solution,self.best_solution_fitness_score
                
        

 #load all data from file
item_quantity=0
def load_data(filename):
    
    #Reading contents of items file
    items_file= open(filename)
    global required_weight , items
    
    items={}
    read_line=items_file.readline()
    required_weight = int(read_line)
    
    read_line = items_file.readline()
    read_line = items_file.readline()
    while(read_line):
        read_line=read_line.split(',')
        items[read_line[0]]=[float(read_line[1]),float(read_line[2])]
        read_line=items_file.readline()
    items_file.close()


def get_huristic_value(location_one,location_two):
    RADIUS=6373.0
    latitude_one = math.radians(location_one[0])
    longitude_one = math.radians(location_one[1])
    latitude_two = math.radians(location_two[0])
    longitude_two = math.radians(location_two[1])

    diffrence_in_longitude = longitude_two-longitude_one
    diffrence_in_latitude = latitude_two -latitude_one

    a = math.pow((math.sin(diffrence_in_latitude/2)),2) + math.cos(latitude_one)*math.cos(latitude_two)*math.pow((math.sin(diffrence_in_longitude/2)),2)
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    distance_between = RADIUS * c
    return distance_between
  
    
def main():
    parser = argparse.ArgumentParser(description="Get file and algorithm name")
    parser.add_argument('--algorithm',help='Enter the name of the algorithm to use such as ga, hl, sa')
    parser.add_argument('--file',help='Enter the name of the file to read from')
    arguments = parser.parse_args()

    filename = arguments.file
    algorithm = arguments.algorithm
    load_data(filename)

    if(algorithm=='ga'):
        genetic_algorithm = GeneticAlgorithm(items,required_weight,20,200)
        result = genetic_algorithm.start()
        print(result)
       
    elif(algorithm=='hl'):
        hill_climbing_algorithm = HillClimbing(items,required_weight)
        result = hill_climbing_algorithm.start()
        print(result)
    elif(algorithm=='sa'):
        simulated_annealing = SimulatedAnnealing(items,required_weight)
        result = simulated_annealing.start()
        print(result)
    
main()