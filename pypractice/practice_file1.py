## write your program here!

time = input('Enter tuple numbers:')
times = int(time)
while times >= 1:
    name = input('Enter　name:')  #strip removes the \n
    age = input('Enter age:')
    weight = input('Enter weight:')
    myTuple = (name, age, weight)
    times = times - 1

b = sorted(myTuple,key =lambda x: (x[0], x[1], x[2]))
print (b)
