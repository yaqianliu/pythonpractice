from numpy import *
a = arange(18).reshape(3,6)
a
a.shape
a.ndim

b = array([2, 4, 6])
c = array([((1.5,4,8), (2,8,8), (3,6,8)),((1.5,4,8), (2,8,8), (3,6,8)),((1.5,4,8), (2,8,8), (3,6,8))])
d = array([((1.5,4,8), (2,8,8), (3,6,8)),(1.5,4,8), (2,8,8), (3,6,8)])
e = array([(((1,1,1),(2,2,2),(3,3,3)),((1,1,1),(2,2,2),(3,3,3)),((1,1,1),(2,2,2),(3,3,3)),((1,1,1),(2,2,2),(3,3,3)))],dtype = complex)

f = zeros((3, 4))
g = ones((2, 4,3),dtype = float64)
h = empty((2, 4, 3))
i = arange(2,3,0.2)#起点，终点，幅度，然后是不包括终点的，如果只有一个参数，默认从零开始，幅度是

j = array(((2,0),(4,0)))
k = array(((0,3),(0,5)))
j*k
dot(j,k)

m = array([[9.9966861076827107e-001, 8.7103817381015327e-003,
 2.4223911629038551e-002],[ -1.3481620898438634e-002,
 9.7879357391115906e-001, 2.0440495485230101e-001],
 [-2.1929763851571783e-002, -2.0466379484461092e-001,
 9.7858664232515324e-001]],dtype = complex)
n = linspace(0,pi,3)
o = ones(3,dtype = int32)
p = n + o
q = exp(c*1j)

r = arange(12).reshape(3,4)
r.sum(axis = 0) # the sum in col
r.sum(axis = 1) #the sum in row
r.cumsum(axis = 0) #cumulative sum in col


#ufunc means unity func exp.sqrt
i = arange(10)**3
a[:6:2] = 1000 #2 means skip one every number


#slice
def f(x,y):
         return x**2 + y
qaq = fromfunction(f,(3,3),dtype = int)


# change array shape hastack hsplit
a = floor(10*random.random((3,4)))#return random floats from 0-1
a.ravel()
a.shape=(2,6)
a.resize(6,2)

#stack
vstack((a,b))# vertical
x = array([4,2])
x = column_stack([:,newaxis])
# hstack((a,b)) horizon
column_stack((a,b))
#hsplit
win =floor(15*random.random((2,12)))
win
win2 = hsplit(win,3)
win2
win3 = hsplit(win,(3,4))

huge = eye(4,k=1)
huge

# incidence  by array
ab = arange(12)**2
i = ([5,4,1,9,2])



