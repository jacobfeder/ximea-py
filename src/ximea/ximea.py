"""
Ximea camera driver.

Copyright (c) 2022, Jacob Feder
All rights reserved.
"""
import xiapi
import numpy as np

class XIMEA:
    """XIMEA camera wrapper driver."""
    def __init__(self, serial_number=None):
        if serial_number is not None:
            self.driver = xiapi.open_device_by_SN(serial_number)
        else:
            # create instance for first connected camera
            self.driver = xiapi.Camera()

    def connect(self):
        self.driver.open_device()
        # default settings
        # set exposure (us)
        self.driver.set_exposure(100000)
        self.driver.start_acquisition()

    def disconnect(self):
        self.driver.stop_acquisition()
        self.driver.close_device()

    def get_image(self):
        img = xiapi.Image()
        self.driver.get_image(img)
        # get raw data from camera
        # for Python3.x function returns bytes
        data_raw = img.get_image_data_raw()

        # transform data to numpy array
        data = np.array(list(data_raw), dtype=np.uint8).reshape(img.width, img.height)

        return data

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        self.disconnect()

if __name__ == '__main__':
    with XIMEA() as cam:
        print(cam.get_image())
