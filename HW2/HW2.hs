-- CptS 355 - Spring 2023 -- Homework2 - Haskell
-- Name: Emma Johnson
-- Collaborators: 
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}

module HW2
     where
import System.Win32 (wAIT_ABANDONED)

{- P1 - remove_every, remove_every_tail  -}

-- (a) remove_every – 7%

{-remove_every n []  = [] 
remove_every n lst = remove_helper n lst n 
  where  
    --needs a case for when the list is empty
     remove_helper 0 (x:xs) k = (remove_helper k xs ) --right here there is an error: remove helper takes 3 parameters but only 2 are fed in here
     remove_helper n (x:xs) k = x:(remove_helper (n-1) xs)  --right here there is an error: remove helper takes 3 parameters but only 2 are fed in here-}
remove_every n []  = [] 
remove_every 0 lst = [] --added a case for when n is zero before needing the recursive solition
remove_every n lst = reverse(remove_helper_tail n lst n [])
  where  
    remove_helper_tail n [] k acc = acc --added a case for when list is empty
    remove_helper_tail 0 (x:xs) k acc = (remove_helper_tail k xs k acc) --added another parameter to remove_helper (fed in k) 
    remove_helper_tail n (x:xs) k acc= (remove_helper_tail (n-1) xs k (x:acc)) --added another parameter to remove_helper (fed in k) 
     
-- (b) remove_every_tail –  10%
remove_every_tail n []  = [] 
remove_every_tail 0 lst = [] --added a case for when n is zero before needing the recursive solition
remove_every_tail n lst = remove_helper n lst n 
  where  
    remove_helper n [] k = [] --added a case for when list is empty
    remove_helper 0 (x:xs) k = (remove_helper k xs k ) --added another parameter to remove_helper (fed in k) 
    remove_helper n (x:xs) k = x:(remove_helper (n-1) xs k) 
------------------------------------------------------
{- P2  get_outof_range and count_outof_range  -}

-- (a) get_outof_range – 6%
{-takes two integer values, v1 and v2,  and a nested list “xs”, 
and returns the total number of values in xs which are less than v1 and greater than v2-}
get_outof_range v1 v2 [] = []
get_outof_range v1 v2 xs = filter (\x-> ((x < v1) `xor` (x > v2))) xs
    where 
        xor :: Bool -> Bool -> Bool  
        xor x y | x == y = False
                | otherwise = True

-- (b) count_outof_range – 10%
count_outof_range v1 v2 [] = 0
count_outof_range v1 v2 xs = foldl (+) 0 (length_out_range xs)
  where length_out_range xs = foldl (\acc x -> (length $ get_outof_range v1 v2 x):acc) [] xs --add component for a nested list- perhaps use foldl and look at your Lab2
         
------------------------------------------------------
{- P3  find_routes - 10% -}
find_routes n [] = []
find_routes n xs = foldl (\acc (x,y) -> if n `elem` y then (x:acc) else acc) [] xs 
  {-where 
      checkRoute n (x,y) | n `elem` y = x
                         | otherwise-}

------------------------------------------------------
{- P4  add_lengths and add_nested_lengths -}
data LengthUnit =  INCH  Int | FOOT  Int | YARD  Int 
                   deriving (Show, Read, Eq) 
-- (a) add_lengths - 6%

add_lengths x y = add_lengths_help x y --fold, then map, then fold like a g, put AString because that is what everything is going to become
     where  

          add_lengths_help (INCH x)(INCH y) = INCH(x + y) 
          add_lengths_help (INCH x)(FOOT y) = INCH(x + (12 * y))
          add_lengths_help (INCH x)(YARD y) = INCH(x + (36 * y))
          add_lengths_help (FOOT x)(FOOT y) = INCH((12 * x) + (12 * y))
          add_lengths_help (FOOT x)(INCH y) = INCH((12 * x) + y)
          add_lengths_help (FOOT x)(YARD y) = INCH((12 * x) + (36 * y))
          add_lengths_help (YARD x)(YARD y) = INCH((36 * x) + (36 * y))
          add_lengths_help (YARD x)(INCH y) = INCH((36 * x) + y)
          add_lengths_help (YARD x)(FOOT y) = INCH((36 * x) + (12 * y))
-- (b) add_nested_lengths - 10%

add_nested_lengths lst = foldr add_lengths_help (INCH 0) (map (foldr add_lengths_help (INCH 0)) lst) --fold, then map, then fold like a g, put AString because that is what everything is going to become
     where  
          add_lengths_help (INCH x)(INCH y) = INCH(x + y) 
          add_lengths_help (INCH x)(FOOT y) = INCH(x + (12 * y))
          add_lengths_help (INCH x)(YARD y) = INCH(x + (36 * y))
          add_lengths_help (FOOT x)(FOOT y) = INCH((12 * x) + (12 * y))
          add_lengths_help (FOOT x)(INCH y) = INCH((12 * x) + y)
          add_lengths_help (FOOT x)(YARD y) = INCH((12 * x) + (36 * y))
          add_lengths_help (YARD x)(YARD y) = INCH((36 * x) + (36 * y))
          add_lengths_help (YARD x)(INCH y) = INCH((36 * x) + y)
          add_lengths_help (YARD x)(FOOT y) = INCH((36 * x) + (12 * y))
------------------------------------------------------
{- P5 sum_tree and create_sumtree -}
data Tree a = NULL | LEAF a | NODE a  (Tree a)  (Tree a)  
              deriving (Show, Read, Eq) 

-- (a) sum_tree - 8%
{-sum_tree  (LEAF v) v
sum_tree (LEAF x) (LEAF y) = x + y
sum_tree (NODE x _ _) (NODE y _ _) = x + y

sum_tree (NODE v t1 t2) = v + (sum_tree t1 t2)-}

sum_tree NULL = 0
sum_tree (LEAF a) = a
sum_tree (NODE a right left) = a + sum_tree right + sum_tree left

-- (b) create_sumtree - 10%

{-  make a copy of the tree -}

create_sumtree NULL = NULL
create_sumtree (LEAF a) = LEAF a
create_sumtree (NODE a left right) = NODE (a + sum_tree left + sum_tree right) (create_sumtree left) (create_sumtree right)
------------------------------------------
{- P6 list_tree - 16% -}
data ListTree a = LEAFs [a] | NODEs [(ListTree a)] 
                  deriving (Show, Read, Eq) 

list_tree funct base (LEAFs xs) = foldl funct base xs
list_tree funct base (NODEs xs) = foldl funct base (map (list_tree funct base) xs)

-- Tree examples - 4%
-- INCLUDE YOUR TREE EXAMPLES HERE
tree1 = (NODE 0 (NODE 6 NULL NULL) (NODE (20) ((NODE (-5) NULL (LEAF (-2)))) (LEAF (8))))
tree2 = (NODE 8 (NODE 6 (NODE 1 (NODE 3 (LEAF 6) NULL) (LEAF 4)) (NODE 6 NULL NULL)) (NODE 8 (NODE 7 (LEAF 5) NULL) (LEAF 9)))
-- Assignment rules 3%