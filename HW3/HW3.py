# CptS 355 - Spring 2023 - Assignment 3 - Python

# Please include your name and the names of the students with whom you discussed any of the problems in this homework
# Name: EMMA JOHNSON
# Collaborators: 

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

from functools import reduce

## problem 1(a) - aggregate_log  - 5%
##adds up the number of hours you studied on each day of the week and returns the summed values as a dictionary
def aggregate_log(data):
     d = {}
     for (classes, log) in data.items():
          for (day, num) in log.items():
               if day not in d:
                    d[day] = num
               else: 
                    d[day] += num 
     return d

## problem 1(b) - combine_dict– 6%
##combines two given study logs and returns the merged dictionary. 

def combine_dict(log1, log2):
     d = {}
     for (day, num) in log1.items():
          d[day] = num

     for (day, num) in log2.items():
               if day not in d:
                    d[day] = num
               else: 
                    d[day] += num 
     return d

## problem 1(c) - merge_logs– 12%
##takes a list of course log dictionaries and returns a dictionary which includes the combined logs for each class

def merge_logs(log_list):
     d = {}
     for dict in log_list:
          for (classes, log) in dict.items():
               if classes not in d:
                    d[classes] = log
               else:
                    d[classes] = combine_dict(d[classes], log)
     return d
## problem 2(a) - most_hours – 15%

from functools import reduce
def most_hours(data):
     if data is None: return None
     map_helper = lambda log: reduce (lambda x,y : x+y, log.values())
     map_result = list (map (lambda t: (t[0], map_helper(t[1])), data.items()))
     return reduce (lambda t1, t2 : t1 if t1[1] >= t2[1] else t2, map_result)

## problem 2(b) - filter_log – 15%
def filter_log(log, day, hours):
     filter_helper =  filter(lambda course: True if day in log.get(course) else False, log)
     return list(filter(lambda course: True if log[course][day] >= hours else False, filter_helper))
## problem 3 - graph_cycle – 12% 
graph = {'A':('B',5),'B':('D',3),'C':('G',10),'D':('E',4),'E':('C',5),
'F':('I',4),'G':('B',9),'H':('G',5),'I':('H',3)}

def graph_cycle(graph, start):
     def graph_help (graph, start, cur_cycle):
          if graph.get(start) is None: 
               return None
          elif start in cur_cycle:
               cur_cycle = cur_cycle + [start] 
               return (cur_cycle[cur_cycle.index(cur_cycle[-1],0,-1):])        
          else: 
               return graph_help (graph, graph[start][0], cur_cycle + [start])
         
     if graph_help(graph, start, []) is None:
         return None
     else:
         return graph_help(graph, start, [])


##problem 4 - filter_iter
# ##Create an iterator whose constructor takes a function (op) and an iterable value (it) as argument and applies op on
##each value of the input iterator. At each call to the next function, the iterator will return the result of (op x)
##where x is the next value from the input sequence.
class filter_iter:
    def __init__(self, it, op):
        self.it = iter(it)
        self.op = op

    def __iter__(self):
        return self

    def __next__(self):
        if self.it is None: 
               raise StopIteration
        x = next(self.it)
        while not self.op(x):
            x = next(self.it)
        return x

it = iter([7,4,5,3,3,6,2])
print(list(filter_iter(it, lambda x: x>0)))

## problem 5 - merge – 10% 
     
def merge(it1, it2, N):
     merged_list = []
     n1 = next(it1, None)
     n2 = next(it2, None)
     for n0 in range(N):
          #print(n0)
          if n1 is not None and n2 is not None:
               if n1 <= n2:
                    print("case1") 
                    merged_list.append(n1) 
                    n1 = next(it1, None)
               else:
                    print("case2") 
                    merged_list.append(n2) 
                    n2 = next(it2, None)
     return merged_list