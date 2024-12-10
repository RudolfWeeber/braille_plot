# Braille plot

This provides some helpers to prepare tactile plots using Matplotlib. The resulting .png files, can, for example, be embossed on an Index Everest using the TactileView software

## Embossers and paper size

* This is used with A4 paper on an Index Everest V4 with TactileView V2.5. For other combinations, the template might have to be adapted.
* For different paper sizes, adapt the figure size in `braillle_plot.figure()`. The provided sie is for 270x210mm (A4 landscape)


## Requirements

* Matplotlib 
* also, the Braille29 font needs to be downloaded and placed in the same directory as the braille_plot.py script
* Downlaod the braille font (Braille29.ttf) from e.g., https://tactilegraphics.cs.washington.edu/comp-architecture/

## Usage

```python
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
``` 

* Marker styles such as `braille_plot.marker_style_circle()`  are also provided.
* The styles are also provided as in `braille_plot.line_styles` and `braille_plot.marker_styles`. These can be used, if you just need some line differing styles, but don't need to control which ones exactly.


