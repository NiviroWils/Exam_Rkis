from random import randint
arr = [randint(-100, 100) for i in range(20)] # для примера а так по условию массив уже дан
#################################################################
 
def add_condition():
     len_arr = len(arr)
     positive = len(list(filter(lambda x : x > 0, arr)))
     negative = len_arr - positive
     factor = 1
     if positive > negative:
          factor = -1
     for _ in range( abs(positive - negative)):
          arr.append( randint(0, 100)*factor)
           
 
print(arr)
add_condition()
print(arr)