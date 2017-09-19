import matplotlib.pyplot as plt
import numpy as np
import aplpy


# Convert all images to common projection
aplpy.make_rgb_cube(['C:/Users/chaowang/r.fits','C:/Users/chaowang/g.fits','C:/Users/chaowang/u.fits'], 'rgb.fits')

# Make 3-color image
aplpy.make_rgb_image('rgb.fits', 'rgb.png',
                     vmin_r=20, vmax_r=400,
                     vmin_g=0, vmax_g=150,
                     vmin_b=-2,vmax_b=50)

# Create a new figure
fig = aplpy.FITSFigure('rgb.fits')

# Show the RGB image
fig.show_rgb('rgb.png')

# Add contours
fig.show_contour('sc.fits', cmap='gist_heat', levels=[0.2,0.4,0.6,0.8,1.0])

# Overlay a grid
fig.add_grid()
fig.grid.set_alpha(0.5)

# Save image
fig.save('plot.png')