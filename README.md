# Complex function plotter

Graphing software to plot functions of a single complex variable. 


_Note: the idea and the code were created in 2015 but were only uploaded to GH in 2022_

## The Idea

Consider a function of a single complex variable:

![CodeCogsEqn](https://user-images.githubusercontent.com/48631759/200193844-df768327-0d5b-470a-aa02-49cbabe432ed.png)


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

The library used to build the 3D objects is [VPython](https://duckduckgo.com/?t=ffab&q=vpython&ia=web). You can install that with `pip install vpython`, and then you can run the grapher with `python ComplexPlotter.py`. Running the script produces 2 3D spaces each containing one of the domain/image plane intersections described above.

Instead of trying to map the whole domain plane there is a coloured rectangle that is mapped. This helps the viewer to figure out how which point in the domain plane resulted in the mapped point.

The graph surfaces are made up of small triangles, which means the surfaces are not perfectly smooth, but this method of building surfaces is easy to work with and allows for colouring to help the viewer see what is going on.

You can change which function is plotted by changing `f` in the code. Note that there are a few pre-written functions available to use.

## Screenshots

Just the axes

![Just the axes](https://user-images.githubusercontent.com/48631759/200191818-84a73bac-3921-4c0c-9392-7146d5814f7a.png)

Axes with domain planes

![Axes with domain planes](https://user-images.githubusercontent.com/48631759/200191837-401eb65b-6419-4d94-911f-c4e3af459125.png)

exp(z) applied to the domain plane

![exp(z) applied to the domain plane](https://user-images.githubusercontent.com/48631759/200191954-6b3af1cd-fdf6-4670-9217-b3f19a8f0214.png)
