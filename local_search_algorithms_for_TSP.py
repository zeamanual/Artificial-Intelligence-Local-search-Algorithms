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
     
   