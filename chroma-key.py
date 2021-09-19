import requests
import cv2
import numpy as np

class Image:

    def __init__(self, image_array) -> None:
        self.image_array = image_array

    def show_image(self):
        cv2.imshow('', self.image_array)
        cv2.waitKey()


    def __create_mask(self):
        hsv = cv2.cvtColor(self.image_array, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (36,55,10), (70,255,255))
        return mask

    def show_silhouette(self):
        mask = self.__create_mask()
        cv2.imshow('', mask)
        cv2.waitKey()

    def __create_erosion(self, mask):
        ret, thresh = cv2.threshold(mask, 127,255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((1,1), np.uint8)
        erosion = cv2.erode(thresh, kernel)
        return erosion

    def invert_image(self):
        mask = self.__create_mask()
        erosion = self.__create_erosion(mask)
        cv2.imshow('', erosion)
        cv2.waitKey()

    def add_background(self, ):
        mask = self.__create_mask()
        erosion = self.__create_erosion(mask)
        imask = erosion == 255
        green = np.zeros_like(self.image_array, np.uint8)
        green[imask]= self.image_array[imask]
        cv2.imshow('', green)
        cv2.waitKey()
        

get_image = requests.get('https://i.stack.imgur.com/Fq8hA.png', stream=True).raw
vetor_image =  np.asarray(bytearray(get_image.read()), dtype="uint8")
decoded_image = cv2.imdecode(vetor_image, cv2.IMREAD_COLOR)




image = Image(decoded_image)
image.show_image()
image.show_silhouette()
image.invert_image()
image.add_background()


