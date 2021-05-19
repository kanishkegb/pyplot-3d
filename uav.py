import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

from utils import ypr_to_R


class Sphere:
    '''
    Draws a sphere at a given position.
    '''

    def __init__(self, ax, r, c='b', x0=np.array([0, 0, 0]).T, resolution=100):
        '''
        Initialize the sphere.

        Params:
            ax: (matplotlib axis) the axis where the sphere should be drawn
            r: (float) radius of the sphere
            c: (string) color of the sphere, default 'b'
            x0: (3x1 numpy.ndarray) initial position of the sphere, default
                is [0, 0, 0]
            resolution: (int) resolution of the plot, default 100

        Returns:
            None
        '''

        self.ax = ax
        self.r = r
        self.color = c
        self.x0 = x0
        self.reso = resolution
    

    def draw(self):
        '''
        Draw the sphere with the initially defined position when the class was
        instantiated.

        Args:
            None
        
        Returns:
            None
        '''

        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]

        x = self.r * np.cos(u) * np.sin(v) + self.x0[0]
        y = self.r * np.sin(u) * np.sin(v) + self.x0[1]
        z = self.r * np.cos(v) + self.x0[2]

        self.ax.plot_surface(x, y, z, color=self.color)
    

    def draw_at(self, position=np.array([0.0, 0.0, 0.0]).T):
        '''
        Draw the sphere at a given position.

        Args:
            position: (3x1 numpy.ndarray) position of the sphere, 
                default = [0.0, 0.0, 0.0]
        
        Returns:
            None
        '''

        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:20j]

        x = self.r * np.cos(u) * np.sin(v) + position[0]
        y = self.r * np.sin(u) * np.sin(v) + position[1]
        z = self.r * np.cos(v) + position[2]

        self.ax.plot_surface(x, y, z, color=self.color)


class Arrow:
    '''
    Draws an arrow at a given position, with a given attitude.
    '''

    def __init__(self, ax, direction, c='b', x0=np.array([0.0, 0.0, 0.0]).T, \
        length=1.0):
        '''
        Initialize the arrow.

        Params:
            ax: (matplotlib axis) the axis where the arrow should be drawn
            direction: (3x1 numpy.ndarray) direction of the arrow
            c: (string) color of the arrow, default = 'b'
            x0: (3x1 numpy.ndarray) origin of the arrow, 
                default = [0.0, 0.0, 0.0]
            length: (float) length of the arrow, default = 1.0

        Returns:
            None
        '''

        self.ax = ax
        self.u0 = direction
        self.color = c
        self.x0 = x0
        self.arrow_length = length
    

    def draw(self):
        '''
        Draw the arrow with the initially defined parameter when the class was
        instantiated.

        Args:
            None
        
        Returns:
            None
        '''

        x = self.x0
        u = self.u0

        self.ax.quiver(x[0], x[1], x[1], \
            u[0], u[1], u[2], \
            color=self.color,
            length=self.arrow_length, \
            normalize=False)
    

    def draw_from_to(self, x=np.array([0.0, 0.0, 0.0]).T, \
        u=np.array([1.0, 0.0, 0.0]).T):
        '''
        Draw the arrow at a given position, with a given direction

        Args:
            x: (3x1 numpy.ndarray) origin of the arrow, 
                default = [0.0, 0.0, 0.0]
            u: (3x1 numpy.ndarray) direction of the arrow, 
                default = [1.0, 0.0, 0.0]
        
        Returns:
            None
        '''
        
        self.ax.quiver(x[0], x[1], x[2], \
            u[0], u[1], u[2], \
            color=self.color,
            length=self.arrow_length, \
            normalize=False)


class Line:
    '''
    Draws a line at a given position, with a given attitude.
    '''

    def __init__(self, ax, direction=np.array([1.0, 0.0, 0.0]).T, \
        c='b', x0=np.array([0.0, 0.0, 0.0]).T):
        '''
        Initialize the line.

        Params:
            ax: (matplotlib axis) the axis where the line should be drawn
            direction: (3x1 numpy.ndarray) direction of the arrow
            c: (string) color of the arrow, default = 'b'
            x0: (3x1 numpy.ndarray) origin of the arrow, 
                default = [0.0, 0.0, 0.0]
                
        Returns:
            None
        '''

        self.ax = ax
        self.u0 = direction
        self.color = c
        self.x0 = x0
    

    def draw(self):
        '''
        Draw the line with the initially defined parameter when the class was
        instantiated.

        Args:
            None
        
        Returns:
            None
        '''
        u = self.u0
        
        self.ax.plot([x[0], u[0]], \
            [x[1], u[1]], \
            [x[1], u[2]], \
            color=self.color)
    

    def draw_from_to(self, x=np.array([0.0, 0.0, 0.0]).T, \
        u=np.array([1.0, 0.0, 0.0]).T):
        '''
        Draw the line at a given position, with a given direction

        Args:
            x: (3x1 numpy.ndarray) origin of the line, 
                default = [0.0, 0.0, 0.0]
            u: (3x1 numpy.ndarray) direction of the line, 
                default = [1.0, 0.0, 0.0]
        
        Returns:
            None
        '''
        
        self.ax.plot([x[0], u[0]], \
            [x[1], u[1]], \
            [x[2], u[2]], \
            color=self.color)


