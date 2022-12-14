from vpython import *
import numpy as np
import math

# all the windows sizes are scaled to this number (so change this number if you want to resize)
dimension = 1200
Range = 20

# the real axis for the domain plane is perpindicular to that of the image Plane, while thier imaginary azes are parallel
RealDisplay = canvas(#title='Imaginary axes paralell, real axes orthogonal',
                     align='left',
                     #caption='  Imaginary axes paralell,\n  real axes orthogonal',
                     width=dimension,
                     height=dimension,
                     background=color.white)
RealDisplay.range = Range

# the imaginary axis for the domain plane is perpindicular to that of the image Plane, while thier real azes are parallel
ImagDisplay = canvas(#title='Real axes paralell, Imaginary axes orthogonal',
                     align='right',
                     #caption='  Real axes paralell,\n  imaginary axes orthogonal',
                     width=dimension,
                     height=dimension,
                     background=color.white)
ImagDisplay.range = Range

# # ==============================================================================================================
# # control methods for the sliders

# # used by the slider action methods
# def redrawAll(frames, plot):
#     # must have the correct display selected before calling this method

#     for frame in frames:
#         for obj in frame.objects:
#             obj.visible = False
#             del obj

#     realT = max(realSliderA.value, realSliderB.value)
#     realB = min(realSliderA.value, realSliderB.value)
#     imagT = max(imagSliderA.value, imagSliderB.value)
#     imagB = min(imagSliderA.value, imagSliderB.value)

#     pos, colour = makeDomRec(realB, realT, imagB, imagT)

#     drawSurface(pos, frames[0], colour, plot)
#     newpos, newcolour = mapShape(pos, colour, 20, 20, plot)
#     drawSurface(newpos, frames[1], newcolour, plot)


# # when either the right or the left slider is moved
# def sliderAction():
#     RealDisplay.select()
#     frames = [Fr, Fdash]
#     redrawAll(frames, 'real')

#     ImagDisplay.select()
#     frames = [fr, fdash]
#     redrawAll(frames, 'imag')

# # ==============================================================================================================
# # controls

# # control panel equipment
# control = controls(title='Controlling the Scene',
#                    x=0,
#                    y=dimension + 10,
#                    width=dimension * 2,
#                    height=150)
# # increase side A of the domain rectangle, parallel to the real axis
# realSliderA = slider(pos=vector(-80, 5, 0),
#                      length=50,
#                      min=-10,
#                      max=10,
#                      value=5,
#                      bind=sliderAction)
# # increase side B of the domain rectangle, parallel to the real axis
# realSliderB = slider(pos=vector(-80, -5, 0),
#                      length=50,
#                      min=-10,
#                      max=10,
#                      value=0,
#                      bind=sliderAction)
# # increase side A of the domain rectangle, parallel to the imaginary axis
# imagSliderA = slider(pos=vector(0, 5, 0),
#                      length=50,
#                      min=-10,
#                      max=10,
#                      value=5,
#                      bind=sliderAction)
# # increase side B of the domain rectangle, parallel to the imaginary axis
# imagSliderB = slider(pos=vector(0, -5, 0),
#                      length=50,
#                      min=-10,
#                      max=10,
#                      value=0,
#                      bind=sliderAction)

# ==============================================================================================================
# construct the grid systems (so that you can see the domain and image Planes clearly)
def drawRealDomainPlane(max=15, rad=0.03, spacing=2):
    RealDisplay.select()
    gray = vector(0.6, 0.6, 0.6)

    for v in range(-max, max + 1, spacing):
        ## parallel to y axis, vary x
        cylinder(pos=vector(v, -max, 0),
                 axis=vector(0, 2 * max, 0),
                 radius=rad,
                 color=gray,
                 opacity=0.2)
        ## parallel to x axis, vary y
        cylinder(pos=vector(-max, v, 0),
                 axis=vector(2 * max, 0, 0),
                 radius=rad,
                 color=gray,
                 opacity=0.2)

    Raxis = cylinder(color=color.green,
                     pos=vector(-max, 0, 0),
                     axis=vector(2 * max, 0, 0),
                     radius=5 * rad)
    Rlbl = label(pos=vector(max + 1, 0, 0),
                 text="Re",
                 color=gray,
                 opacity=0,
                 height=30)

    Iaxis = cylinder(color=color.magenta,
                     pos=vector(0, -max, 0),
                     axis=vector(0, 2 * max, 0),
                     radius=5 * rad)
    Ilbl = label(pos=vector(0, max + 1, 0),
                 text="Im",
                 color=gray,
                 opacity=0,
                 height=30)


