import numpy as np
import matplotlib.pyplot as plt


def my_linfit(x, y): #Pen and paper calculations for a and b. Made into a code.
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)

    # a function
    a = (sum_xy - (sum_y*sum_x)/n) / (sum_x2-((sum_x*sum_x)/n))
    # b function
    b = (sum_y - a*sum_x)/n

    return a, b


# Event handler for mouse clicks
def clicker(event):
    if event.button == 1:  # Left click to add point
        points.append([event.xdata, event.ydata])
        plt.plot(event.xdata, event.ydata, "kx")  # Plot the point
        plt.draw()  # Update the plot
    elif event.button == 3:  # Close if right click.
        plt.disconnect(cid)
        plt.close()


# Empty list to store points
points = []

# Set up the figure and connect the event handler
fig, ax = plt.subplots()
ax.set_title("Left click to add points, right click to stop")
cid = fig.canvas.mpl_connect("button_press_event", clicker)

# Show the grid to take points from user input, aka clicks.
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(True)
plt.show()

if len(points) > 1:  # Ensure we have at least 2 points
    points = np.array(points)
    x = points[:, 0]
    y = points[:, 1]

    # Fit the line using the functions defined earlier
    a, b = my_linfit(x, y)

    # Plot the points and the fitted line
    plt.plot(x, y, "kx")
    xp = np.linspace(min(x), max(x), 100)
    plt.plot(xp, a * xp + b, "r-")
    plt.grid(True)
    plt.show()

    # Print the computed values of a and b
    print(f"My fit: a = {a} and b = {b}")
else:
    print("Not enough points to fit a line. Need at least 2")