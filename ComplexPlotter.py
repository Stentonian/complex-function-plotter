from visual import *
from visual.controls import *
import numpy as np
import math

dimension = 600 # all the windows sizes are scaled to this number (so change this number if you want to resize)
Range = 20

# the real axis for the domain plane is perpindicular to that of the image Plane, while thier imaginary azes are parallel
RealDisplay = display(title='Imaginary axes paralell, real axes orthogonal', x=0, y=0, width=dimension, height=dimension, background=color.white)
RealDisplay.range = Range

# the imaginary axis for the domain plane is perpindicular to that of the image Plane, while thier real azes are parallel
ImagDisplay = display(title='Real axes paralell, Imaginary axes orthogonal', x=dimension+10, y=0, width=dimension, height=dimension, background=color.white)
ImagDisplay.range = Range

# control panel equipment
control = controls(title='Controlling the Scene', x=0, y=dimension+10, width=dimension*2, height=150)
realSliderA = slider( pos=(-80,5), length=50, min=-10, max=10, value=5, action=lambda: sliderAction() ) # increase side A of the domain rectangle, parallel to the real axis
realSliderB = slider( pos=(-80,-5), length=50, min=-10, max=10, value=0, action=lambda: sliderAction() ) # increase side B of the domain rectangle, parallel to the real axis
imagSliderA = slider( pos=(0,5), length=50, min=-10, max=10, value=5, action=lambda: sliderAction() ) # increase side A of the domain rectangle, parallel to the imaginary axis
imagSliderB = slider( pos=(0,-5), length=50, min=-10, max=10, value=0, action=lambda: sliderAction() ) # increase side B of the domain rectangle, parallel to the imaginary axis

# ==============================================================================================================
# control methods for the sliders

# used by the slider action methods
def redrawAll(frames, plot):
    # must have the correct display selected before calling this method
    
    for frame in frames:
        for obj in frame.objects:
            obj.visible = False
            del obj

    realT = max(realSliderA.value, realSliderB.value)
    realB = min(realSliderA.value, realSliderB.value)
    imagT = max(imagSliderA.value, imagSliderB.value)
    imagB = min(imagSliderA.value, imagSliderB.value)
    
    pos, colour = makeDomRec(realB,realT,imagB,imagT)
    
    drawSurface(pos,frames[0],colour, plot)
    newpos, newcolour = mapShape(pos, colour, 20, 20, plot)
    drawSurface(newpos,frames[1], newcolour, plot)

# when either the right or the left slider is moved
def sliderAction():
    RealDisplay.select()
    frames = [Fr, Fdash]
    redrawAll(frames, 'real')

    ImagDisplay.select()
    frames = [fr, fdash]
    redrawAll(frames, 'imag')
    
# ==============================================================================================================
# construct the grid systems (so that you can see the domain and image Planes clearly)
def drawRealDomainPlane(max=15, rad=0.03, spacing=2):
    RealDisplay.select()
    gray = (0.6,0.6,0.6)
    
    for v in range(-max,max+1,spacing):
        cylinder(pos=(v,-max,0), axis=(0,2*max,0), radius=rad, color=gray, opacity=0.2) ## parallel to y axis, vary x
        cylinder(pos=(-max,v,0), axis=(2*max,0,0), radius=rad, color=gray, opacity=0.2) ## parallel to x axis, vary y

    Raxis=cylinder(color=color.green, pos=(-max,0,0), axis=(2*max,0,0), radius=5*rad)
    Rlbl=label(pos=(max+1,0,0), text="Re", color=gray, opacity=0, height=30)
    
    Iaxis=cylinder(color=color.magenta, pos=(0,-max,0), axis=(0,2*max,0), radius=5*rad)
    Ilbl=label(pos=(0,max+1,0), text="Im", color=gray, opacity=0, height=30)

