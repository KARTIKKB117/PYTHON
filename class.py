class employee :
    language = 'py'   # this is class attribute 
    salary = 1000
    
harry = employee()
harry.name = 'harry' # this is object attribute 
print(harry.name ,harry.language, harry.salary)
    
rohan = employee()
rohan.name = 'rohan'
print(rohan.name ,rohan.language, rohan.salary)
