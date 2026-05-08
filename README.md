# Lunar Rover FSM Navigation

A ROS 2 + Gazebo project for autonomous lunar rover navigation using a finite-state machine (FSM) and LiDAR sensing.

This repository is organized as a clean robotics-simulation project, with separate folders for worlds, launch files, scripts, documentation, and source code.

## Repository Structure

```text
lunar_rover_github_scaffold/
├── .github/workflows/          # CI placeholders
├── assets/figures/             # report figures, screenshots, diagrams
├── config/                     # thresholds, gains, rover params
├── docs/                       # architecture and setup notes
├── launch/                     # ROS 2 launch files
├── scripts/                    # helper scripts for setup and running
├── src/
│   ├── fsm_controller/         # rover FSM controller package
│   └── path_logger/            # path logging package
├── worlds/                     # Gazebo world files
├── .gitignore
└── README.md
```

## Features

- Sector-based LiDAR processing
- FSM navigation states: goal seek, obstacle detected, turn, bypass, goal reacquire
- Gazebo-based lunar terrain simulation
- ROS 2 topic-based modular design
- Path logging for evaluation

## Suggested Workflow

1. Put your ROS 2 Python packages inside `src/`
2. Put your Gazebo `.sdf` world files inside `worlds/`
3. Put figures for your report inside `assets/figures/`
4. Use the scripts in `scripts/` to build and launch the project

## Core Topics

- `/scan` — LiDAR input
- `/cmd_vel` — rover velocity commands
- `/odom` — rover odometry

## Notes


