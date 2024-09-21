# iRobot Create3 Roomba Programming

<p align="center">
  <img src="images/irobot_physical1.png" alt="iRobot Hardware Image 1" width="400"/>
  <img src="images/irobot_physical2.png" alt="iRobot Hardware Image 2" width="400"/>
</p>

## Overview

This project involves programming the **iRobot Create3 Roomba** to achieve multiple advanced functionalities. By leveraging Python, the iRobot SDK, and the Roomba's onboard sensors, we developed a series of features that significantly enhance the Roomba's operational capabilities. These enhancements include password protection, ping pong functionality, object detection, collision warning/avoidance, and a dynamic maze-solving algorithm.

## Features

**Password Protection:** Implemented a secure access mechanism to control and restrict the use of the Roomba, ensuring that only authorized users can operate the device.

<img src="images/irobot_sensation.png" alt="iRobot Sensors" width="400"/>
**Infrared Sensors:** Utilized the Roomba's front-mounted IR sensors to implement an object collision detection system. This system allows the Roomba to sense obstacles in real-time, enabling it to navigate around objects and avoid collisions, ensuring smooth operation and protecting both the device and its surroundings.

<img src="images/irobot_pingpong.png" alt="iRobot Ping Pong Functionality" width="400"/>
**Ping Pong Functionality:** Developed a unique feature where the Roomba can engage in a simple ping pong interaction, showcasing the versatility of its motion and sensor capabilities.

<p align="center">
  <img src="images/irobot_positioning.png" alt="iRobot Positioning" width="300"/>
  <img src="images/irobot_reflection.png" alt="iRobot Reflection" width="300"/>
  <img src="images/irobot_barrier_detection.png" alt="iRobot Barrier Detection" width="300"/>
</p>

**Object Detection and Collision Avoidance:** Utilized the Roomba's infrared (IR) sensors to detect obstacles in its path. The system not only warns the user of potential collisions but also employs an algorithm to autonomously navigate around obstacles, preventing accidents and ensuring smooth operation.

<div>
  <img src="images/irobot_maze1.png" alt="iRobot Maze Solving Image 1" width="230"/>
  <img src="images/irobot_maze2.png" alt="iRobot Maze Solving Image 2" width="230"/>
  <img src="images/irobot_maze3.png" alt="iRobot Maze Solving Image 3" width="230"/>
  <img src="images/irobot_maze4.png" alt="iRobot Maze Solving Image 4" width="230"/>
</div>

**Dynamic Maze Solving Algorithm:** Designed and implemented a sophisticated algorithm that leverages the Roomba's Cartesian coordinate navigation system. This allows the Roomba to navigate and solve complex mazes dynamically. The Roomba adapts to different maze configurations, efficiently finding its way from start to finish by mapping out the maze and calculating the optimal path in real-time.

