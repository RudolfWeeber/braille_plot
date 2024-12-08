import matplotlib.pyplot as plt
import braille_plot as bp
import numpy as np

bp.set_default_styles(plt)
fig, ax = bp.figure(plt,title="eample plot")


x = np.linspace(-3, 3)
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")
ax.plot(x, x, **bp.line_style_solid())
ax.plot(x, x + 1.5, **bp.line_style_thick())
ax.plot(x, -x, **bp.line_style_dotted())
ax.plot(x, -x + 1.5, **bp.line_style_dashed())
ax.plot(x, [0] * len(x), **bp.line_style_dashed2())
plt.savefig("braille_demo_lines.svg")
plt.clf()

fig, ax = bp.figure(plt,title="eample plot")


x = np.linspace(-3, 3,15)
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")
ax.plot(x, x, **bp.marker_style_square())
ax.plot(x, x+1.5, **bp.marker_style_circle())
ax.plot(x, -x, **bp.marker_style_triangle_up())
ax.plot(x, x+1.5, **bp.marker_style_diamond())

plt.savefig("braille_demo_markers.svg")
