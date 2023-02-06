{- Example of using the HUnit unit test framework.  See  http://hackage.haskell.org/package/HUnit for additional documentation.
To run the tests type "run" at the Haskell prompt.  -} 

module HW1Tests
    where

import Test.HUnit
import Data.Char
import Data.List (sort)
import HW1

-- P1(a) count tests  

--empty string test
p1a_test4 = TestCase (assertEqual "count-test4"
                                 0
                                 (count '2' []) )
--character string test
p1a_test5 = TestCase (assertEqual "count-test5"
                                3
                                (count 'a' "Emmaaah") )

-- P1(b) diff tests

--if both strings are empty
{-p1b_test4 = TestCase (assertEqual "diff-test4"
                                []
                               (sort $ diff [] []) )-}
--if string 1 is empty
p1b_test5 = TestCase (assertEqual "diff-test5"
                                 []
                                 (sort $ diff [] [1,2,2,3,3,3,6,7,4,4,4,4,5,5,5,5,5,6,6]) )
--if string 2 is empty
p1b_test6 = TestCase (assertEqual "diff-test6"
                                 [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,7]
                                 (sort $ diff [6,2,2,3,5,3,6,7,4,4,5,4,5,5,4,5,3,1,6] []) )
                               


-- P1(c) bag_diff tests

--test first is empty string
p1c_test5 = TestCase (assertEqual "bag_diff-test5"
                                 (sort [] )
                                 (sort $ bag_diff [] [1,2,3,4]) )
--test if 2nd is empty string
p1c_test6 = TestCase (assertEqual "bag_diff-test6"
                                 (sort [2,3,4,5,6] )
                                 (sort $ bag_diff [2,3,4,5,6] []) )
--string test
p1c_test7 = TestCase (assertEqual "bag_diff-test7"
                                 (sort"my name is emma" )
                                 (sort $ bag_diff "my name is emma" "") )
--empty string test
p1c_test8 = TestCase (assertEqual "bag_diff-test8"
                                 (sort"" )
                                 (sort $ bag_diff "" "test test") )

-- P2  everyN tests
--every 0 for a string
p2_test5 = TestCase (assertEqual "everyN-test5"
                                  ""
                                  (everyN "haskell" 0) )
--every 0 for a list
p2_test6 = TestCase (assertEqual "everyN-test6"
                                  []
                                  (everyN [1,2,3,4,5,6] 0) )
-- P3(a) make_sparse tests
--every index has a value
p3a_test5 = TestCase (assertEqual "make_sparse-test5"
                                  [1,2,3,4,5]
                                  (make_sparse [(0,1),(1,2),(2,3),(3,4),(4,5)]) )
--negative numbers to sparse
p3a_test6 = TestCase (assertEqual "make_sparse-test6"
                                  [0,0,0,-4,5]
                                  (make_sparse [(3,-4),(4,5)]) )
              
-- P3(b) compress tests
--compress every index 
p3b_test5 = TestCase (assertEqual "compress-test5"
                                  [(0,1),(1,2),(2,3),(3,4),(4,5)]
                                  (compress [1,2,3,4,5]) )
--compress with negatives
p3b_test6 = TestCase (assertEqual "compress-test6"
                                  [(3,-4),(4,5)]
                                  (compress  [0,0,0,-4,5]) )

-- P4 added_sums tests
--added sum with one value
p4_test4 = TestCase (assertEqual "added_sums-test4"
                                  ([1])
                                  (added_sums [1]) )
--added su with all zeros
p4_test5 = TestCase (assertEqual "added_sums-test5"
                                  ([0, 0, 0, 0, 0, 0])
                                  (added_sums [0, 0, 0, 0, 0, 0]) )

-- P5 find_routes tests
routes_test = [("Lentil",["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"]), 
   ("Wheat",["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"]), 
   ("Silver",["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Outlet", "RockeyWay","Main"]),
   ("Blue",["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"]),
   ("Gray",["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]),
   ("Coffee",["TransferStation", "Grand", "Main", "Visitor","Stadium", "Spark", "CUB"])]    


-- find_routes tests
--no route given, nothing returned
p5_test4 = TestCase (assertEqual "find_routes-test4"
                                  (sort [])
                                  (sort $ find_routes "" routes_test ) )
--route name given instead of stop name
p5_test5 = TestCase (assertEqual "find_routes-test5"
                                  (sort [])
                                  (sort $ find_routes "Coffee" routes_test ) )                                  

-- P6 group_sum tests
--test with negative numbers and a sum of 0
p6_test4 = TestCase (assertEqual "(group_sum-test4)"
                                  [[-2,-3]]
                                  (group_sum [-2,-3] 0) )
--test with en empty list                                  
p6_test5 = TestCase (assertEqual "(group_sum-test5)"
                                  []
                                  (group_sum [] 4) )

-- add the test cases you created to the below list. 
tests = TestList [ --tests for 1a
                    TestLabel "Problem 1a- test4 " p1a_test4,
                    TestLabel "Problem 1a- test5 " p1a_test5,

                  --tests for 1b
                    --TestLabel "Problem 1b- test4 " p1b_test4, --wack, so it has been jailed as a comment
                    TestLabel "Problem 1b- test5 " p1b_test5,
                    TestLabel "Problem 1b- test6 " p1b_test6,

                   --tests for 1c
                   TestLabel "Problem 1c- test5 " p1c_test5,
                   TestLabel "Problem 1c- test6 " p1c_test6,
                   TestLabel "Problem 1c- test7 " p1c_test7,
                   TestLabel "Problem 1c- test8 " p1c_test8,

                  --tests for 2
                   TestLabel "Problem 2- test5 " p2_test5,
                   TestLabel "Problem 2- test6 " p2_test6,
                 
                  --tests for 3a
                   TestLabel "Problem 3a- test5 " p3a_test5,
                   TestLabel "Problem 3a- test6 " p3a_test6,
                
                  --tests for 3b
                   TestLabel "Problem 3b- test5 " p3b_test5,
                   TestLabel "Problem 3b- test6 " p3b_test6, 

                  --tests for 4
                   TestLabel "Problem 4- test4 " p4_test4,
                   TestLabel "Problem 4- test5 " p4_test5,

                   --tests for 5
                   TestLabel "Problem 5- test4 " p5_test4,
                   TestLabel "Problem 5- test5 " p5_test5,
                  
                  --tests for 5
                   TestLabel "Problem 6- test4 " p6_test4,
                   TestLabel "Problem 6- test5 " p6_test5

                 ]
                  
-- shortcut to run the tests
run = runTestTT  tests