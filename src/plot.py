"""Create a basic Bokeh line plot."""


import json
from pathlib import Path

from bokeh import embed, plotting
import numpy


x = numpy.linspace(0, 16, 1_000)
y = numpy.sin(x) + 0.5 * numpy.random.random(1_000) - 0.25

figure = plotting.figure(
    title="Noisy Sine Wave",
    x_axis_label="time",
    y_axis_label="amplitube",
    sizing_mode="scale_height",
)
figure.line(x, y, line_width=2)

output = Path(__file__).parent / "line_plot.json"
with open(output, "w") as fd:
    json.dump(embed.json_item(figure), fd)
