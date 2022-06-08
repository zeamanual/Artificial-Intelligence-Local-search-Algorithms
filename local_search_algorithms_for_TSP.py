import argparse
import math
import random

class HillClimbing:
    def __init__(self,city_coordinates):
        local_city_coordinates=city_coordinates.copy()
        self.city_coordinates = local_city_coordinates.copy()
        self.first_solution=[]
        for city in self.city_coordinates.keys():
            random_index = random.randint(0,len(local_city_coordinates)-1) 
            self.first_solution.append(list(local_city_coordinates.keys())[random_index])
            local_city_coordinates.pop(list(local_city_coordinates.keys())[random_index])
           
    def get_solution_cost(self,solution):
        cost = 0
        for current_city_index in range(len(solution)):
            if ( current_city_index+1<len(solution)):
                in_between_cost = get_huristic_value(self.city_coordinates[solution[current_city_index]],self.city_coordinates[solution[current_city_index+1]])
                cost+=in_between_cost
        return cost

    def get_best_solution(self,solutions):
        best_solution=None
        best_solution_cost=float('inf')
        for solution in solutions:
            cost = self.get_solution_cost(solution)
            if(cost < best_solution_cost):
                best_solution=solution
                best_solution_cost=cost
        return best_solution
                
    def get_alternative_solutions(self,solution):
        alternative_solutions = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbour = solution[0:]
                neighbour[i] = solution[j]
                neighbour[j] = solution[i]
                alternative_solutions.append(neighbour)
        return alternative_solutions
    
    def start(self):
        self.best_solution = self.first_solution
        self.best_soluion_cost = self.get_solution_cost(self.best_solution)
        running = True
        while running:
            alternative_solutions = self.get_alternative_solutions(self.best_solution)
            temp_best_solution = self.get_best_solution(alternative_solutions)
            if(self.best_soluion_cost > self.get_solution_cost(temp_best_solution)):
                self.best_solution=temp_best_solution
                self.best_soluion_cost=self.get_solution_cost(temp_best_solution)
            else:
                running= False
        return self.best_solution,self.best_soluion_cost
     
     
class SimulatedAnnealing:
    def __init__(self,city_coordinates):
        local_city_coordinates=city_coordinates.copy()
        self.city_coordinates = local_city_coordinates.copy()
        self.temprature=100
        self.final_temprature=2
        self.first_solution=[]
        for city in self.city_coordinates.keys():
            random_index = random.randint(0,len(local_city_coordinates)-1) 
            self.first_solution.append(list(local_city_coordinates.keys())[random_index])
            local_city_coordinates.pop(list(local_city_coordinates.keys())[random_index])
              
    def get_solution_cost(self,solution):
        cost = 0
        for current_city_index in range(len(solution)):
            if ( current_city_index+1<len(solution)):
                in_between_cost = get_huristic_value(self.city_coordinates[solution[current_city_index]],self.city_coordinates[solution[current_city_index+1]])
                cost+=in_between_cost
        return cost

    def get_best_solution(self,solutions):
        best_solution=None
        best_solution_cost=float('inf')
        for solution in solutions:
            cost = self.get_solution_cost(solution)
            if(cost < best_solution_cost):
                best_solution=solution
                best_solution_cost=cost
        return best_solution
                
    def get_alternative_solutions(self,solution):
        alternative_solutions = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbour = solution[0:]
                neighbour[i] = solution[j]
                neighbour[j] = solution[i]
                alternative_solutions.append(neighbour)
        return alternative_solutions
    
    def start(self):
        self.best_solution = self.first_solution
        self.best_soluion_cost = self.get_solution_cost(self.best_solution)
        running = True
        iteration_count=1
        while running:
            alternative_solutions = self.get_alternative_solutions(self.best_solution)
            temp_best_solution = self.get_best_solution(alternative_solutions)
            temp_best_solution_cost = self.get_solution_cost(temp_best_solution)
            solution_cost_diffrence = temp_best_solution_cost-self.best_soluion_cost
            acceptance_probablity = math.exp(-solution_cost_diffrence//self.temprature)
            if(
                solution_cost_diffrence < 0
                or
                random.random() < acceptance_probablity
            ):
                self.best_solution=temp_best_solution
                self.best_soluion_cost=temp_best_solution_cost
            if(self.temprature<self.final_temprature):
                running=False
            
            self.temprature/=iteration_count*0.5
            iteration_count+=1
        return self.best_solution,self.best_soluion_cost
     
            
            
class GeneticAlgorithm:
    def __init__(self,city_coordinates,generation_count,population_size):
        self.city_coordinates = city_coordinates.copy()
        self.generation_count= generation_count
        self.population_size=population_size

    def create_initial_population(self,size):
        initial_population = []
        city_cordinates=self.city_coordinates.copy()
        for i in range(size):
            solution=[]
            for city in self.city_coordinates.keys():
                random_index = random.randint(0,len(city_cordinates)-1) 
                solution.append(list(city_cordinates.keys())[random_index])
                city_cordinates.pop(list(city_cordinates.keys())[random_index]) 
            initial_population.append(solution)
            city_cordinates=self.city_coordinates.copy()      
        return initial_population
            
    def get_fitness_score(self,solution):
        cost = 0
        for current_city_index in range(len(solution)):
            if ( current_city_index+1<len(solution)):
                in_between_cost = get_huristic_value(self.city_coordinates[solution[current_city_index]],self.city_coordinates[solution[current_city_index+1]])
                cost+=in_between_cost
        return 1/cost
       
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
        temp_one = random.randint(0,solution_length-1)
        temp_two = random.randint(0,solution_length-1)
        temp = solution[temp_one]
        solution[temp_one]=solution[temp_two]
        solution[temp_two]=temp
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
            # print(f"generation {count} best {1/temp_best_solution[0]}")
    
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

        return self.best_solution,1/self.best_solution_fitness_score
                
        

 #load all data from file
def load_data(filename):
    
    #Reading contents of city coordinates file
    city_coordinate_file= open(filename)
    global city_coordinates
    city_coordinates={}
    read_line=city_coordinate_file.readline()
    while(read_line):
        read_line=read_line.split(',')
        city_coordinates[read_line[0]]=[float(read_line[1]),float(read_line[2])]
        read_line=city_coordinate_file.readline()
    city_coordinate_file.close()


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

