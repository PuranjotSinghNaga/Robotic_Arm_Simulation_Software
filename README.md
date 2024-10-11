# 🤖 Robotic_Arm_Simulation_Software

This is a repositorty for a robotic arm simulations software made using [PyBullet](https://pybullet.org/).

## 🚀Features

- **🎮Real-time simulation**: Control the robotic arm joints using sliders in the GUI.
- 🧭 **Joint angle display**: View the current angle of each joint in a dedicated window.
- 📸 **Record positions**: Capture the current positions of all joints and save them for future use.
- 🔄**Move to recorded positions**: Select and move the robotic arm to previously recorded positions.

## 💻 Requirements

### 🐧 On Linux and 🍎Mac

- Python 3.x
- PyBullet (`pip install pybullet`)
- Tkinter (comes pre-installed with Python on most systems)

### 🪟On Windows

> **_NOTE_:**
> If using Windows it may be viable to use [Anaconda](https://www.anaconda.com/download) and create environments because of installations criteria required for PyBullet.
> You can alternatively install it natively as shown in the docs for PyBullet. [Pybullet docs](https://github.com/bulletphysics/bullet3)
>
> For this project we utilized Conda due to ease of access

#### 1. Setting up Anaconda

we will open `Anaconda Prompt` and create a new environement for the project

```bash
conda create -n myen python
```

you can name the environment as you like, by changing the myen to your wanted name.

Now you can attacth to the environment by using the command

```bash
conda activate myen
```

#### 2. Installing dependencies

now we will isntall the major dependecies for the project

```bash
conda install conda-forge::pybullet
conda install anaconda::tk
conda install anaconda::pyserial
```

## 🏃‍♂️Running the Application

After the dependencies are installed we can run the application by navigating to the application folder and running

```bash
python main.py
```

## 🔍How to Use

### Controlling the Robot Joints

- Use the sliders in the Main Control Window to adjust the angle of each joint.
- The current angle of each joint will be displayed in the Joint Angles & Recorded Positions Window.
  ![The application after running](/assets/main-page.png "Main page")

### Recording Positions

- To record the current joint positions, click the Record Position button in the Main Control Window.
- The recorded positions will be listed in the Joint Angles & Recorded Positions Window, and you can select a position from the dropdown menu to move the robotic arm to that position.
  ![Recording current position of the Robot](/assets/recording.png "Recording position")

  ![Recorded Position of the Robot](/assets/recorded%20.png "Recorded position")

### Moving to a Recorded Position

- Select a recorded position from the dropdown menu in the Joint Angles & Recorded Positions Window.
- Click the Move to Selected Position button to move the robotic arm to the selected position.
  ![Move to a position using the dropdown](/assets/moveto.png "Move To Postion")

## 🛠Left to Do

- [] Add PySerial support
- [] Implement Complete Motion Recording and Replay Playing Feature
- [] Implement a Path Planning Algorithm
- [] Ui Overhaul
