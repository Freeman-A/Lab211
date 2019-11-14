from problem import Problem
import random
from random import randint

def numar(x,stack):
     stack.append(x); #O(n)
 
def p(arr,stack):
     arr.append(stack.pop()); #O(n)

class Problem3(Problem):
    def __init__(self):
        statement = '3. Primiti o stiva. Operatii: \n'
        statement += 'numar -> se inseaza numarul in stiva \n'
        statement += 'P -> se extrage un numar din stiva si se afiseaza \n'
        statement += 'Gasiti o succesiune de mutari a.i. introducand el. 1 2 3 4 5 in stiva (in aceasta ordine) la final sa se afiseze 3 2 4 5 1.'
        statement += '\n\n\n'
        
        data=[];
        n=randint(3, 99);  
        for i in range (1, n):
          data.append(randint(1, 99));
        super().__init__(statement, data)
        
    def solve(self):
          solution = 'Vom parcurge vectorul\n'
          solution += 'Se vor citi, in ordine, urmatoarele numere: \n'
          n = len(data);       
          stack = [];
          arr = [];
          ok = 0; #ok := verifica daca s-a citit pana la k (k actioneaza ca un separator)
          i = 0;
          contor = 1;
          n = n-1;
          
          if n <= 3:
               k=radint(1,3);
          else:
               k=radint(int(n/2), n-3);
               
          while i <= n: #O(n^2)
                      if i <= k:
                            if ok == 0:
                                   e = data[i]
                                   numar(e,stack)
                                   solution +='S-a introdus in stiva numarul ' + str(e) + ' lungimea fiind ' + str(len(stack)) + '\n'
                                   if i == k:
                                              ok = 1;
                                              i = 1;
                                   else:
                                        i = i + 1;
                                        contor += 1;
                                       
                            elif contor != 1:
                                    solution += 'Se va elimina din stiva numarul ' + str(data[contor-1]) + '\n'
                                    p(arr,stack);
                                    i = i + 1;
                                    contor -= 1
                                        
                            if ok == 1 & contor == 1: 
                                    contor = k + 1;
                                   
                      else:
                            if contor == n:
                                break;
                            e = data[contor];
                            numar(e,stack);
                            solution +='S-a introdus in stiva numarul ' + str(e) + '\n'
                            solution += 'Se va elimina din stiva numarul ' + str(data[contor-1]) + '\n'
                            p(arr,stack);
                            contor = contor + 1;
                            i = i + 1;
                                
          solution += 'Se va elimina din stiva numarul ' + str(stack[0]) + '\n'   
          p(arr,stack);
          
          solution += 'Rezultatul final este : ' + str(arr) + '\n'
          return solution