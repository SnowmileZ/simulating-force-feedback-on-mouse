# === simulating-force-feedback-on-mouse ===
# === SnowmileZ ===

import mmap
import struct

# === Shared Memory Setup ===
SHARED_MEMORY_NAME = "Local\\acpmf_physics"
SHARED_MEMORY_SIZE = 312
TELEMETRY_STRUCT_FORMAT = 'f' * 78
FFB_INDEX = 77  # Force Feedback index

# Initialize Shared Memory
shared_memory = mmap.mmap(-1, SHARED_MEMORY_SIZE, SHARED_MEMORY_NAME)
telemetry_struct = struct.Struct(TELEMETRY_STRUCT_FORMAT)

# === Constants ===
INT32_MAX = (2 ** 14) - 1
INT32_MIN = -INT32_MAX

# === Configuration Settings ===
MOUSE_SENSITIVITY = 4.0
SENSITIVITY_CENTER_REDUCTION = 1.0
SCALE = 1000
THROTTLE_INVERSION = BRAKING_INVERSION = CLUTCH_INVERSION = 1
THREAD_INTERVAL = 5  # Execution interval in milliseconds

# === Initialization ===
if starting:
    v = vJoy[0]
    v.x = v.y = v.z = v.rx = v.ry = v.rz = v.slider = v.dial = INT32_MIN
    system.setThreadTiming(TimingTypes.HighresSystemTimer)
    system.threadExecutionInterval = THREAD_INTERVAL

    # Persistent variables (retain state between iterations)
    steering = 0.0
    steering_max = float(INT32_MAX)
    steering_min = float(INT32_MIN)

    throttle_max = INT32_MAX * THROTTLE_INVERSION
    throttle_min = INT32_MIN * THROTTLE_INVERSION
    throttle = throttle_min
    throttle_rate = (throttle_max / (100 / THREAD_INTERVAL))  # Simplified rate calculation

    braking_max = INT32_MAX * BRAKING_INVERSION
    braking_min = INT32_MIN * BRAKING_INVERSION
    braking = braking_min
    braking_rate = (braking_max / (50 / THREAD_INTERVAL))  # Simplified rate calculation

    clutch_max = INT32_MAX * CLUTCH_INVERSION
    clutch_min = INT32_MIN * CLUTCH_INVERSION
    clutch = clutch_min
    clutch_rate = (clutch_max / (50 / THREAD_INTERVAL))  # Simplified rate calculation

# === Button Bindings ===
BUTTON_KEYS = [mouse.leftButton, mouse.rightButton, Key.NumberPad0, Key.NumberPad1, Key.NumberPad2, Key.NumberPad3, Key.NumberPad4, Key.NumberPad5]
for i, key in enumerate(BUTTON_KEYS):
    v.setButton(i, keyboard.getKeyDown(key) if isinstance(key, Key) else key)

# === Read Telemetry Data ===
shared_memory.seek(0)
telemetry_values = telemetry_struct.unpack(shared_memory.read(telemetry_struct.size))
ffb_value = telemetry_values[FFB_INDEX]

# === Steering Logic ===
steering_center_reduction = SENSITIVITY_CENTER_REDUCTION ** (1 - abs(steering / steering_max))
steering += (float(mouse.deltaX) * MOUSE_SENSITIVITY) / steering_center_reduction
steering = max(min(steering, steering_max), steering_min)
v.x = int(round(steering - ffb_value * SCALE))

# === Throttle Logic ===
if keyboard.getKeyDown(Key.Q) and keyboard.getKeyDown(Key.W): 
    throttle_amnt = throttle_max * -0.25
elif keyboard.getKeyDown(Key.Q):
    throttle_amnt = throttle_max * -0.45
elif keyboard.getKeyDown(Key.W) and keyboard.getKeyDown(Key.E): 
    throttle_amnt = throttle_max * 0.4
elif keyboard.getKeyDown(Key.W):
    throttle_amnt = throttle_max * 0.1
elif keyboard.getKeyDown(Key.E):
    throttle_amnt = throttle_max * 1
else:
    throttle_amnt = throttle_min

throttle += throttle_rate if any(keyboard.getKeyDown(k) for k in [Key.Q, Key.W, Key.E]) else -throttle_rate
throttle = max(min(throttle, throttle_amnt), throttle_min)
v.y = throttle

# === Braking Logic ===
if keyboard.getKeyDown(Key.LeftControl):
    braking += braking_rate if mouse.wheelUp else -braking_rate if mouse.wheelDown else 0
else:
    braking -= braking_rate  # Gradual release

braking = max(min(braking, braking_max), braking_min)
v.rz = braking

# === Clutch Logic ===
clutch += clutch_rate if keyboard.getKeyDown(Key.LeftShift) else -clutch_rate
clutch = max(min(clutch, clutch_max), clutch_min)
v.z = clutch

# === Debugging ===
diagnostics.watch(vJoy[0].x)
diagnostics.watch(vJoy[0].y)
diagnostics.watch(vJoy[0].rz)
diagnostics.watch(vJoy[0].z)
diagnostics.watch(ffb_value)
