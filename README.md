# Python-UAV-Plot


![Landing](media/video.gif)

A Python class for drawing a UAV using Python Matplotlib library.
Please note that this is not a real-time plot.
Once you have simulation data for the UAV position and attitude, that can use them for visualization.

## How to Use

### Python
```python
import matplotlib.pyplot as plt
from uav import UavPlot

plt.style.use('seaborn')

# initialize plot
fig = plt.figure()
ax = fig.gca(projection='3d')

arm_length = 0.24  # in meters
uav_plot = UavPlot(ax, arm_length)

# update the plot
ani = animation.FuncAnimation(fig, update_plot, frames=steps, \
        fargs=(x, R,))
    
plt.show()
```
