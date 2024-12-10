import matplotlib.pyplot as plt
import braille_plot as bp
import numpy as np

bp.set_default_styles(plt)
fig, ax = bp.figure(plt,title="eample plot")


x = np.linspace(-3, 3)
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")
ax.plot(x, x, **bp.line_style_solid(), label="l 1")
ax.plot(x, x + 1.5, **bp.line_style_thick(), label="l 2")
ax.plot(x, -x, **bp.line_style_dotted(), label="l 3")
ax.plot(x, -x + 1.5, **bp.line_style_dashed(), label="l 4")
ax.plot(x, [0] * len(x), **bp.line_style_dashed2(), label="l 5")
bp.legend(ax,fig)
plt.savefig("braille_demo_lines.png")
plt.clf()

fig, ax = bp.figure(plt,title="eample plot")


x = np.linspace(-3, 3,15)
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")
ax.plot(x, x, **bp.marker_style_square(),label="m 1")
ax.plot(x, x+1.5, **bp.marker_style_circle(), label="m 2")
ax.plot(x, -x, **bp.marker_style_triangle_up(), label="m 3")
ax.plot(x, x+1.5, **bp.marker_style_diamond(), label="m 4")
bp.legend(ax,fig)

plt.savefig("braille_demo_markers.png")
