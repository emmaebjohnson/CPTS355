# CptS 355 - Spring 2023 - Lab 3
# Please include your name here: Emma Johnson

debugging = False
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1 getNumCases - which calculates the total number of new cases for a given list 
##of counties during a given list of months


 
## problem 2 getMonthlyCases - formats the CDC data as described above
def getMonthlyCases(data):
     d = {}
     for (county, log) in data.items():
          for (month, num) in log.items():
               if month not in d:
                    d[month] = {}
               d[month][county]  = num 
     return d


## problem 3 mostCases -  find the month that had the maximum total number of new cases

from functools import reduce
def mostCases(data):
     monthlyCases = getMonthlyCases(data)
     map_helper = lambda log: reduce (lambda x,y : x+y, log.values())
     map_result = list (map (lambda t: (t[0], map_helper(t[1])), monthlyCases.items()))
     return reduce (lambda t1, t2 : t1 if t1[1] >= t2[1] else t2, map_result)

## problem 4a) searchDicts(L,k) - akes a list of dictionaries L and a key k as input and checks 
##each dictionary in L starting from the end of the list.

def searchDicts(L, k):
    tL = list(reversed(L))
    for i in range(0, len(L)):
        if k in tL[i]:
            return tL[i][k]
    return None

## problem 4b) searchDicts2(L,k)
def searchDicts2(L,k):
     def helper(tL, k, ind):
          if k in tL[ind][1]:
               return tL[ind][1][k]
          else:
               if ind == 0:
                    return None
               else:
                    return helper(tL, k, tL[ind][0])
     return helper (L, k, len(L) -1)

## problem 5 - getLongest - arbitrarily nested list of strings (L) and it returns the longest string in L. 
def getLongest(L):
     getLonger = lambda x,y: x if len(x) >= len(y) else y
     longest = ''
     for item in L:
          if isinstance(item, list):
               longest = getLonger(longest, getLongest(item))
          else:
               longest = getLonger(longest, item)
     return longest
## problem 6 - apply2nextN 
class apply2nextN(object):
     def __init__(self, op, n, it):
          self.input1 = it
          self.op = op
          self.n = n
          self.current = self.__getNextInput()
     def __getNextInput(self):
          try:
               current = self.input1.__next__()
          except: 
               current = None
          return current
     
     def __next__(self):
          if self.current is None: 
               raise StopIteration
          temp_n = self.n
          total = self.current
          self.current = self.__getNextInput()
          while (temp_n > 1):
               if (self.current is not None):
                    total = self.op(total, self.current)
               else:
                    break
               self.current = self.__getNextInput()
               temp_n -= 1
          return total
     
     def __iter__(self):
          return self
     
