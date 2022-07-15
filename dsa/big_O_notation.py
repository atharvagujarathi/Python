# asymptotic behaviour of a function ---> how fast a function f(n) as a n becomes large.
# f(n) is O(g(n)) if there a exists c and n0 such that
# f(n) <= c g(n) for all n >= n0
# 
# functions which is used in upper bound - 
#  slow growing to fast growing -

# g(n)

#  1
#  log n
#  n
#  n log n
#  n2(square)
#  n3(cube)
#  n rest to k
#  2 rest to n
#  3 rest to n
#  k rest to n
#  n!


# HOW TO FIND THE big-O?
# for example - 
#  3n2 + 4n + 15
#  consider n = 10
#  so its a , 300 + 40 + 15
#  hence the contribution of 300 is
#   300 / (300 + 40 + 15) * 100 = 84.50%
#  the contribution of 20 is
#   20 / (300 + 40 + 15) * 100 = 11.26%
#  the contribution of 15 is
#   15 / (300 + 40 + 15) * 100 = 4.22%
#  hence the fastest growing term becomes dominent and smallest term and constants becomes insignificant.


#  **RULE 1 = keep the fastest growing term becomes dominent and discard the lower term and constants.
#  **RULE 2 = Ignore coefficient
#               f(n) = c * g(n)
#               f(n) is O(g(n))
# for example  f(n) = 5n2 , hence ignore 5 
#               f(n) is O(n2)
#  **RULE 3 = If f(n) = c , then we can say that f(n) O(1).
#               for example = f(n) = 3
#                             f(n) = O(1).
#  **RULE 4 = Base of logarithm is not important.
#                for example = f(n) = 8log2n = f(n) is O(logn).



# big-O analysis of an algorithm(TIME COMPLEXITY) = 
#  **RULE 1 = express the running time as function of input size(n).
#  **RULE 2 = Find big-O for function T(n).
#  * and / T(n) becomes log n