def drawImagDomainPlane(max=15, rad=0.03, spacing=2):
    ImagDisplay.select()
    gray = (0.6,0.6,0.6)
    
    for v in range(-max,max+1,spacing):
        cylinder(pos=(v,-max,0), axis=(0,2*max,0), radius=rad, color=gray, opacity=0.2) ## parallel to y axis, vary x
        cylinder(pos=(-max,v,0), axis=(2*max,0,0), radius=rad, color=gray, opacity=0.2) ## parallel to x axis, vary y

    Raxis=cylinder(color=color.green, pos=(-max,0,0), axis=(2*max,0,0), radius=5*rad)
    Rlbl=label(pos=(max+1,0,0), text="Re", color=gray, opacity=0, height=30)
    
    Iaxis=cylinder(color=color.magenta, pos=(0,-max,0), axis=(0,2*max,0), radius=5*rad)
    Ilbl=label(pos=(0,max+1,0), text="Im", color=gray, opacity=0, height=30)

def drawRealImagePlane(max=15, rad=0.03, spacing=2):
    RealDisplay.select()
    gray = (0.2,0.2,0.2)
    
    for v in range(-max,max+1,spacing):
        cylinder(pos=(0,-max,v), axis=(0,2*max,0), radius=rad, color=gray, opacity=0.2) ## parallel to y axis, vary z
        cylinder(pos=(0,v,-max), axis=(0,0,2*max), radius=rad, color=gray, opacity=0.2) ## parallel to z axis, vary y

    Raxis=cylinder(color=color.red, pos=(0,0,-max), axis=(0,0,2*max), radius=5*rad)
    Rlbl=label(pos=(0,0,-(max+1)), text="Re", color=gray, opacity=0, height=30)
    
    Ilbl=label(pos=(0,max+4,0), text="Im", color=gray, opacity=0, height=30)

def drawImagImagePlane(max=15, rad=0.03, spacing=2):
    ImagDisplay.select()
    gray = (0.2,0.2,0.2)
    
    for v in range(-max,max+1,spacing):
        cylinder(pos=(-max,0,v), axis=(2*max,0,0), radius=rad, color=gray, opacity=0.2) ## parallel to x axis, vary z
        cylinder(pos=(v,0,-max), axis=(0,0,2*max), radius=rad, color=gray, opacity=0.2) ## parallel to z axis, vary x

    Rlbl=label(pos=(max+4,0,0), text="Re", color=gray, opacity=0, height=30)

    Iaxis=cylinder(color=color.red, pos=(0,0,-max), axis=(0,0,2*max), radius=5*rad)
    Ilbl=label(pos=(0,0,-(max+1)), text="Im", color=gray, opacity=0, height=30)

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
    return vector(z.x,-z.y,0)

# multiply two complex numbers
# z, w must be vectors
# returns a vector, z*w
def mult(z,w):
    return vector(z.x*w.x - z.y*w.y, z.x*w.y + z.y*w.x, 0)
    # or you can use the z = r*e^(i*theta) notation: (the above one is probably faster)
    # return mod(z)*mod(w)*iExp(arg(z) + arg(w))

# divide two complex numbers
# z, w must be vectors
# returns a vector, z/w
def div(z,w):
    return mult(z,conj(w)/(mod(w)**2))

# powers of z
# z must be a vector
# n must be an integer
# returns z^n
def power(z,n):
    if n == 0: # z^0 = 1
        return vector(1,0,0)
    w = z
    for i in range(2,abs(n)+1):
        w = mult(w,z)
    if n > 0: # z^n
        return w
    else: # z^(-n) = 1/z^n
        return div(vector(1,0,0),w)

# complex exponential
# theta must be a real number
# returns e^(i*theta)
def iExp(theta):
    return vector(np.cos(theta),np.sin(theta),0)

# ==============================================================================================================
# functions to plot go here
# note: z is a vector (z = (a,b,0) = a + bi)

def Log(z): # Log(z)
    return vector(np.log(mod(z)), arg(z), 0)

def squared(z): # z^2
    return mult(z,z)

# e^z, this function is computed using real and imaginary exponetials seperately
# z must be a vector
def exp(z):
    return math.exp(z.x)*iExp(z.y)

