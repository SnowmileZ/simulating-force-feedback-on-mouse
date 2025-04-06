# Mouse Force Feedback Simulation

This project explores an innovative approach to simulating force feedback using telemetry data from Assetto Corsa’s shared memory. The objective is to use real-time force feedback data and translate it into virtual mouse axis input via **vJoy**. This adjusted input is then fed back into the simulator to manipulate the virtual steering wheel's position—creating a unique attempt at mimicking force feedback using only a mouse.

While the system has been partially implemented, full functionality is still a work in progress. Current results show promise but require further tuning and optimization to achieve realistic force simulation.

## Software Used

- **vJoy**: A virtual joystick driver used to emulate controller inputs.
- **AutoHotkey**: Utilized to hide the mouse cursor during operation.
- **FreePIE (Programmable Input Emulator)**: Used for scripting and managing input mappings and force feedback translation.

## Content manager Control Scheme 
   select wheel as an input method

### Axis Assignments
- **Axis 1**: Steering (mouse drag)
- **Axis 2**: Throttle (controlled via `Q`, `W`, `E` keys to adjust throttle levels)
- **Axis 3**: Clutch (`Left Shift`)
- **Axis 6**: Brake (`Ctrl` + Mouse Scroll Wheel)

### Button Mappings (Used as Shifters)
- **Button 1**: Previous gear (Mouse left-click)
- **Button 2**: Next gear (Mouse right-click)

### Additional Control (Combine with Keyboard)
- **Spacebar**: Handbrake

## Project Overview

Using Assetto Corsa's shared memory telemetry, this project aims to simulate force feedback on a standard mouse. For example, when a force is applied to the virtual steering wheel making it turn left, the simulation requires the user to drag the mouse left to countersteer. This emulates the natural reaction needed in a real driving scenario.

## Getting Started

1. **Assetto Corsa Configuration**:  
   Ensure that Assetto Corsa is set up to output telemetry data via shared memory (the game already do this by default).

2. **Install vJoy**:  
   Download and install the latest vJoy driver from the [vJoy website](http://vjoystick.sourceforge.net).

3. **Install FreePIE**:  
   Download and install FreePIE from its official source.

4. **Run the python Script**:  
   Run the mouse_ffb_script.py using freepie.
   
5. **Run MouseHider**:  
   A standalone AHK app that toggles the visibility of the mouse cursor during simulation by clicking the middle mouse button.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
