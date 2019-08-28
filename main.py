import numpy as np
import cv2

class FaceDetector(object):

    def __init__(self, arg):
        super(FaceDetector, self).__init__()
        self.arg = arg

    def run(self,name,number):
        self.name = name
        self.number = number