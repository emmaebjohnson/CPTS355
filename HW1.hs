-- CptS 355 - Spring 2023 -- Homework1 - Haskell
-- Name:Emma Johnson
-- Collaborators: Function definition comments are taken from "CPTS355_Assignment1_Haskell1.pdf"
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}

module HW1
     where
import Control.Monad (when)
import Distribution.Compat.Lens (_1)

-- P1(a) count ;  6%
{-function count which takes a value and a list and returns the number of occurrences of that value 
in the input list. -}

count v [] = 0 --if list is empty return 0
count v (x:xs) | v == x = 1 + count v xs --if value is equal to the value up first in the list, add one to the total count
               | otherwise = count v xs --if value is not equal then move along the list 
 
-- P1(b) diff ;  6%
{-function diff that takes two lists as input and returns the difference of the first list with respect 
to the second.  The input lists may have duplicate elements. If an element in the first list also appears in the 
second one, the element – and its duplicate copies – should be excluded in the output.-}
diff [] ys = []
diff xs [] = xs
diff (x:xs) ys | 0 == count x ys = x:diff xs ys
               | otherwise = diff xs ys

    where
        count v [] = 0 --if list is empty return 0
        count v (x:xs) | v == x = 1 + count v xs --if value is equal to the value up first in the list, add one to the total count
                       | otherwise = count v xs --if value is not equal then move along the list 
 

-- P1(c) bag_diff ; 8%
{- function diff that takes two lists as input and returns the difference of the first list with respect 
to the second. The input lists may have duplicate elements. If an element appears in both lists and if the 
number of duplicate copies of the element is bigger in the first list, then this element should appear in the 
result as many times as the difference of the number of occurrences in the input lists. -}
-- for this solution, I talked through the logic with another student, Doug Takada, and then we each came up with solutions

bag_diff [] ys = [] --if the first list is empty, the result is empty
bag_diff xs [] = xs --if the second list is empty, the result is the first list
bag_diff (x:xs) l2 | 0 == count x l2 = x:bag_diff xs l2 --if count is zero then they have nothing in common and you can include x in the result
                   | 1 + count x xs > count x l2 = x : bag_diff xs l2 --if there are more values of x in list1, then add x to the result
                   | otherwise = bag_diff xs l2 -- if there is an equal or greater number of x in list2, then you have to keep on trucking through

-- P2  everyN ; 10%
{-The function everyN takes a list and a number ‘n’ (representing a count) and returns every nth value in 
the input list.-}

everyN lst n = helpn (n-1) n lst --call insert help but and set a counter "k" to the n-value
    
     where
        helpn 0 k [] = [] -- if you return every 0 then you are not returning anything >:-)
        helpn n k [] = [] --empty list is just empty list OMG!
        helpn 0 k (x:xs) = x:helpn (k-1) k xs --if the n is zero then you return a value and reset the n back to normal
        helpn n k (x:xs) = helpn (n-1) k xs --continue to increment until n is zero

   

{-A sparse vector is a vector having a relatively small number of nonzero elements. When a sparse vector is 
saved, it is typically put in storage without its zero elements. A possible solution for storing sparse vector is 
compressing it as a list of tuples where the tuples store the indices and values for non-zero elements-}
-- P3(a) make_sparse ; 15%
{-Write a function make_sparse which takes a compressed  vector value (represented as a Haskell list of 
tuples)  and returns the equivalent sparse vector (including all 0 values). -}

make_sparse [] = [] --its empty
make_sparse lst = sillysparse lst 0 --its not empty! Call Sillysparse
    where
        sillsparse [] _ = [] --silly its empty
        sillysparse ((x,y):xs) n |n == x && null xs = [y] --If this is the last (x,y) combo and it is add index you can just add y  
                                 |n == x = y:sillysparse xs (n+1) --at index, insert y and move on
                                 |otherwise = 0:sillysparse ((x,y):xs) (n+1) --moving forward toward index

-- P3(b) compress ; 15%
{-Write a function compress which takes a sparse vector value (represented as a Haskell list)  and returns 
the equivalent compressed values as a list of tuples.-}

compress [] = [] --its empty
compress lst = compresshelp lst 0 --call compress help
    where
     compresshelp [] _ = [] --if empty then its empty
     compresshelp (x:xs) k | x == 0 = compresshelp xs (k+1) -- if x is zero, move on and increment the index
                           | otherwise = (k,x):compresshelp xs (k+1) --if x is not zero, create a tuple of it and the index and move on
-- P4 added_sums ; 8%
{-Write a function added_sums that takes a list of numbers and returns a list including the cumulative 
partial sums of these numbers. -}


added_sums [] = [] -- empty case
added_sums (x:xs) = x:helpsums x xs --call helper function and place x at the beginning

    where
        helpsums x [] = [] --if emtpty
        helpsums x (y:ys) = (x+y):helpsums (x+y) ys -- add the sum to the beginning and increment through
        
    -- P5 find_routes ; 8%
{-function find_routes that takes the list of bus routes and  a stop name, and returns the list of the 
bus routes which stop at the given bus stop.   -}

find_routes n [] = [] --empty
find_routes n ((x, y):xs) | n `elem` y = x:find_routes n xs --is n in y? if yes then put the route name and keep truckin (bussin?)
                          | otherwise = find_routes n xs --if n is not in y, keep looking through the list


-- P6 group_sum ; 15% 
{-this one is hard to explain honestly-}
{- basically create sublists named values 1 through k and the subcontents sum up to or less than n*2^k-}

group_sum [] n = [] --empty case
group_sum lst n = sumhelp 0 lst n 0 [] --call sumhelp so you can add a counter and a buf
   
    where
        sumhelp sum [] n k [] = [] --if both list and buf is empty, return empty
        sumhelp sum [] n k buf = [reverse buf] --if its the end of the list (or if its just empty), print out the last buf
        sumhelp sum (x:xs) n k buf |(sum + x) > (n*(2^k)) = reverse buf:sumhelp 0 (x:xs) n (k+1) [] --check to see if the next x belongs in the current buf, if it is larger, then return the buf and start a new one
                                   | otherwise = sumhelp (sum + x) xs n k (x:buf) --if x belongs in the buf, add it and increase the sum to include it
                      

-- Assignment rules ; 3%
-- Your own tests; please add your tests to the HW1Tests.hs file ; 6%


