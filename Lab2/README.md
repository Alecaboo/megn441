# Lab 2: Simultaneous Localization and Mapping (SLAM)

## Lab Overview

By the end of this lab, you will be able to:

- Install off-the-shelf ROS2 packages
- Build off-the-shelf ROS2 packages
- Visualize sensors using RViz
- Map a room using SLAM

During week 1 of this lab, we will be getting our LiDAR and RGBD cameras working and then visualizing the output using RViz. And then, during week 2, we will use slam_toolbox to map the basement hallway of Brown!

### Lab Procedure

1. Download and install the sllidar_ros2 package from [Slamtec sllidar](https://github.com/Slamtec/sllidar_ros2). Copy this node over to the robot in your workspace, and build it with `colcon build --packages-select sllidar_ros2`. In order to run the node, you will need to locate the address of your Lidar on the robot. It will be in the `/dev/` folder, likely beginning with `/dev/USB` or `/dev/ACM`. You can also list usb devices on the bot to see what's available with `lsusb`. There are two other parameters that we'll need to change from the default node: our `frame_id` should be `lidar_frame` and our `serial_baudrate` should be 115200. Use the ROS2 Humble documentation to figure out how to apply those three parameters in your ros2 run command - they will be flags on your command.
2. While one terminal runs the sllidar node, open another terminal and run

    ```bash
    ros2 run rviz2 rviz2
    ```

    This is RViz, one of the most useful ROS2 tools. With it, we can visualize our robot with its current joint configuration along with all of the sensor readings that our robot is taking in. In order to view those things, we will need to add those displays to our RViz. On the left-hand side of RViz is a panel titled Displays. At the bottom of the panel is a button that says Add. Selecting this option brings up a pop-up with various types of display plugins for RViz. We want to select two now: a `LaserScan` and a `RobotModel`. After adding those, you'll need to click on the dropdown for each within the Displays panel to select the topic that each is subscribed to. We'll also need to update the Fixed Frame in the global options at the top. I recommend choosing `base_footprint` as our fixed frame, as it is the reference frame centered under the robot on the floor. Then, using the File menu, you can save this view as sensors.rviz.
3. Download and install the OrbbecROS2_SDK packages from [OrbbecSDK_ROS2](https://github.com/orbbec/OrbbecSDK_ROS2/tree/main). After you download, you'll need an older version of the repository, so type `git checkout main`. NOTE: When you copy this package over to the robot, it has symbolic links in it (this broke mine). If using rsync to copy files, use the `-l` flag, as in `rsync -rluv` to copy files to the robot. We'll need to change one argument in this launch file - we need `camera_name` to be `depth_cam`. Then we'll use the `dabai_dcw.launch.py` launch file from the `orbbec_camera` package. Once you get this running, add a `DepthCloud` display and a `Camera` display to RViz, finding the relevant topic(s) for each.
4. Write a launch file to run your lidar, your depth camera, and rviz, pulling all relevant parameters, arguments, and RViz configuration file.
5. Use slam_toolbox to map the basement of Brown!

## Lab Grading

The grading of each lab is based 50\% on the successful completion of the lab. For this lab, that 50\% breaks down into:

- 10\% - Get your LiDAR running
- 10\% - Get your RGBD camera running
- 10\% - Visualize your LiDAR and RGBD camera in RViz
- 20\% - Map the basement hallways of Brown

### Lab Report Guidelines

The guidelines below will be used in grading your lab report. Be sure to include everything that the guidelines below mention for full credit!

#### 1. Problem Statement

- Write a succinct 1-3 sentence description of the goals of this lab.

#### 2. Methods

- Briefly describe the Rosbot, including a description of the drivetrain.
- Describe your contributions to the software of the robot for Lab 1.
- Explain 3 topics running on the Rosbots. What is the msg type that is sent to each of those topics? Which nodes publish to or subscribe to each of those topics?

#### 3. Results

- Describe how driving with the keyboard works.
- Include a link to a video of piloting the bot with the keyboard.
- Report on how your controller driving node works.
- Include a link to a video of piloting the bot with the controller.
- Report on what is included in your launch file.
- Include a .zip file of the package you wrote with your submission and describe where in the folder yoru launch file and joystick node can be found.

#### 4. Conclusions

- Discuss the performance of the different approaches to remotely piloting the robot.
- Discuss what your team's biggest lessons learned are from this lab.
- Discuss your current thoughts on pros vs cons of using ROS2 to create a robot.

#### AI Appendix

- Include a 1 paragraph reflection on the questions below, whether or not you used AI.
  - Did you use any AI to support support the completion of this lab? Why or why not?
  - If no, how could it have helped? What did you gain by avoiding AI use?
  - If yes, how was your experience of using it? How did it help? What did you miss out on by using AI?
  - If you used AI, what resources do you think it used in generating its answers?
  - If you used AI, please copy and paste your interactions below:
