
import matplotlib.pyplot as plt
import braille_plot as bp
import numpy as np

bp.set_default_styles(plt)
fig, ax = bp.figure(plt, title="eample plot")


x = np.linspace(-3, 3)
ax.set_xlabel("x-axis Label")
ax.set_ylabel("y-axis Label")
ax.plot(x, x**2, **bp.line_style_solid(), label="parab")
ax.plot(x, x, **bp.line_style_thick(), label="lin")
bp.legend(ax, fig)
plt.savefig("two_func.png")
