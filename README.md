# ximea-py

This module provides a python interface to XIMEA cameras. It is simply a repackaging of XIMEA's python drivers available [at their page](https://www.ximea.com/downloads/recent/XIMEA_Linux_SP.tgz) (package/api/Python/v3/ximea) in order to allow for easier installation with pip, e.g. into virtual or conda environments. Windows support was added too by including xiAPI's Windows libraries.

# Prerequisites

## Windows

1. Download and install [XIMEA Windows Software Package](https://www.ximea.com/support/wiki/apis/XIMEA_Windows_Software_Package)
2. Make sure the camera is connected and recognized in xiCOP (XIMEA CameraControl Tool)

## Linux

1. Download and install [XIMEA Linux Software Package](https://www.ximea.com/support/wiki/apis/XIMEA_Linux_Software_Package)
2. Add users that will use the camera to the "plugdev" group:

    ```bash
    sudo usermod -aG plugdev <myuser>
    ```

# Installation

Install with:

```bash
pip install ximea-py
```

and use like so:

```python
import ximea.xiapi

ximea.xiapi.Camera()
...
```
