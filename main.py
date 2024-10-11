import pybullet as p
import pybullet_data
import tkinter as tk
from tkinter import ttk

# Initialize PyBullet simulation
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Load URDF from standard directory

# Load your robot URDF with the base fixed
robot_id = p.loadURDF("example.urdf", useFixedBase=True)  # Add useFixedBase=True

# Get number of joints in the robot
num_joints = p.getNumJoints(robot_id)

# Create a simple GUI using Tkinter
class JointControlApp:
    def __init__(self, root, angle_window):
        self.root = root
        self.angle_window = angle_window
        self.root.title("Robot Joint Control")
        self.sliders = []
        self.joint_angle_labels = []
        self.recorded_positions = []  # List to store recorded positions
        
        # Create sliders for each joint
        for joint_index in range(num_joints):
            joint_info = p.getJointInfo(robot_id, joint_index)
            joint_name = joint_info[1].decode('utf-8')
            joint_lower_limit = joint_info[8]
            joint_upper_limit = joint_info[9]
            
            # Create label and slider
            label = tk.Label(root, text=f"Joint {joint_index}: {joint_name}")
            label.pack()
            slider = tk.Scale(root, from_=joint_lower_limit, to=joint_upper_limit, orient=tk.HORIZONTAL, length=300, command=lambda val, j=joint_index: self.update_joint_position(j, val))
            slider.pack()
            self.sliders.append(slider)
            
            # Create label for joint angles in the second window
            joint_angle_label = tk.Label(angle_window, text=f"Joint {joint_index}: {joint_name} - Angle: 0.0")
            joint_angle_label.pack()
            self.joint_angle_labels.append(joint_angle_label)

        # Add a "Record Position" button
        record_button = tk.Button(root, text="Record Position", command=self.record_position)
        record_button.pack()

        # Create a label for displaying recorded positions in the second window
        self.recorded_positions_label = tk.Label(angle_window, text="Recorded Positions: None")
        self.recorded_positions_label.pack()

        # Create a dropdown (combobox) to select recorded positions
        self.position_selector = ttk.Combobox(angle_window, state="readonly")
        self.position_selector.pack()
        
        # Add a button to move to selected recorded position
        move_button = tk.Button(angle_window, text="Move to Selected Position", command=self.move_to_selected_position)
        move_button.pack()

    # Update the robot joint position in the PyBullet simulation
    def update_joint_position(self, joint_index, slider_value):
        p.setJointMotorControl2(bodyUniqueId=robot_id, jointIndex=joint_index, controlMode=p.POSITION_CONTROL, targetPosition=float(slider_value))
        
    # Update the joint angles in the second window
    def update_joint_angles(self):
        for joint_index in range(num_joints):
            joint_state = p.getJointState(robot_id, joint_index)
            joint_angle = joint_state[0]
            joint_info = p.getJointInfo(robot_id, joint_index)
            joint_name = joint_info[1].decode('utf-8')
            
            # Update the text in the angle label
            self.joint_angle_labels[joint_index].config(text=f"Joint {joint_index}: {joint_name} - Angle: {joint_angle:.2f}")
    
    # Record the current joint positions
    def record_position(self):
        current_positions = []
        for joint_index in range(num_joints):
            joint_state = p.getJointState(robot_id, joint_index)
            joint_angle = joint_state[0]
            current_positions.append(joint_angle)
        
        self.recorded_positions.append(current_positions)
        print(f"Recorded position: {current_positions}")
        
        # Update the recorded positions label in the second window
        self.update_recorded_positions_label()

    # Update the recorded positions display in the second window
    def update_recorded_positions_label(self):
        positions_text = "\n".join([f"Position {i + 1}: {pos}" for i, pos in enumerate(self.recorded_positions)])
        if positions_text:
            self.recorded_positions_label.config(text=f"Recorded Positions:\n{positions_text}")
            # Update the combobox with new recorded positions
            self.position_selector['values'] = [f"Position {i + 1}" for i in range(len(self.recorded_positions))]
            self.position_selector.set("Select a Position")
        else:
            self.recorded_positions_label.config(text="Recorded Positions: None")

    # Move the robot to the selected recorded position
    def move_to_selected_position(self):
        selected_index = self.position_selector.current()
        if selected_index >= 0:
            selected_position = self.recorded_positions[selected_index]
            for joint_index in range(num_joints):
                p.setJointMotorControl2(bodyUniqueId=robot_id, jointIndex=joint_index, controlMode=p.POSITION_CONTROL, targetPosition=selected_position[joint_index])

# Main loop
root = tk.Tk()
angle_window = tk.Toplevel(root)  # Create a second window for joint angles and recorded positions
angle_window.title("Joint Angles & Recorded Positions")

app = JointControlApp(root, angle_window)

def update_pybullet():
    p.stepSimulation()
    app.update_joint_angles()  # Update the joint angles in the second window
    root.after(50, update_pybullet)  # Run PyBullet simulation in the background

update_pybullet()
root.mainloop()

# Disconnect PyBullet after closing the window
p.disconnect()
