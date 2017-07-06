import numpy
p,q,r=map(int,input().split())

arr1 = []
arr2 = []
for i in range(p):
    tmp = list(map(int,input().split()))
    arr1.append(tmp)
for i in range(q):
    tmp = list(map(int,input().split()))
    arr2.append(tmp)    
np_arr1 = numpy.array(arr1)
np_arr2 = numpy.array(arr2)
print(numpy.concatenate((np_arr1,np_arr2),axis = 0))
