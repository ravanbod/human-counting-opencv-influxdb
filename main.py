import detector
import image_detection
import video_detection
import camera_detection
import argparse

# Parsing arguments
arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("-v", "--video", default=None)
arg_parse.add_argument("-i", "--image", default=None)
arg_parse.add_argument("-o", "--output", type=str)
arg_parse.add_argument("-c", "--camera", default=False)
arg_parse.add_argument("--influxdburl", default=None)
arg_parse.add_argument("--influxdbtoken", default=None)
arg_parse.add_argument("--influxdborg", default=None)
arg_parse.add_argument("--influxdbbucketname", default=None)
args = vars(arg_parse.parse_args())


frame_detector = detector.Detector()

if args['image'] != None and args['output'] != None:
    image_detection_obj = image_detection.ImageDetector(
        frame_detector, args['image'], args['output'])
    image_detection_obj.process()
elif args['video'] != None and args['output'] != None:
    video_detection_obj = video_detection.VideoDetector(
        frame_detector, args['video'], args['output'])
    video_detection_obj.process()
elif args['camera'] != None:
    camera_detection_obj = camera_detection.CameraDetector(
        frame_detector, args['influxdburl'], args['influxdbtoken'], args['influxdborg'], args['influxdbbucketname'])
    camera_detection_obj.process()
