# colourwheel-complex-plotter
This code will visualize functions in the complex plane.


#### what is a complex colourwheel plot?

colourwheel is a way of plotting a complex function. this is done by assinging a colour to all complex numbers. The hue is proportional to the angle between the positive real axis and the point, the lightness to the absolute value (=e**(-ln(1+|z|)) )
A plot of all complex numbers between -5-5i and 5+5i is:

![plot of z](http://i.imgur.com/93XmvAR.png)

#### how to use

open the file (colourwheel-complex-plotter.py) and execute. Now the function plot is avaidable.

syntax: `plot("function",minimum real value,maximum real value, minimum imaginairy value,maximum imaginary value, resolution)`.
The function (as string) gets executed for every pixel. The coordinates of said pixel wil be stored in the variable z (in the form of a complex float number) and as a and b were a+bi=z. 

For example, to plot the function sin(z) one would use:

`plot("cmath.sin(z)",-5,5,-5,5,25)`

would give the folowing image:

![plot of sin(z)](http://i.imgur.com/Dwa1759.png)

I also made a plot of a few zeroes of the zeta-function. I used the mpmath module:
```
import mpmath
plot("float(mpmath.zeta(z).real)+i*float(mpmath.zeta(z).imag)",-1,2,0,35,22.5)
```
[plot of zeta function](http://i.imgur.com/v5t63eX.png)

#### controls

- Press left mouse on the sreen to get the coordinates and the returned value.
- Press [S] to save the current plot, a popup will apear to choose a path. The graph wil by default save as .png image.
- Press [=] to zoom in, centering on the mouse position. By default it zooms in with a factor of 1.5, however this can easyly be changed using `zoomFactor=`. The command to get directly to the zoomed in state will be printed.
- Press [-] to zoom out, centering on the mouse position. By default it zooms out with the zoomFactor. The command to get directly to the zoomed out state will be printed.
- Press [PAGE UP] to increase the resolusion by the zoomFactor. 
- Press [PAGE DOWN] to decrease the resolusion by the zoomFactor. 
- Press [ESC] to close the window and stop the program.
