import cv2
import imutils
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import ASYNCHRONOUS


class CameraDetector:
    def __init__(self, detector, influxdb_url=None, influxdb_token=None, influxdb_org=None, influxdb_bucket_name=None):
        self.detector = detector
        self.influx_client = None
        if influxdb_url is not None:
            self.influxdb_url = influxdb_url
            self.influxdb_token = influxdb_token
            self.influxdb_org = influxdb_org
            self.influxdb_bucket_name = influxdb_bucket_name
            self.influx_client = InfluxDBClient(
                url=influxdb_url, token=influxdb_token, org=influxdb_org)
            self.influx_write_api = self.influx_client.write_api(
                write_options=ASYNCHRONOUS)

    def process(self):
        video = cv2.VideoCapture(0)
        while True:
            check, frame = video.read()
            if check:
                frame = imutils.resize(frame, width=min(800, frame.shape[1]))
                frame, total_persons = self.detector.detect(frame)
                cv2.imshow('output', frame)
                if self.influx_client is not None:
                    self.influx_write_api.write(self.influxdb_bucket_name, self.influxdb_org, [
                                                "persons,location=location persons={}".format(total_persons).encode()])

                if cv2.waitKey(1) == ord('q'):
                    break

        video.release()
