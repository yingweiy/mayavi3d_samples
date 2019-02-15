import numpy as np
from mayavi.mlab import *

def test_points3d():
    t = np.linspace(0, 4 * np.pi, 20)

    x = np.sin(2 * t)
    y = np.cos(t)
    z = np.cos(2 * t)
    s = 2 + np.sin(t)

    return points3d(x, y, z, s, colormap="copper", scale_factor=.25)


def test_plot3d():
    """Generates a pretty set of lines."""
    n_mer, n_long = 6, 11
    dphi = np.pi / 1000.0
    phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi)
    mu = phi * n_mer
    x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
    y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
    z = np.sin(n_long * mu / n_mer) * 0.5

    l = plot3d(x, y, z, np.sin(mu), tube_radius=0.025, colormap='Spectral')
    return l

def test_volume_slice():
    x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]

    scalars = x * x * 0.5 + y * y + z * z * 2.0

    obj = volume_slice(scalars, plane_orientation='x_axes')
    return obj


test_points3d()
test_plot3d()
test_volume_slice()
show()

