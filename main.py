# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(name:str) -> str:
   message = "Hello, " + name + "."

   return message


message = welcome_message("griffindoeff@calpoly.edu")
print(message)

def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated? → when n (first value) is less than m (second value)
    else:
        return m
first = smallest(3, 2)       # What is the value of first? → 2
second = smallest(2, 2)      # What is the value of second? Is this a reasonable result? Why or why not? → → 2, which is reasonable because the code will return m as long as n </ m, not necessarily if n > m
print(first, second)

def function2(a:int, b:int, c:int) -> int:
   if a > b and a > c:
       return a - b             # In general, when will a call to this function evaluate this statement? → when a is the largest inputted value
   elif b > c:
       return b + c             # In general, when will a call to this function evaluate this statement? → when b is the largest inputted value
   else:
       return 2 * c             # In general, when will a call to this function evaluate this statement? → when c is the largest inputted value
answer1 = function2(3, 2, 1)     # What is the value of answer1? → 1
answer2 = function2(2, 3, 1)     # What is the value of answer2? → 4
answer3 = function2(2, 1, 3)     # What is the value of answer3? → 6
print(answer1, answer2, answer3)

def checked_access(L:list[int], idx:int) -> Optional[int]:
   test = idx >= 0 and idx < len(L)    # What is the value of test on each call? → → False (first), True (second)
   if test:                            # What is this check preventing? → Checking that the index is not negative and is less than the total length (ie will be able to run without error)
       return L[idx]
   else:
       return None
first = checked_access([1, 0, 1], 9)     # What is the value of first? → None
second = checked_access([1, 0, 1], 2)    # What is the value of second? → 1
print(first, second)

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated → if len(L) > 2…result = len(L[0]) + len(L[1]) + len(L[2])
    elif len(L) > 1:                                  #   and what are the values being added? → → the total number of characters in "this" (4), "is" (2), and "the" (3)
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated → → elif len(L) > 1…result = len(L[0]) + len(L[1])
    elif len(L) > 0:                                  #   and what are the values being added? → → the total number of characters in “another call” (11)
        result = len(L[0])                            # For which call below is this statement evaluated → elif len(L) > 0…result = len(L[0])
    else:                                             # and what are the values being added? → → the total number of characters in "another" (7)
        result = 0
    return result
first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first, second, third)

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L




words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? → 'this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.'
         # What are the values of first and second at this point? → 'this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.'
         # What happened? → the L being returned by the function is always the original list, with whatever subsequent append modifications
print(words, first, second)
