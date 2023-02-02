-- CptS 355 - Lab 1 (Haskell) - Spring 2023
-- Resources Used: Shakire Lab 1 Zoom Call (went over similar problems and ways to approach problems)
-- Name: Emma Johnson

{-# OPTIONS_GHC -Wno-overlapping-patterns #-}


module Lab1
     where


-- 1.insert 
--takes an integer “n”, a value “item”, and a list “iL” and inserts the 
--item at index “n” in the list “iL”

insert 0 item [] = [item] --when index is zero and the string is empty, insert the item at the end of the string
insert n item [] = [] --when the index is greater than the length of the string, return empty string
insert n item (x:xs) | n == 0 =  item:x:xs --if the index is zero, insert in the location in the string you are in
                     | otherwise = x:insert (n-1) item xs --continue to move down the string, decrementing the index
                     
-- 2. insertEvery
--takes an integer “n”, a value “item”, and a list “iL” and inserts 
--the “item” at every nth index in “iL”

insertEvery :: (Eq t, Num t) => t -> a -> [a] -> [a]
insertEvery 0 item [] = [item] --base case, when n is zero and list is empty, insert at end of string
insertEvery n item [] = []--when the index is greater than the length of the string, return empty string
insertEvery n item (x:xs) = inserthelp n item n (x:xs) --call insert help but and set a counter "k" to the n-value
     where
          inserthelp 0 item k [] = [item] --if index is zero 
          inserthelp n item k [] = []
          inserthelp 0 item k (x:xs) = item:x:inserthelp (k-1) item k xs 
          inserthelp n item k (x:xs) = x:inserthelp (n-1) item k xs 


-- 3. getSales
--Write a function insert that takes an integer “n”, a value “item”, and a list “iL” and inserts the 
--item” at index “n” in the list “iL”

getSales :: (Num p, Eq t) => t -> [(t, p)] -> p 
getSales d [] = 0
getSales d ((day, amount):xs) | day == d = amount + getSales d xs
                              | otherwise = getSales d xs

                                                  
-- 4. sumSales
--Write a function, sumSales, that takes a store name, a day-of-week, and a sales log list (similar to 
--sales”) and returns the total sales of that store on that day-of-week.  

sumSales s d [] = 0
sumSales s d ((store,log):xs) | store == s = getSales d log + sumSales s d xs
                              | otherwise = sumSales s d xs
-- 5. split
--that takes a delimiter value “c” and a list “iL”, and it splits the input list with 
--respect to the delimiter “c”. 

split c lst = splithelp c lst
    
     where
          splithelp c [] buf | (buf == []) = []
                             |otherwise = (reverse buf):[]
          splithelp c (x:xs) buf | c == x = (reverse buf):(splithelp c xs [])
                                  | otherwise = splithelp c xs (x:buf)

                                  

-- 6. nSplit
-- takes a delimiter value “c”, an integer “n”,  and a list “iL”, and it splits 
--the input list with respect to the delimiter “c” up to “n” times. Unlike split, it should not split the 
--input list at every delimiter occurrence, but only for the first “n” occurrences of it. 
nSplit c n lst = nsplithelper c n lst []
     where     
          nsplithelper c n [] buf | buf == [] = []
                                  |otherwise = reverse buf:[]
          nsplithelper c n (x:xs) buf | c == x && n > 0 = reverse buf: nsplithelper c (n-1) xs [] 
                                   | c/= x && n > 0 = nsplithelper c n xs (x:buf)
                                   | otherwise = (x:xs):[]
