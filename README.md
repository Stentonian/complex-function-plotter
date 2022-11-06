# Complex function plotter

Graphing software to plot functions of a single complex variable. 


_Note: the idea and the code were created in 2015 but were only uploaded to GH in 2022_

## The Idea

Consider a function of a single complex variable:

It is common to algebraically represent complex numbers using 2 real numbers (imaginary and real parts) and it is common to visually represent complex numbers using a Cartesian plane. Using 2 dimensions to represent any 1 complex number means that the graph of a function of 1 complex variable can only be fully appreciated in 4 spatial dimensions, which is a problem for us 3D humans. There are other some ways of plotting complex functions (such as [this one](http://davidbau.com/conformal/#z)) and the following is a description of one such way.

Consider 2 complex planes: the domain plane (`z`) and the image plane (`f(z)`). If we have these planes in 3-space then unless they are parallel they will intersect in a straight line. Consider 2 cases:
- this intersection line is the imaginary axes for both planes
- this intersection line is the real axes for both planes
These 2 different alignments of the domain and image planes are the axes for our graph. To be able to talk about where points are going to be located we will use R^3 (or 3-space) coordinates: `<x,y,z>`. Place the domain plane in the same place as the xy-plane, and then place the image plane such that it gives the 2 desired intersections above.

The way that the graph is formed is like so:
- take a point `z=a+bi` in the domain plane (note that it's coordinates are `<a,b,0>` in 3-space)
- apply the function `f` to `z` to get `f(z)=c+di`
- draw a point at the following 3-space coordinates:
  - for the imaginary-aligned axes: `<c,b,d>`
  - for the real-aligned axes: `<a,d,c>`

## How the code works

The library used to build the 3D objects is VPython. You can install that with `pip install vpython`, and then you can run the grapher with `python ComplexPlotter.py`. Running the script produces 2 3D spaces each containing one of the domain/image plane intersections described above.

Instead of trying to map the whole domain plane there is a coloured rectangle that is mapped. This helps the viewer to figure out how which point in the domain plane resulted in the mapped point.

The graph surfaces are made up of small triangles, which means the surfaces are not perfectly smooth, but this method of building surfaces is easy to work with and allows for colouring to help the viewer see what is going on.

## Screenshots