def drawImagDomainPlane(max=15, rad=0.03, spacing=2):
    ImagDisplay.select()
    gray = vector(0.6, 0.6, 0.6)

    for v in range(-max, max + 1, spacing):
        ## parallel to y axis, vary x
        cylinder(pos=vector(v, -max, 0),
                 axis=vector(0, 2 * max, 0),
                 radius=rad,
                 color=gray,
                 opacity=0.2)
        ## parallel to x axis, vary y
        cylinder(pos=vector(-max, v, 0),
                 axis=vector(2 * max, 0, 0),
                 radius=rad,
                 color=gray,
                 opacity=0.2)

    Raxis = cylinder(color=color.green,
                     pos=vector(-max, 0, 0),
                     axis=vector(2 * max, 0, 0),
                     radius=5 * rad)
    Rlbl = label(pos=vector(max + 1, 0, 0),
                 text="Re",
                 color=gray,
                 opacity=0,
                 height=30)

    Iaxis = cylinder(color=color.magenta,
                     pos=vector(0, -max, 0),
                     axis=vector(0, 2 * max, 0),
                     radius=5 * rad)
    Ilbl = label(pos=vector(0, max + 1, 0),
                 text="Im",
                 color=gray,
                 opacity=0,
                 height=30)


def drawRealImagePlane(max=15, rad=0.03, spacing=2):
    RealDisplay.select()
    gray = vector(0.2, 0.2, 0.2)

    for v in range(-max, max + 1, spacing):
        ## parallel to y axis, vary z
        cylinder(pos=vector(0, -max, v),
                 axis=vector(0, 2 * max, 0),
                 radius=rad,
                 color=gray,
                 opacity=0.2)
        ## parallel to z axis, vary y
        cylinder(pos=vector(0, v, -max),
                 axis=vector(0, 0, 2 * max),
                 radius=rad,
                 color=gray,
                 opacity=0.2)

    Raxis = cylinder(color=color.red,
                     pos=vector(0, 0, -max),
                     axis=vector(0, 0, 2 * max),
                     radius=5 * rad)
    Rlbl = label(pos=vector(0, 0, -(max + 1)),
                 text="Re",
                 color=gray,
                 opacity=0,
                 height=30)

    Ilbl = label(pos=vector(0, max + 4, 0),
                 text="Im",
                 color=gray,
                 opacity=0,
                 height=30)


def drawImagImagePlane(max=15, rad=0.03, spacing=2):
    ImagDisplay.select()
    gray = vector(0.2, 0.2, 0.2)

    for v in range(-max, max + 1, spacing):
        ## parallel to x axis, vary z
        cylinder(pos=vector(-max, 0, v),
                 axis=vector(2 * max, 0, 0),
                 radius=rad,
                 color=gray,
                 opacity=0.2)
        ## parallel to z axis, vary x
        cylinder(pos=vector(v, 0, -max),
                 axis=vector(0, 0, 2 * max),
                 radius=rad,
                 color=gray,
                 opacity=0.2)

    Rlbl = label(pos=vector(max + 4, 0, 0),
                 text="Re",
                 color=gray,
                 opacity=0,
                 height=30)

    Iaxis = cylinder(color=color.red,
                     pos=vector(0, 0, -max),
                     axis=vector(0, 0, 2 * max),
                     radius=5 * rad)
    Ilbl = label(pos=vector(0, 0, -(max + 1)),
                 text="Im",
                 color=gray,
                 opacity=0,
                 height=30)


# ==============================================================================================================
drawImagDomainPlane()
drawImagImagePlane()
drawRealDomainPlane()
drawRealImagePlane()

# ==============================================================================================================
# complex math equipment
# note: every complex number is a vector (z = (a,b,0) = a + bi)


