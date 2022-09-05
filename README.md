
# Object Detection with OpenCV and ROS

In this project I performed 3 different tasks to implement an object detection algoritm on a tennis ball using OpenCV and ROS. 

Task 1:
In the frist task, I read a video file using just OpenCV functionalities(without using ROS) and for each frame read, I applied a ball detection algorithm to detect the ball(s) in the image, displayed the result and continued processing the video until a key was pressed. 


Task 2:
In the second task using OpenCV + ROS, developed a publisher node to read the video stream frame by frame, and publish them through a specific topic.
And developed a subscriber node which subscribes to the image topic of the tennis ball, extracts the image form ROS topic, converts it to an OpenCV image usign cv_bridge. And then applied the ball detection algorithm. 

Task 3: 
In the third task, I did the same thing as Task 2 but the stream was read form a USB camera. 

