import detector
import image_detection
import video_detection


frame_detector = detector.Detector()
image_detection_obj = image_detection.ImageDetection(frame_detector, 'pic.png', 'output.png')
image_detection_obj.process()

video_detection_obj = video_detection.VideoDetector(frame_detector, 'vid.mp4', 'output.mp4')
video_detection_obj.process()