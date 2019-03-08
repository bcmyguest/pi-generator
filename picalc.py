# gennerator to determine pi at increasing accuracy

def piGen():
    n, last, pi  = 0.0, 0.0, 4.0

    while True:
        pi = last + 4*((-1)**n)*(1/((2*n)+1))
        last = pi
        n += 1
        yield pi
        

p = piGen()
res = 1.0
#change this value to increase or decrease the accuracy of the value
num_iterations = 100000

for i in range(num_iterations):
    res = next(p)
    if i%10000 == 0:
        print("pi: " + str(res))
