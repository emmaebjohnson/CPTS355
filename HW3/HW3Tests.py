#------------------------------------------------------
#-- INCLUDE YOUR OWN TESTS IN THIS FILE
#------------------------------------------------------
import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    def setUp(self):
        self.log_input = {'CptS355': {'Mon': 4, 'Wed': 4, 'Sat': 4, 'Sun': 4}, 
                          'CptS317': {'Mon': 4, 'Tue': 4, 'Wed': 4, 'Fri': 4, 'Thu': 4}}
        
    
    def sort_values(self,d):
        return dict(map(lambda t: (t[0],list(sorted(t[1]))), d.items()))
    #--- Problem 1(a)----------------------------------
    

    def test_aggregate_log1(self):
        log_input = {'CptS355':{'Mon':3,'Wed':2,'Sat':2},
                     'CptS360':{'Mon':3,'Tue':2,'Wed':2,'Fri':10}}
        output = {'Fri': 10, 'Mon': 6, 'Sat': 2, 'Tue': 2, 'Wed': 4}
        self.assertDictEqual(aggregate_log(log_input),output)

    def test_aggregate_log2(self):
        log_input = {}
        output = {}
        self.assertDictEqual(aggregate_log(log_input),output)
        # Provide your own test here. Create your own input dictionary for this test.
    
    #--- Problem 1(b)----------------------------------
    def test_combine_dict1(self):
        log1 = {'Mon':3}
        log2 = {'Tue':2}
        output = {'Mon': 3, 'Tue': 2}
        self.assertDictEqual(combine_dict(log1,log2),output)
        #make sure input dictionaries are not changed. 
        self.assertDictEqual(log1, {'Mon':3})
        self.assertDictEqual(log2, {'Tue':2})
    
    def test_combine_dict2(self):
        log1 = {}
        log2 = {'Tue':2}
        output = {'Tue': 2}
        self.assertDictEqual(combine_dict(log1,log2),output)
        #make sure input dictionaries are not changed. 
        self.assertDictEqual(log1, {})
        self.assertDictEqual(log2, {'Tue':2})
        # Provide your own test here. Create your own input dictionary for this test .
        # You can re-use the data dictionary you created for problem-1.
    def test_combine_dict3(self):
        log1 = {'Mon':3}
        log2 = {}
        output = {'Mon': 3}
        self.assertDictEqual(combine_dict(log1,log2),output)
        #make sure input dictionaries are not changed. 
        self.assertDictEqual(log1, {'Mon':3})
        self.assertDictEqual(log2, {})

    #--- Problem 1(c) ----------------------------------
    def test_merge_logs1(self):
        log_list_backup = [{'CptS355':{'Mon':3,'Wed':2,'Sat':2},'CptS355':{'Sun':8}}]
        log_list = [{'CptS355':{'Mon':3,'Wed':2,'Sat':2},'CptS355':{'Sun':8}}]
        output = {'CptS355': {'Mon': 3, 'Wed': 2, 'Sat': 2, 'Sun': 8}}
        self.assertListEqual(log_list,log_list_backup)

    def test_merge_logs2(self):
        log_list_backup = [{}]
        log_list = [{}]
        output = {}
        self.assertListEqual(log_list,log_list_backup)
        # Provide your own test here. Create your own input dictionary for this test .
        # You can re-use the data dictionary you created for problem-1.

    #--- Problem 2(a)----------------------------------
    def test_most_hours1(self):
        output = ('CptS317', 20)
        self.assertTupleEqual(most_hours(self.log_input),output)
    
    def test_most_hours2(self):
        test_input = {'CptS355': {'Mon': 12}}
        output = ('CptS355', 12)
        self.assertTupleEqual(most_hours(test_input),output)
        # Provide your own test here. Create your own input dictionary for this test 
            
    #--- Problem 2(b) ----------------------------------
    def test_filter_log1(self):
        log_input = {'CptS355': {'Mon': 4, 'Wed': 4, 'Sat': 4}, 
                          'CptS317': {'Mon': 4, 'Tue': 4, 'Wed': 4, 'Fri': 4, 'Thu': 4}}
        output = sorted([])
        self.assertListEqual(sorted(filter_log(log_input,"Sun", 3)),output)

    def test_filter_log2(self):
        log_input = {'CptS355': {'Mon': 4, 'Wed': 4, 'Sat': 4}, 
                          'CptS317': {'Mon': 6, 'Tue': 4, 'Wed': 4, 'Fri': 4, 'Thu': 4}}
        output = sorted(['CptS317'])
        self.assertListEqual(sorted(filter_log(log_input,"Mon", 6)),output)
        # Provide your own test here. Create your own input dictionary for this test 

    #--- Problem 3----------------------------------
    def test_graph_cycle1(self):
        graph = {'A':('B',5),'B':('C',3),'C':('D',10)}
        self.assertEqual(graph_cycle(graph,'A'), None)

    def test_graph_cycle2(self):
        graph = {'A':('B',5),'B':('C',3),'C':('D',10), 'D': ('B', 4)}
        self.assertEqual(graph_cycle(graph,'A'), ['B', 'C', 'D', 'B'])
        # Provide your own test here.   Create your own input graph for this test 

    #--- Problem 4----------------------------------
    def test_filter_iter1(self):
        it = iter([-1,-3,4,5,3,-2,0,3,2,-1])
        expected_output = [-1,-3,-2,-1]
        actual_output = list(filter_iter(it, lambda x: x<0))  #convert the iterator output to list
        self.assertListEqual(actual_output, expected_output)

    def test_filter_iter2(self):
        it = iter([])
        expected_output = []
        actual_output = list(filter_iter(it, lambda x: x<0))  #convert the iterator output to list
        self.assertListEqual(actual_output, expected_output)
        # Provide your own test here. Initialize the iterator with your own input.

    #--- Problem 5----------------------------------
    def test_merge1(self):
        class Numbers():
            def __init__(self,init):
                self.current = init
            def __next__(self):
                result = self.current
                self.current += 1
                return result
            def __iter__(self):
                return self

        class Letters():
            def __init__(self,init):
                self.current = init
            def __next__(self):
                result = self.current
                self.current = chr(ord(self.current)+1)
                return result
            def __iter__(self):
                return self
    
        it1 = filter_iter(Numbers(10), lambda x: x>0 and x%2==0)
        it2 = filter_iter(Numbers(0), lambda x: x%4==0)
        
        # first call to merge
        self.assertListEqual(merge(it1,it2, 10), [0, 4, 8, 10, 12, 12, 14, 16, 16, 18])
       
        # Provide your own test here.
    def test_merge2(self):
        class Numbers():
            def __init__(self,init):
                self.current = init
            def __next__(self):
                result = self.current
                self.current += 1
                return result
            def __iter__(self):
                return self

        class Letters():
            def __init__(self,init):
                self.current = init
            def __next__(self):
                result = self.current
                self.current = chr(ord(self.current)+1)
                return result
            def __iter__(self):
                return self
    
        it1 = filter_iter(Numbers(0), lambda x: x>0)
        it2 = filter_iter(Numbers(0), lambda x: x>0)
        
        # first call to merge
        self.assertListEqual(merge(it1,it2, 10), [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
        # Provide your own test here.
        

if __name__ == '__main__':
    unittest.main()

