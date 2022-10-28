# ximea-py

This module provides a python interface to XIMEA cameras. It is simply a repackaging of XIMEA's python drivers available at https://www.ximea.com/downloads/recent/XIMEA_Linux_SP.tgz (package/api/Python/v3/ximea) in order to allow for easier installation with pip, e.g. into virtual or conda environments.

# Installation

On Linux, add users that will use the camera to the "plugdev" group:

`sudo usermod -aG plugdev <myuser>`

Install with:

`pip install git+https://github.com/jacobfeder/ximea-py.git`

and use like so:

```
import ximea.xiapi

ximea.xiapi.Camera()
...
```
