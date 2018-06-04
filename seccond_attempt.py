import clr
from pprint import pformat
import System
from System.Reflection import *

analogMap = []
global analogMap
jogMap = []
global jogMap
buttonMap = []
global buttonMap

def analog(midiNum, analogNum, stick, axis):
  analogMap.append([midiNum, analogNum, stick, axis]) 

def jog(midiNum, knobNum, stick, buttonL, buttonR):
  jogMap.append([midiNum, knobNum, stick, buttonL, buttonR]) 

def button(midiNum, buttonNum, stick, button):
  buttonMap.append([midiNum, buttonNum, stick, button]) 

def update():
  # diagnostics.watch(pformat([midi[1].data.status,midi[1].data.buffer]))
  # diagnostics.watch(pformat([midi[2].data.status,midi[2].data.buffer]))
  for a in analogMap:
    [midiNum, analogNum, stick, axis] = a
    midiStatus = midi[midiNum].data.status
    [wantedAnalog, wantedValue] = midi[midiNum].data.buffer
    if midiStatus == MidiStatus.Control and wantedAnalog == analogNum:
      wantedValue = wantedValue - 64
      if wantedValue < 0: wantedValue = float(wantedValue) / 64.0
      elif wantedValue > 0: wantedValue = float(wantedValue) / 63.0
      setattr(vJoy[stick], axis, vJoy[stick].axisMax * wantedValue)
  for j in jogMap:
    [midiNum, knobNum, stick, buttonL, buttonR] = j
    midiStatus = midi[midiNum].data.status
    [wantedKnob, wantedValue] = midi[midiNum].data.buffer
    if midiStatus == MidiStatus.Control and wantedKnob == knobNum:
      if int(wantedValue) < 64: vJoy[stick].setPressed(buttonL)
      if int(wantedValue) > 64: vJoy[stick].setPressed(buttonR)
  for b in buttonMap:
    [midiNum, buttonNum, stick, button] = b
    midiStatus = midi[midiNum].data.status
    [wantedButton, wantedValue] = midi[midiNum].data.buffer
    if wantedButton == buttonNum:
      vJoy[stick].setButton(button, midiStatus == MidiStatus.NoteOn)

