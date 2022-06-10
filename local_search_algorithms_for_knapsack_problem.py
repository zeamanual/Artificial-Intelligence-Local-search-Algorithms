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
     
    