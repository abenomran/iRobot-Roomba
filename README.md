# iRobot Create 3 Roomba Programming

<p align="center">
  <img src="images/irobot_physical1.png" alt="iRobot Hardware Image 1" width="400"/>
  <img src="images/irobot_physical2.png" alt="iRobot Hardware Image 2" width="400"/>
</p>

## Overview

This project involves programming the **iRobot Create 3 Roomba** to achieve multiple advanced functionalities. As the first-ever student at Georgia Tech to complete this project, I spearheaded a team in developing the iRobot Create 3 program functionality and worked closely with Dr. Rodrigo Borela (all lab creation credit due to him) to tailor his instruction for the first-time launch of the lab. 

By leveraging Python, the iRobot SDK, and the Roomba's onboard sensors, we developed a series of features that significantly enhance the Roomba's operational capabilities. These enhancements include password protection, ping pong functionality, object detection, collision warning/avoidance, and a dynamic maze-solving algorithm.

## Features

<h5>Password Protection:</h5>
<p>Implemented a secure access mechanism to control and restrict the use of the Roomba, ensuring that only authorized users can operate the device.</p>

<p align="center">
  <img src="images/irobot_sensation.png" alt="iRobot Sensors" width="400"/>
  <img src="images/irobot_barrier_detection.png" alt="iRobot Barrier Detection" width="400"/>
</p>

**Infrared Sensors:** Utilized the Roomba's front-mounted IR sensors to implement an object collision detection system. This system allows the Roomba to sense obstacles in real-time, enabling it to navigate around objects and avoid collisions, ensuring smooth operation and protecting both the device and its surroundings.

<p align="center">
  <img src="images/irobot_pingpong.png" alt="iRobot Ping Pong Functionality" width="400"/>
</p>

**Ping Pong Functionality:** Developed a unique feature where the Roomba can engage in a simple ping pong interaction, showcasing the versatility of its motion and sensor capabilities.

<p align="center">
  <img src="images/irobot_positioning.png" alt="iRobot Positioning" width="400"/>
  <img src="images/irobot_reflection.png" alt="iRobot Reflection" width="400"/>
</p>

**Object Detection and Collision Avoidance:** Utilized the Roomba's infrared (IR) sensors to detect obstacles in its path. The system not only warns the user of potential collisions but also employs an algorithm to autonomously navigate around obstacles, preventing accidents and ensuring smooth operation.

<p align="center">
  <img src="images/irobot_maze1.png" alt="iRobot Maze Solving Image 3" width="400"/>
  <img src="images/irobot_maze2.png" alt="iRobot Maze Solving Image 4" width="400"/>
</div>
<p align="center">
  <img src="images/irobot_maze3.png" alt="iRobot Maze Solving Image 3" width="400"/>
  <img src="images/irobot_maze4.png" alt="iRobot Maze Solving Image 4" width="400"/>
</div>

**Dynamic Maze Solving Algorithm with Cost Analysis:** Designed and implemented a sophisticated algorithm that leverages the Roomba's Cartesian coordinate navigation system, incorporating a cost analysis function. This allows the Roomba to navigate and solve complex mazes dynamically by assigning a cost to each cell in the maze. The algorithm evaluates these costs, taking into account factors such as distance and obstacles, to calculate the optimal path in real-time. By analyzing and minimizing the total cost of different routes, the Roomba efficiently adapts to various maze configurations and finds the most efficient path from start to finish.