# modulus
# z must be a vector
# returns a real number
def mod(z):
    return np.sqrt(z.x**2 + z.y**2)


# argument
# z must be a vector
# returns a real number
def arg(z):
    return np.arctan2(z.y, z.x)


# conjugate
# z must be a vector
# returns a vector, z*
def conj(z):
    return vector(z.x, -z.y, 0)


# multiply two complex numbers
# z, w must be vectors
# returns a vector, z*w
def mult(z, w):
    return vector(z.x * w.x - z.y * w.y, z.x * w.y + z.y * w.x, 0)
    # or you can use the z = r*e^(i*theta) notation: (the above one is probably faster)
    # return mod(z)*mod(w)*iExp(arg(z) + arg(w))


# divide two complex numbers
# z, w must be vectors
# returns a vector, z/w
def div(z, w):
    return mult(z, conj(w) / (mod(w)**2))


# powers of z
# z must be a vector
# n must be an integer
# returns z^n
def power(z, n):
    # z^0 = 1
    if n == 0:
        return vector(1, 0, 0)
    w = z
    for i in range(2, abs(n) + 1):
        w = mult(w, z)
# z^n
    if n > 0:
        return w
# z^(-n) = 1/z^n
    else:
        return div(vector(1, 0, 0), w)


# complex exponential
# theta must be a real number
# returns e^(i*theta)
def iExp(theta):
    return vector(np.cos(theta), np.sin(theta), 0)


# ==============================================================================================================
# functions to plot go here
# note: z is a vector (z = (a,b,0) = a + bi)


# Log(z)
def Log(z):
    if mod(z) == 0:
        return vector(-1000000, arg(z), 0)
    return vector(np.log(mod(z)), arg(z), 0)


# z^2
def squared(z):
    return mult(z, z)


# e^z, this function is computed using real and imaginary exponetials seperately
# z must be a vector
def exp(z):
    return math.exp(z.x) * iExp(z.y)


# cos(z), this function is plotted using Euler's formula
# z must be a vector
def cosine(z):
    return 0.5 * (iExp(z.x) * math.exp(-z.y) + iExp(-z.x) * math.exp(z.y))


# use this to pick a function to plot
# it is crucial to use this function because other methods use this function for computing stuff
def f(z):
    return exp(z)


# ==============================================================================================================
# maps a curve in the domain Plane to a curve in the image space using 'f(z)'
#
# c must be a curve
def mapCurve(c):
    F = lambda v1, v2: f(vector(v1, v2, 0))

    image = map(F, c.x, c.y)

    C = curve(color=color.black)

    C.x = c.x
    C.y = map(lambda v: v.y, image)
    C.z = map(lambda v: -v.x, image)


# ==============================================================================================================
# creates a faces object using an input of triangle vertices
# and then draws the surface in the specified graphics window
#
# S mst be an array of traingle vertices e.g.
#   S = [(0,0,0), (0,1,0), (0,0,1), --> first tirangle's three vertices
#        (x,y,z), (x,y,z), (x,y,z)] --> second triangle's three vertices
# c must be a color
# plot must be a string, either 'real' or 'imag', specifies on which display to draw
def drawSurface(S, c, plot):
    if plot == 'real':
        RealDisplay.select()
    elif plot == 'imag':
        ImagDisplay.select()
    else:
        raise Exception('drawSurface requires plot to be real or imag')

    for i in range(len(S)):
        triangle(vs=[vertex(pos=S[i][0], color=c[i]),
                     vertex(pos=S[i][1], color=c[i]),
                     vertex(pos=S[i][2], color=c[i])])