if starting:
  # MM1 row 0
  analog(1, 1, 0, 'x') # Out 1
  analog(1, 2, 0, 'y') # Out 2
  button(1, 16, 0, 2) # Left
  jog(1, 3, 0, 0, 1) # Browse
  button(1, 17, 0, 3) # Right
  analog(1, 4, 0, 'z') # Cue Vol
  analog(1, 5, 0, 'rx') # Cue Mix
  # MM1 row 1
  analog(1, 6, 0, 'ry')
  analog(1, 7, 0, 'rz') 
  analog(1, 8, 0, 'slider')
  analog(1, 9, 0, 'dial')
  # MM1 row 2
  analog(1, 10, 1, 'x')
  analog(1, 11, 1, 'y')
  analog(1, 12, 1, 'z')
  analog(1, 13, 1, 'rx')
  # MM1 row 3
  analog(1, 14, 1, 'ry')
  analog(1, 15, 1, 'rz')
  analog(1, 16, 1, 'slider')
  analog(1, 17, 1, 'dial')
  # MM1 row 4
  analog(1, 18, 1, 'x')
  analog(1, 19, 1, 'y')
  button(1, 18, 0, 4) # Seems to be related to the VU meter?
  analog(1, 20, 1, 'z')
  analog(1, 21, 1, 'rx')
  # MM1 row 5 (Slider Outs)
  button(1, 19, 0,  5) # Slider 1 Out 1
  button(1, 20, 0,  6) # Slider 1 Out 2
  button(1, 23, 0,  7) # Slider 2 Out 1
  button(1, 24, 0,  8) # Slider 2 Out 2
  button(1, 27, 0,  9) # Slider 3 Out 1
  button(1, 28, 0, 10) # Slider 3 Out 2
  button(1, 31, 0, 11) # Slider 4 Out 1
  button(1, 32, 0, 12) # Slider 4 Out 2
  # MM1 row 6 (Slider Cues)
  button(1, 48, 0, 13) # Slider 1 Cue
  button(1, 49, 0, 14) # Slider 2 Cue
  button(1, 50, 0, 15) # Slider 3 Cue
  button(1, 51, 0, 16) # Slider 4 Cue
  # MM1 row 7 (Sliders)
  analog(1, 48, 1, 'ry') # Slider 1
  analog(1, 49, 1, 'rz') # Slider 2
  analog(1, 50, 1, 'slider') # Slider 3
  analog(1, 51, 1, 'dial') # Slider 4
  # MM1 row 8
  analog(1, 64, 2, 'x') # Cross-Fader
  # DV1 Bank 0 FX1
  jog(2, 20, 0, 17, 18)
  jog(2, 21, 0, 19, 20)
  jog(2, 22, 0, 21, 22)
  jog(2, 23, 0, 23, 24)
  button(2, 20, 0, 25)
  button(2, 21, 0, 26)
  button(2, 22, 0, 27)
  button(2, 23, 0, 28)
  # DV1 Bank 0 FX2
  jog(2, 24, 0, 29, 30)
  jog(2, 25, 0, 31, 32)
  jog(2, 26, 0, 33, 34)
  jog(2, 27, 0, 35, 36)
  button(2, 24, 0, 37)
  button(2, 25, 0, 38)
  button(2, 26, 0, 39)
  button(2, 27, 0, 40)
  # DV1 Bank 0 FX3
  jog(2, 28, 0, 41, 42)
  jog(2, 29, 0, 43, 44)
  jog(2, 30, 0, 45, 46)
  jog(2, 31, 0, 47, 48)
  button(2, 28, 0, 49)
  button(2, 29, 0, 50)
  button(2, 30, 0, 51)
  button(2, 31, 0, 52)
  # DV1 Bank 0 FX4
  jog(2, 32, 0, 53, 54)
  jog(2, 33, 0, 55, 56)
  jog(2, 34, 0, 57, 58)
  jog(2, 35, 0, 59, 60)
  button(2, 32, 0, 61)
  button(2, 33, 0, 62)
  button(2, 34, 0, 63)
  button(2, 35, 0, 64)
  # DV1 Bank 1 FX1
  jog(2, 36, 0, 65, 66)
  jog(2, 37, 0, 67, 68)
  jog(2, 38, 0, 69, 70)
  jog(2, 39, 0, 71, 72)
  button(2, 36, 0, 73)
  button(2, 37, 0, 74)
  button(2, 38, 0, 75)
  button(2, 39, 0, 76)
  # DV1 Bank 1 FX2
  jog(2, 40, 0, 77, 78)
  jog(2, 41, 0, 79, 80)
  jog(2, 42, 0, 81, 82)
  jog(2, 43, 0, 83, 84)
  button(2, 40, 0, 85)
  button(2, 41, 0, 86)
  button(2, 42, 0, 87)
  button(2, 43, 0, 88)
  # DV1 Bank 1 FX3
  jog(2, 44, 0, 89, 90)
  jog(2, 45, 0, 91, 92)
  jog(2, 46, 0, 93, 94)
  jog(2, 47, 0, 95, 96)
  button(2, 44, 0, 97)
  button(2, 45, 0, 98)
  button(2, 46, 0, 99)
  button(2, 47, 0, 100)
  # DV1 Bank 1 FX4
  jog(2, 48, 0, 101, 102)
  jog(2, 49, 0, 103, 104)
  jog(2, 50, 0, 105, 106)
  jog(2, 51, 0, 107, 108)
  button(2, 48, 0, 109)
  button(2, 49, 0, 110)
  button(2, 50, 0, 111)
  button(2, 51, 0, 112)
  # DV1 Bank 2 (No FX Available)
  jog(2, 64, 0, 113, 114)
  jog(2, 65, 0, 115, 116)
  jog(2, 66, 0, 117, 118)
  jog(2, 67, 0, 119, 120)
  # DV1 Focus Mode
  button(2, 64, 1, 1) # A
  button(2, 65, 1, 2) # B
  button(2, 66, 1, 3) # C
  button(2, 67, 1, 4) # D
  # DV1 Master Mode
  button(2, 68, 1, 5) # A
  button(2, 69, 1, 6) # B
  button(2, 70, 1, 7) # C
  button(2, 71, 1, 8) # D
  # DV1 Double Mode
  button(2, 72, 1, 9) # A 
  button(2, 73, 1, 10) # B
  button(2, 74, 1, 11) # C 
  button(2, 75, 1, 12) # D
  # Time Buttons
  button(2, 80, 1, 13) # 1/16 | 1
  button(2, 81, 1, 14) # 1/8 | 2
  button(2, 82, 1, 15) # 1/4 | 4
  button(2, 83, 1, 16) # 1/2 | 8
  # Sequencing Buttons
  button(2, 84, 1, 17) # Slice
  button(2, 85, 1, 18) # Erase
  button(2, 86, 1, 19) # Store
  button(2, 87, 1, 20) # Phrase
  # Number Buttons
  button(2, 88, 1, 25) # 5
  button(2, 89, 1, 26) # 6
  button(2, 90, 1, 27) # 7
  button(2, 91, 1, 28) # 8
  button(2, 92, 1, 21) # 1
  button(2, 93, 1, 22) # 2
  button(2, 94, 1, 23) # 3
  button(2, 95, 1, 24) # 4
  # Assign the update functions
  midi[1].update += update
  midi[2].update += update

i = 0
devs = []
global devs
while True:
  try: 
    dev = joystick[i]
  except:
    break
  joystick_global = clr.GetClrType(type(dev))
  device = joystick_global.GetField("device", BindingFlags.NonPublic | BindingFlags.Instance)
  di_joystick = device.FieldType.GetField("joystick", BindingFlags.NonPublic | BindingFlags.Instance)
  device_val = device.GetValue(dev)
  joystick_val = di_joystick.GetValue(device_val)
  axes = {}
  for axis in ['x', 'y', 'z', 'xRotation', 'yRotation', 'zRotation', 'sliders']:
    try:
      aval = getattr(dev, axis)
    except:
      continue
    axes[axis] = aval
  axes['buttons'] = []
  j = 0
  while True:
    try: 
      if (dev.getDown(j)):
        axes['buttons'].append(j)
    except: break
    j = j + 1
  devs.append([joystick_val.Properties.InstanceName, axes])
  i = i + 1

diagnostics.watch(pformat(devs))