class UavPlot:
    '''
    Draws a quadrotor at a given position, with a given attitude.
    '''

    def __init__(self, ax, arm_length):
        '''
        Initialize the quadrotr plotting parameters.

        Params:
            ax: (matplotlib axis) the axis where the sphere should be drawn
            arm_length: (float) length of the quadrotor arm

        Returns:
            None
        '''

        self.ax = ax
        self.arm_length = arm_length

        self.b1 = np.array([1.0, 0.0, 0.0]).T
        self.b2 = np.array([0.0, 1.0, 0.0]).T
        self.b3 = np.array([0.0, 0.0, 1.0]).T

        # Center of the quadrotor
        self.body = Sphere(self.ax, 0.08, 'y')

        # Each motor
        self.motor1 = Sphere(self.ax, 0.05, 'r')
        self.motor2 = Sphere(self.ax, 0.05, 'g')
        self.motor3 = Sphere(self.ax, 0.05, 'b')
        self.motor4 = Sphere(self.ax, 0.05, 'b')

        # Arrows for the each body axis
        self.arrow_b1 = Arrow(ax, self.b1, 'r')
        self.arrow_b2 = Arrow(ax, self.b2, 'g')
        self.arrow_b3 = Arrow(ax, self.b3, 'b')

        # Quadrotor arms
        self.arm_b1 = Line(ax)
        self.arm_b2 = Line(ax)
    

    def update_plot(self, x=np.array([0.0, 0.0, 0.0]).T, R=np.eye(3)):
        '''
        Draw the quadrotor at a given position, with a given direction

        Args:
            x: (3x1 numpy.ndarray) position of the center of the quadrotor, 
                default = [0.0, 0.0, 0.0]
            R: (3x3 numpy.ndarray) attitude of the quadrotor in SO(3)
                default = eye(3)
        
        Returns:
            None
        '''

        # First, clear the axis of all the previous plots
        self.ax.clear()

        # Center of the quadrotor
        self.body.draw_at(x)

        # Each motor
        self.motor1.draw_at(x + R.dot(self.b1) * self.arm_length)
        self.motor2.draw_at(x + R.dot(self.b2) * self.arm_length)
        self.motor3.draw_at(x + R.dot(-self.b1) * self.arm_length)
        self.motor4.draw_at(x + R.dot(-self.b2) * self.arm_length)

        # Arrows for the each body axis
        self.arrow_b1.draw_from_to(x, R.dot(self.b1) * self.arm_length * 1.8)
        self.arrow_b2.draw_from_to(x, R.dot(self.b2) * self.arm_length * 1.8)
        self.arrow_b3.draw_from_to(x, R.dot(self.b3) * self.arm_length * 1.8)

        # Quadrotor arms
        self.arm_b1.draw_from_to(x, x + R.dot(-self.b1) * self.arm_length)
        self.arm_b2.draw_from_to(x, x + R.dot(-self.b2) * self.arm_length)


if __name__ == '__main__':
    from matplotlib import animation
    
    def update_plot(i, x, R):
        uav_plot.update_plot(x[:, i], R[:, :, i])
        
        # These limits must be set manually since we use
        # a different axis frame configuration than the
        # one matplotlib uses.
        xmin, xmax = -2, 2
        ymin, ymax = -2, 2
        zmin, zmax = -2, 2

        ax.set_xlim([xmin, xmax])
        ax.set_ylim([ymax, ymin])
        ax.set_zlim([zmax, zmin])

    # Initiate the plot
    plt.style.use('seaborn')

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    arm_length = 0.24  # in meters
    uav_plot = UavPlot(ax, arm_length)


    # Create some fake simulation data
    steps = 60
    t_end = 1

    x = np.zeros((3, steps))
    x[0, :] = np.arange(0, t_end, t_end / steps)
    x[1, :] = np.arange(0, t_end, t_end / steps) * 2

    R = np.zeros((3, 3, steps))
    for i in range(steps):
        ypr = np.array([i, 0.1 * i, 0.0])
        R[:, :, i] = ypr_to_R(ypr, degrees=True)


    # Run the simulation
    ani = animation.FuncAnimation(fig, update_plot, frames=steps, \
        fargs=(x, R,))
    
    plt.show()