# ==============================================================================================================
# creates an array of points (and corresponding array of colours) desribing a rectangle
# these arrays must still be used to draw the rectangle in the domain plane
#
# Rmax & Rmin are the real bounds of the rectangle
# Imax & Imin are the imaginary bounds of the rectangle
# both must be integers
#
# the array of points created (and returned) has the form of 'S' in 'drawSurface()' method
def makeDomRec(Rmin, Rmax, Imin, Imax, step=0.5):
    # rectangele vector array (each set of 3 vectors is a triangle)
    rec = []
    # colours array
    col = []

    # the number of steps in the real direction
    Rrange = int((Rmax - Rmin) / step) + 1
    # the number of steps in the imaginary direction
    Irange = int((Imax - Imin) / step) + 1

    dColReal = 1.0 / Rrange
    dColImag = 1.0 / Irange

    for r in range(Rrange):
        for i in range(Irange):
            R = Rmin + r * step
            I = Imin + i * step
            dR = step
            dI = step

            topTri = [
                vec(R, I, 0),
                vec(R + dR, I, 0),
                vec(R + dR, I + dI, 0)
            ]
            botTri = [
                vec(R, I, 0),
                vec(R, I + dI, 0),
                vec(R + dR, I + dI, 0)
            ]

            # go from dark blue to cyan as the real part moves in +ve direction
            topCol = vec(0, r * dColReal, 1)
            # go from light gray to dark gray as the imaginary part move in +ve direction
            botCol = vec(i * dColImag, i * dColImag, i * dColImag)

            rec += [topTri, botTri]
            col += [topCol, botCol]

    return rec, col


def realMapper(mappedTri, originalTri):
    a = mappedTri[0]
    b = mappedTri[1]
    c = mappedTri[2]

    A = originalTri[0]
    B = originalTri[1]
    C = originalTri[2]

    one = vector(A.x, a.y, -a.x)
    two = vector(B.x, b.y, -c.x)
    three = vector(C.x, c.y, -c.x)

    return [one, two, three]


def imagMapper(mappedTri, originalTri):
    a = mappedTri[0]
    b = mappedTri[1]
    c = mappedTri[2]

    A = originalTri[0]
    B = originalTri[1]
    C = originalTri[2]

    one = vector(a.x, A.y, -a.y)
    two = vector(b.x, B.y, -b.y)
    three = vector(c.x, C.y, -c.y)

    return [one, two, three]


def checkWithinBounds(mappedTri, bound):
    a = mappedTri[0]
    b = mappedTri[1]
    c = mappedTri[2]

    one = abs(a.x) < bound and abs(a.y) < bound and abs(a.z) < bound
    two = abs(b.x) < bound and abs(b.y) < bound and abs(b.z) < bound
    three = abs(c.x) < bound and abs(c.y) < bound and abs(c.z) < bound

    return one and two and three


# ==============================================================================================================
# maps a set of vectors using 'f(z)'
#
# S must be a set of points, the same as 'S' in the 'drawSurface()' method
# Rbound & I bound are the bounds of the image space, so nothing will be drawn outside of the bounds
# C must be an array of colour vectors
# plot must be a string, either 'real' or 'imag', specifies on which display to draw
#
# returns a set of mapped points
def mapShape(S, C, Rbound, Ibound, plot):
    mapped = list(map(lambda v: [f(v[0]), f(v[1]), f(v[2])], S))

    bound = min(Rbound, Ibound)

    mappedPrime = []
    SPrime = []
    CPrime = []

    for i in range(0, len(mapped)):
        if checkWithinBounds(mapped[i], bound):
            mappedPrime += [mapped[i]]
            SPrime += [S[i]]
            CPrime += [C[i]]

    if plot == 'real':
        RealDisplay.select()
        return list(map(realMapper, mappedPrime, SPrime)), CPrime
    elif plot == 'imag':
        ImagDisplay.select()
        return list(map(imagMapper, mappedPrime, SPrime)), CPrime
    else:
        raise Exception('Plot needs to be real or imag')


# ==============================================================================================================

#makeDomRec(realSliderB.value,realSliderA.value,imagSliderB.value,imagSliderA.value)
pos, colour = makeDomRec(-5, 10, -5, 10)

ImagDisplay.select()
drawSurface(pos, colour, 'imag')
newpos, newcolour = mapShape(pos, colour, 20, 20, 'imag')
drawSurface(newpos, newcolour, 'imag')

RealDisplay.select()
drawSurface(pos, colour, 'real')
newpos, newcolour = mapShape(pos, colour, 20, 20, 'real')
drawSurface(newpos, newcolour, 'real')

# need this when running from terminal: https://vpython.org/presentation2018/install.html
while True:
    rate(30)
