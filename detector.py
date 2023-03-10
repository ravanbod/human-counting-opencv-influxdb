import cv2


class Detector:
    def __init__(self):
        self.hogcv = cv2.HOGDescriptor()
        self.hogcv.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, frame):
        bounding_box_cordinates, weights = self.hogcv.detectMultiScale(
            frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
        person = 1
        for x, y, w, h in bounding_box_cordinates:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f'person {person}', (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person += 1

        cv2.putText(frame, 'Status : Detecting ', (40, 40),
                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
        cv2.putText(frame, f'Total Persons : {person-1}',
                    (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
        return frame, person-1
