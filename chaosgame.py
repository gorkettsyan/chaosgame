import matplotlib.pyplot as plt
from random import randint

x = [2, 6, 4, 3]
y = [3, 3, 14, 8]


def sierpinski(n):
    
    for i in range(n):
        rand = randint(1, 3)
        if rand == 1 :
            x.append((x[0] + x[len(x) -1])/2)
            y.append((y[0] + y[len(y) - 1])/2)
                

        elif rand == 2:
            x.append((x[1] + x[len(x) -1])/2)
            y.append((y[1] + y[len(y) - 1])/2)

        
        elif rand == 3:
            x.append((x[2] + x[len(x) -1])/2)
            y.append((y[2] + y[len(y) - 1])/2)


    plt.plot(x, y, 'b.')
    plt.show()



sierpinski(100000)



