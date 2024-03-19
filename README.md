# RGBvis
Python module to create and visualize rgb sequences
## Installation
Make sure you installed python on your machine.
Check [python.org/downloads](https://www.python.org/downloads/) for more information.
Install this package in your terminal via:
```console
pip install --upgrade git+https://github.com/xRamsonx/RGBvis.git
```

## Example


```python
from rgbvis import Sequence

s = Sequence()
#type, duration, endvalue, rgbs="rgb", intensity=1.0
s.add("rising", 10, 1, "rg")
s.add("rising", 10, 1, "b", intensity=4)
s.add("sinking", 5,.5, "gb")
s.add("rising", 5,.5, "r")
s.add("rising", 20,.1, "g")
s.add("linear", 20,.1, "b")
s.add("sinking", 20,.1, "r")
s.add("sinking", 10, 1, "rgb")
s.add("sinking", 5, 0, "rgb")
s.show(np.linspace(0,50,121)).show()
```
