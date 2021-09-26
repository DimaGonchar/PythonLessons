def countWord(arr):
    count=0
    for i in range(len(arr)):
        if type(arr[i]) != int and "two" in arr[i]:
           count+=1
        else:
          continue
    return count     

my_arr = ["one, two", 1, 2,3]
print(countWord(my_arr))

def multiplication(lst):
  multi=1
  for product in lst:
        multi*=product
  return multi

print(multiplication(my_arr))