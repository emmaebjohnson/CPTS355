-- CptS 355 - Lab 2 (Haskell) - Spring 2023
-- Name: Emma Johnson
-- Collaborated with: n/a but did look at the Lab2 zoom and talked with Chandler Juego about logic a little

module Lab2
     where
import System.Win32 (COORD(xPos))
import Distribution.Simple.Program.HcPkg (list)

-- 1
{-The function merge2 takes two lists, l1 and l2, and returns a merged list where the elements from l1 
and l2 appear interchangeably.  The resulting list should include the leftovers from the longer list and it 
may include duplicates.  -}
{- (a) merge2 -}
merge2 [] [] = [] --empty case
merge2 lst [] = lst --second list empty, return first
merge2 [] lst = lst --first list empy, retrun the second
merge2 (x:xs) (y:ys) =x:y:merge2 xs ys --place the first value from lst1 and first value from lst2 at the front and continue onward!
                         
{-Re-write the merge2 function from part (a) as a tail-recursive function.  Name your function 
merge2Tail. -}
{- (b) merge2Tail -}

merge2Tail [] [] = [] --empty cases
merge2Tail lst [] = lst --second list empty, return first
merge2Tail [] lst = lst --first list empy, retrun the second
merge2Tail lst lst2 = reverse(merge2Tailhelp lst lst2 []) --call a helper and add an empty lst to put things onto

     where
          merge2Tailhelp [] lst acc = acc ++ lst --add list value into the returned list (add to the back because you're reversing later)
          merge2Tailhelp lst [] acc = acc ++ lst
          merge2Tailhelp (x:xs) (y:ys) acc = reverse(merge2Tailhelp xs ys (y:x:acc)) --none empty? Then recursively call the function while placing the values into the acc list    
                                                                                     --also you will end up reversing so y then x, also reverse the sublist when done


{-Using merge2 function defined above and the foldl function, define mergeN which takes a list of 
lists and returns a new list containing all the elements in sublists. The sublists should be merged left to 
right, i.e., first two lists should be merged first and the merged list should further be merged with the 
third list, etc. Provide an answer using foldl; without using explicit recursion. -}
{- (c) mergeN -}
mergeN[[]] = [] --it is empty
mergeN lst = foldl merge2 [] lst --fold into the sublist and then call your "normal" merge, base case is empty string here 


-- 2
{-Define a function count which takes a value and a list as input and it count the number of occurrences 
of the value in the input list.  Your function should not need a recursion but should use a higher order 
function (map, foldr/foldl, or filter). Your helper functions should not be recursive as well, but 
they can use higher order functions. You may use the length function in your implementation. -}
{- (a) count -}
count n [] = 0 --empty means there's nothing to count >:)
count n xs = length $ filter (\x -> x == n) xs --get the length while also filtering the list to only return the values of n found
 
{-The function histogram creates a histogram for a given list. The histogram will be a list of tuples 
(pairs) where the first element in each tuple is an item from the input list and the second element is the 
number of occurrences of that item in the list.  Your function shouldn’t need a recursion but should use 
a higher order function (map, foldr/foldl, or filter). Your helper functions should not be 
recursive as well, but they can use higher order functions. You may use the count function you defined 
in part (a) and eliminateDuplicates function you defined in HW1. 
 -}
{- (b) histogram  -}

--histogram :: [a1] -> [([a1] -> a2 -> Bool, Int)]
 
histogram [] = [] --empty case
histogram xs = eliminateDuplicates ( map (\x -> (x, count x xs)) xs) --using elimate duplicates, for every value of x map it to a tuple broski
     where    
          eliminateDuplicates xs = foldr helper [] xs 
                 where helper x base | (x `elem` base ) =  base
                                     | otherwise = x:base

-- 3     
{-Function concatAll is given a nested list of strings and it returns the concatenation of all 
strings in all sublists of the input list. Your function should not need a recursion but should use functions 
“map” and “foldr”. You may define additional helper functions which are not recursive. -}           
{- (a) concatAll -}

concatAll [[]] = []-- empty tuple return empty string
concatAll lst = help ( map help lst) --map that bish to get the sublists >:)
     where   
       help xs = foldr (++) [] xs -- concat it together !!

{-Define a Haskell function concat2Either that takes a nested list of AnEither values and it returns 
an AString, which is the concatenation of all values  in all sublists of the input list. The parameter of 
the AnInt values should be converted to string and included in the concatenated string. You may use 
the show function to convert an integer value to a string.  -}
{- (b) concat2Either -}               
data AnEither  = AString String | AnInt Int
               deriving (Show, Read, Eq)


concat2Either:: [[AnEither]] -> AnEither 
concat2Either lst = foldr eitherconcat (AString "") (map (foldr eitherconcat (AString "")) lst) --fold, then map, then fold like a g, put AString because that is what everything is going to become
     where  

          eitherconcat (AString x)(AnInt y)  = AString (x ++ (show y)) --concat, but if its an int turn it into a string w show
          eitherconcat (AnInt x )(AString y) = AString ((show x) ++ y)
          eitherconcat (AString x)(AString y) = AString (x ++ y)
          eitherconcat (AnInt x)(AnInt y) =  AString (show(x + y))
-- 4      
{-Re-define your concat2Either function so that it returns a concatenated string value instead of an 
AString value. Similar to concat2Either, the parameter of the AnInt values should be converted 
to string and included in the concatenated string.  
 -}
{-  concat2Str -}               

concat2Str lst = foldr (++) "" (map concat_help lst)
     where  
          concat_help xs = foldr eitherconcat2str "" xs --fold the lsit to get the values in sublist

          eitherconcat2str (AString x) y  = x ++ y --concat w string from AString
          eitherconcat2str (AnInt x ) y = show x ++ y --concat w string from AnInt (remember to use show to turn it into a string to concat)
        



data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)

evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub   x y = x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y

data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)

-- 5 
{- evaluateTree -}



-- 6
{- printInfix -}



--7
{- createRTree -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)






