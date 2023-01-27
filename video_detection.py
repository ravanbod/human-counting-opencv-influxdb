import cv2
import imutils

class VideoDetector:
    def __init__(self, detector, file_path, output_path):
        self.file_path = file_path
        self.output_path = output_path
        self.detector = detector
        self.writer = cv2.VideoWriter(
            output_path, cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))

    def process(self):
        video = cv2.VideoCapture(self.file_path)
        check, frame = video.read()
        if check == False:
            print('Error in loading video file')
            return
        print('detecting')
        while video.isOpened():
            check, frame = video.read()
            if check:
                frame = imutils.resize(frame, width=min(800, frame.shape[1]))
                frame, _ = self.detector.detect(frame)         
                self.writer.write(frame)
                cv2.imshow('output', frame)
                if cv2.waitKey(1) == ord('q'):
                    break
                
            else:
                break
        video.release()
