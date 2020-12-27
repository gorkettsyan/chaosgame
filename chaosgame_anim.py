from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def siperpinski_triangle():
    x = [2, 4, 6, 3]
    y = [3, 14, 3, 8]

    def animate(i):
        rand = randint(1, 6)
        if rand == 1 or rand == 2:
            x.append((x[0] + x[len(x) - 1])/2)
            y.append((y[0] + y[len(y) - 1])/2)

        elif rand == 3 or rand == 4:
            x.append((x[1] + x[len(x) - 1])/2)
            y.append((y[1] + y[len(y) - 1])/2)

        elif rand == 5 or rand == 6:
            x.append((x[2] + x[len(x) - 1])/2)
            y.append((y[2] + y[len(y) - 1])/2)

        ax1.scatter(x, y, color='g', s=2)

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    animation.FuncAnimation(fig, animate, interval=100, frames=1)

    plt.show()


siperpinski_triangle()
