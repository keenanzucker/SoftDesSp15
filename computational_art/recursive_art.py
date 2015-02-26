<<<<<<< HEAD
""" Recursive Art!  Computers can do amazing things! This program can create beautiful PNG images using the power of random and recursion. It works
by using a build function that will be generate random functions within nested lists between a passed-in depth. Then the random function will be evaluated
and remapped to a value between 0-255, which correspond to an RGB color value. This creates unique and stylish images each time run!"""

import random
from PIL import Image
import math

minDepth = 9
maxDepth = 12
numImages = 5
=======
""" TODO: Put your header comment here """

import random
from PIL import Image

>>>>>>> f995e7995873fb13efc0faeca7688191045d189d

def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    # TODO: implement this
<<<<<<< HEAD
    temp = random.randint(2,7)

    if max_depth == 0:                          #Base case for maximum depth, chooses between x and y to return
        return [random.choice(["x", "y"])]
    if min_depth <= 0 and random.randint(0,1):  #Base case for minimum depth, only returns 50% of time
        return [random.choice(["x", "y"])]


    elif temp == 0:     #Function SQ(A) = A**2
        return ["sq", build_random_function(min_depth-1, max_depth-1)]

    elif temp == 1:     #Function THR(A) = A**3
        return ["thr", build_random_function(min_depth-1, max_depth-1)]

    elif temp == 2:     #Function COS_PI(A) = COS(PI*A)
        return ["cos_pi", build_random_function(min_depth-1, max_depth-1)]

    elif temp == 3:     #Function SIN_PI(A) = SIN(PI*A)
        return ["sin_pi", build_random_function(min_depth-1, max_depth-1)]

    elif temp == 4:     #Function PROD(A,B) = A*B
        return ["prod", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]

    elif temp == 5:     #Fucntion AVG(A,B) = 0.5 * (A + B)
        return ["avg", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]

    elif temp == 6:     #Fucntion DIV(A,B) = A/2 + B/3
        return ["addDiv", build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]

    elif temp == 7:     #Fucntion DIV(A,B) = A/2 + B/3
        return ["root", build_random_function(min_depth-1, max_depth-1)]


print build_random_function(minDepth,maxDepth)
=======
    pass

>>>>>>> f995e7995873fb13efc0faeca7688191045d189d

def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    # TODO: implement this
<<<<<<< HEAD

    if f[0] == "x":     #Function for X
        return x

    elif f[0] == "y":   #Function fof Y
        return y

    elif f[0] == "sq":      #Squares the first input
        return (evaluate_random_function(f[1], x, y) ** 2)

    elif f[0] == "thr":         #Takes the first input to the third power
        return (evaluate_random_function(f[1], x, y) ** 3)

    elif f[0] == "cos_pi":     #Function takes cos of pi times input
        return math.cos(math.pi * evaluate_random_function(f[1], x, y))

    elif f[0] == "sin_pi":      #Function takes sin of pi times input
        return math.sin(math.pi * evaluate_random_function(f[1], x, y))

    elif f[0] == "prod":        #Function multiplies two inputs
        return (evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y))

    elif f[0] == "avg":         # Function takes average of first and second input
        return (0.5 * (evaluate_random_function(f[1], x, y) + evaluate_random_function(f[2], x, y)))

    elif f[0] == "addDiv":      #Function multiplies each inmput by value under 1
        return ( (evaluate_random_function(f[1], x, y)) +  (evaluate_random_function(f[2], x, y)))

    elif f[0] == "root":        #Function takes square root of first input
        return math.sqrt(abs(evaluate_random_function(f[1], x, y)))
=======
    pass
>>>>>>> f995e7995873fb13efc0faeca7688191045d189d


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # TODO: implement this
<<<<<<< HEAD
    
    position = val - float(input_interval_start)

    distanceInput = float(input_interval_end) - float(input_interval_start)  

    relative = position / distanceInput

    distanceOutput = float(output_interval_end) - float(output_interval_start)  

    return (relative * distanceOutput) + output_interval_start
=======
    pass
>>>>>>> f995e7995873fb13efc0faeca7688191045d189d


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


<<<<<<< HEAD
def generate_art(filename, x_size=1600, y_size=900):
=======
def generate_art(filename, x_size=350, y_size=350):
>>>>>>> f995e7995873fb13efc0faeca7688191045d189d
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
<<<<<<< HEAD
    red_function = build_random_function(minDepth, maxDepth)
    green_function = build_random_function(minDepth, maxDepth)
    blue_function = build_random_function(minDepth, maxDepth)
=======
    red_function = ["x"]
    green_function = ["y"]
    blue_function = ["x"]
>>>>>>> f995e7995873fb13efc0faeca7688191045d189d

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
<<<<<<< HEAD
    for i in range (0, numImages):
        generate_art("Wall" + str(i) + ".png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    #test_image("noise.png")

=======
    #generate_art("myart.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    test_image("noise.png")
>>>>>>> f995e7995873fb13efc0faeca7688191045d189d
