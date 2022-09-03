#!/usr/bin/env python
import numpy as np
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError
 
 
bridge = CvBridge()
 
 
def publisher():
    video_capture = cv2.VideoCapture('Video/tennis-ball-video.mp4')
    publisher = rospy.Publisher('tennis_ball_image', Image, queue_size=10)
 
    rospy.init_node('tennis_ball_publisher', anonymous= True)
 
    rate = rospy.Rate(100)
 
    while not rospy.is_shutdown():
        video_capture = cv2.VideoCapture('Video/tennis-ball-video.mp4')
        while not 0xFF == ord('q'):
            ret, frame = video_capture.read()  
            if not ret:
                break
 
            msg = bridge.cv2_to_imgmsg(frame, 'bgr8')
            publisher.publish(msg)
 
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        
    if rospy.is_shutdown():
        video_capture.release()
 
if __name__ == '__main__':
    try: 
        publisher()
    except rospy.ROSInitException:
        pass
