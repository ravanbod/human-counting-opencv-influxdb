import cv2
import imutils


class ImageDetector:
    def __init__(self, detector, file_path, output_path):
        self.file_path = file_path
        self.output_path = output_path
        self.detector = detector

    def process(self):
        image = cv2.imread(self.file_path)
        image = imutils.resize(image, width=min(800, image.shape[1]))
        result_image, _ = self.detector.detect(image)
        cv2.imwrite(self.output_path, result_image)
