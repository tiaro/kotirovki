import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set maximum drawing speed
t.pencolor("white")

# Define the vertices of the initial triangle
vertices = [[-200, -100], [0, 200], [200, -100]]

# Function to calculate the midpoint between two points
def midpoint(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

# Chaos Game algorithm
def chaos_game(n):
    # Start at the first vertex
    point = vertices[0]
    t.up()
    t.goto(point)
    t.down()

    for _ in range(n):
        # Choose a random vertex
        vertex = vertices[random.randint(0, 2)]
        # Calculate the midpoint between the current point and the chosen vertex
        point = midpoint(point, vertex)
        # Draw the point
        t.goto(point)

# Call the chaos_game function with the desired number of points
chaos_game(50000)

# Keep the window open until it's closed manually
turtle.done()
