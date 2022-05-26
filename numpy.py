import numpy as np

list1 = [1,2,3]
# np1 = np.array(list1)
# np2 = np.array([1.0, 2, 3])
# np3 = np.array(range(1, 4))
# np4 = np.array([range(x,x+3) for x in [2 , 4, 6]])

# np5 = np.zeros(10, dtype=np.int)
# np6 = np.ones((3,5), dtype=np.int)
# np7 = np.full((3,5), 255)
# np8 = np.arange(0, 20, 2)
# np9 = np.linspace(0, 1,5)
# np10 = np.random.random((3,3))
# np11 = np.random.randint(0,6,(3,3))
# np12 = np.random.normal(0,1,(3,3))
# np13 = np.eye(7)
# np14 = np.empty(7)

list1 = [1,2,3,4,5,6,7]
list2 = list1[1:4]
print(list2)
list2[0] = 100
print(list1)

np1 = np.array([1, 2, 3, 4, 5, 6, 7])
np2 = np1[1:4]
print(np2)
np2[0] = 100
print(np1)