# cos(z), this function is plotted using Euler's formula
# z must be a vector
def cosine(z):
    return 0.5*(iExp(z.x)*math.exp(-z.y) + iExp(-z.x)*math.exp(z.y))

# use this to pick a function to plot
# it is crucial to use this function because other methods use this function for computing stuff
def f(z):
    return Log(z)

# ==============================================================================================================
# maps a curve in the domain Plane to a curve in the image space using 'f(z)'
#
# c must be a curve
def mapCurve(c):
    F = lambda v1,v2: f(vector(v1,v2,0))

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
# f must be a frame
# c must be a color
# plot must be a string, either 'real' or 'imag', specifies on which display to draw
def drawSurface(S, f, c, plot):
    if plot == 'real':
        RealDisplay.select()
    elif plot == 'imag':
        ImagDisplay.select()
    else:
        print 'you fucked up in the drawSurfaces method'
        
    shape = faces(pos=S, color=c, frame=f)
    shape.make_normals()
    shape.make_twosided()
    shape.smooth()

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
    rec = [] # rectangele vector array (each set of 3 vectors is a triangle)
    col = [] # colours array
    
    Rrange = int((Rmax - Rmin)/step) + 1 # the number of steps in the real direction
    Irange = int((Imax - Imin)/step) + 1 # the number of steps in the imaginary direction

    dColReal = 1.0/Rrange
    dColImag = 1.0/Irange
    
    for r in range(Rrange):
        for i in range(Irange):
            R = Rmin + r*step
            I = Imin + i*step
            dR = step
            dI = step
            
            topTri = [vector(R, I, 0), vector(R+dR, I, 0), vector(R+dR, I+dI, 0)]
            botTri = [vector(R, I, 0), vector(R, I+dI, 0), vector(R+dR, I+dI, 0)]

            topCol = [(0,r*dColReal,1)]*3 # go from dark blue to cyan as the real part moves in +ve direction
            botCol = [(i*dColImag,i*dColImag,i*dColImag)]*3 # go from light gray to dark gray as the imaginary part move in +ve direction

            rec += topTri + botTri
            col += topCol + botCol

    return rec, col

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
    mapped = map(lambda v: f(v), S)
    mappedPrime = []
    SPrime = []
    CPrime = []

    for i in range(0, len(mapped), 3):
        if abs(mapped[i].x) < Rbound and abs(mapped[i+1].x) < Rbound and abs(mapped[i+2]) < Rbound and abs(mapped[i].y) < Ibound and abs(mapped[i+1].y) < Ibound and abs(mapped[i+2].y) < Ibound:
            mappedPrime += [mapped[i], mapped[i+1], mapped[i+2]]
            SPrime += [S[i], S[i+1], S[i+2]]
            CPrime += [C[i], C[i+1], C[i+2]]

    if plot == 'real':
        RealDisplay.select()
        return map(lambda v, w: vector(w.x, v.y, -v.x), mappedPrime, SPrime), CPrime
    elif plot =='imag':
        ImagDisplay.select()
        return map(lambda v, w: vector(v.x, w.y, -v.y), mappedPrime, SPrime), CPrime
    else:
        print 'you fucked up in the mapShape function'
        exit()

# ==============================================================================================================

#k = curve(x=arange(0,20,0.1), color=color.green)
#k.y = [1]*len(k.x)
#drawCurve(k)

pos, colour = makeDomRec(0,10,0,10) #makeDomRec(realSliderB.value,realSliderA.value,imagSliderB.value,imagSliderA.value)

global fr, fdash, Fr, Fdash

ImagDisplay.select()
fr = frame()
fdash = frame()
drawSurface(pos,fr,colour, 'imag')
newpos, newcolour = mapShape(pos, colour, 20, 20, 'imag')
drawSurface(newpos,fdash, newcolour, 'imag')

RealDisplay.select()
Fr = frame()
Fdash = frame()
drawSurface(pos,Fr,colour, 'real')
newpos, newcolour = mapShape(pos, colour, 20, 20, 'real')
drawSurface(newpos,Fdash, newcolour, 'real')

