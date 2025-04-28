(* quick_sort : 分割統治法 *)
(* int list -> int list *)
let rec take_less n list_ = match list_ with 
    [] -> []
    | first :: rest ->
        if first <= n then 
            first :: take_less n rest
        else
            take_less n rest 

let rec take_greater n list_ = match list_ with 
    [] -> []
    | first :: rest -> 
        if first >= n then 
            first :: take_greater n rest 
        else
            take_greater n rest

let rec quick_sort list_ = match list_ with 
    [] -> []
    | first :: rest -> 
        quick_sort (take_less first rest) @ [first] @ quick_sort (take_greater first rest)


(* test *)
let test0 = quick_sort [] = []
let test1 = quick_sort [5; 4; 9; 8; 2; 3] = [2; 3; 4; 5; 8; 9]