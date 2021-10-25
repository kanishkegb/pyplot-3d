# Plotting 3D Objects with Matplotlib


![UAV](media/video.gif)

A Python class for drawing a 3D objects using Python Matplotlib library.

## How to Use

1. Add this as a submodule.
    ```sh
    cd /directory/where/you/have/your/python/files
    git submodule add https://github.com/kanishkegb/pyplot-3d.git ./pyplot3d
    ```
    Alternatively, you can download the repo as a zip file, extract it, rename it to `pyplot3d`, and move it your directory with python codes.
1. Use the library in your code.
    ```python
    import pyplot3d.uav
    import matplotlib.pyplot as plt

    plt.style.use('seaborn')

    # initialize plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    arm_length = 0.24  # in meters
    uav = Uav(ax, arm_length)

    uav.
    ```