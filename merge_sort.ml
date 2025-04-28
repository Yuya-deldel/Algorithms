(* merge_sort: list, list -> list *)
let rec merge list1 list2 = match (list1, list2) with 
    ([], []) -> []
    | (first1 :: rest1, []) -> list1 
    | ([], first2 :: rest2) -> list2 
    | (first1 :: rest1, first2 :: rest2) ->
        if first1 < first2 then 
            first1 :: (merge rest1 list2)
        else
            first2 :: (merge list1 rest2)

(* test *)
let test0 = merge [] [] = []
let test1 = merge [] [1] = [1]
let test2 = merge [1] [] = [1]
let test3 = merge [1; 3; 5] [0; 2; 4] = [0; 1; 2; 3; 4; 5]