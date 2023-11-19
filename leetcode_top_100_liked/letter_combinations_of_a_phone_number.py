# def letterCombinationsdigits(digits):
#     if not digits:
#         return []

#     letters = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"],
#         "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"],
#         "8":["t","u","v"], "9":["w","x","y","z"]}
#     res = []

#     def backtrack(combination, n_digit):
#         if not n_digit:
#             res.append(combination)
#             return
            
#         for letter in letters[n_digit[0]]:
#             backtrack(combination+letter, n_digit[1:])
                
#     backtrack("", digits)
#     return res

# print(letterCombinationsdigits(input()))


from itertools import product

def letterCombinationsdigits(digits):
    if not digits:
        return []

    letters = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"],
        "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"],
        "8":["t","u","v"], "9":["w","x","y","z"]}
    
    array = [letters[d] for d in digits]
    combinations = product(*array)
    
    return [''.join(combi) for combi in combinations]
    
print(letterCombinationsdigits(input()))