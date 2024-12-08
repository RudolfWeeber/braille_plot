
import matplotlib.pyplot as plt
import numpy as np

def set_default_styles(plt):
    """
    Set default matplotlib parameters for font sizes and other plot aesthetics.
    """
    plt.rcParams.update({
        'svg.fonttype': "none",
        'font.size': 30,           # Set global font size for readability
        'axes.titlesize': 30,      # Title font size
        'axes.labelsize': 30,      # Axis label font size
        'xtick.labelsize': 30,     # X-axis tick font size
        'ytick.labelsize': 30,     # Y-axis tick font size
        'legend.fontsize': 30      # Legend font size
    })

def configure_axes(ax):
    """
    Configure the axis settings for major ticks, padding, and labels.
    
    Parameters:
    ax (matplotlib.axes.Axes): The axes object to configure.
    """
    # Configure major ticks
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))  # Limit to 5 major ticks on the X axis
    ax.yaxis.set_major_locator(plt.MaxNLocator(5))  # Limit to 5 major ticks on the Y axis

    # Padding adjustments
    ax.xaxis.labelpad = 20  # Adjust padding for X-axis
    ax.yaxis.labelpad = -10  # Adjust padding for Y-axis
    ax.tick_params(axis='y', pad=30)

def line_style_solid():
    """ Return parameters for a solid line style. """
    return {'linestyle': '-', 'color': 'k', 'linewidth': 5}

def line_style_thick():
    """ Return parameters for a thicker solid line style. """
    return {'linestyle': '-', 'color': 'k', 'linewidth': 12}

def line_style_dotted():
    """ Return parameters for a dotted line style. """
    return {'linestyle': ':', 'color': 'k', 'linewidth': 4}

def line_style_dashed():
    """ Return parameters for a dashed line style. """
    return {'linestyle': '--', 'color': 'k', 'linewidth': 4}

def line_style_dashed2():
    """ Return parameters for a custom dash pattern. """
    return {'linestyle': (0, (5, 5)), 'color': 'k', 'linewidth': 3}

def marker_style_circle():
    """ Return parameters for a circular marker style suitable for Braille printing. """
    return {'marker': 'o', 'markersize': 10,"linestyle":""}  # ~3-4 mm size

def marker_style_square():
    """ Return parameters for a square marker style suitable for Braille printing. """
    return {'marker': 's', 'markersize': 10, "linestyle":""}  # ~3-4 mm size

def marker_style_triangle_up():
    """ Return parameters for an upward-pointing triangle marker style. """
    return {'marker': '^', 'markersize': 10, "linestyle": ""}  # ~3-4 mm size

def marker_style_diamond():
    """ Return parameters for a diamond marker style suitable for Braille printing. """
    return {'marker': 'D', 'markersize': 10,"linestyle": ""}  # ~3-4 mm size


def figure(plt, title=""):
        fig, ax = plt.subplots(figsize=(12,10))
        configure_axes(ax)
        ax.set_title(title, loc="left", pad=30)
        return fig, ax
