# tuya-smart-light-manager
Python CLI and webapp to control smart lights through Tuya's cloud platform.

## Intro
Tuya Smart is a platform for smart devices to communicate with the cloud to interface with controls for the smart devices. Several SDKs are available,
including SDKs for the device firmware and for OEM Android/iOS apps. [One API](https://iot.tuya.com/oem/sdk) exposed allows a registered user to control devices
associated with their account, which is used by this application. This API in turn is supported by several SDKs in major languages, including a 
[first-party Python SDK](https://github.com/tuya/tuya-iot-python-sdk/tree/master). Additional SDKs are available from third parties, and this app uses the 
[tinytuya SDK](https://github.com/jasonacox/tinytuya/tree/master/tinytuya).

## Setup
Register an app on the Tuya cloud platform and connect your account.  
Download code on machine with Python 3.  
Install tinytuya (pip install tinytuya).  
Run the tinytuya wizard or manually create tinytuya.json with API keys.  
Launch Python and import ttApp.

## Functionality
### Implemented:
1. ttApp.on(bulb name: string) and .off(...) - Turn light on and off by bulb name.
2. cherryPy integration for on and off - Turn light (hard-coded) on or off upon visiting a URL hosting server component.
3. ttApp.morseCode(bulb name: string, message: string) - Take input string and cause target light to flash dots and dashes to communicate the input string.

### Planned:
2. Support color and scene mode (parity with native app).
1. Light grouping in tree structure by floor, zone, room and fixture (e.g. chandelier, mirror) and functionality to apply a command to all descendents of a node in the tree.
3. Support pre-sets for different scenarios (e.g. "Company", "Day", "Evening", "Night", "Cook", "TV", "Party", "Presentation").
4. Allow replacing disconnected bulb with another by reusing the same name (no updating ids, and no reconfiguring scenes, poweron, etc)
5. Controlled animations in fixtures (e.g. in a circle around a chandelier)
6. Guest access tokens (client cert auth)
7. Easy-bookmark URLs
8. UI - expose selected scenarios (

## Data Model
### Modules:
  - Presets
    - MyPreset(Tag) - call/recurse with other presets. e.g. "Green", "Off", "MyAnimation", "MySceneMode"
  - Scenario
    - MyScenario - Apply preset to tag on command
  - Tag
  - User
  - Utilities
    - Animation (TBD)
    - Flash (duration)
    - Morse (string)
  - Website
### Notes
Tags are ordered (for animation) lists of tags and bulbs. Spatial hierarchy is configured through this.  
Presets are registered as Python functions in a "presets" module. No need for inner platform.  
Site needs a main UI and API. v2 needs a separate UI per user.

## Example Home
\* = "Common space" tag
\^ = "Window View"
\` = "Outside"

#### Loft/top level
  - Pantry A*, B*
  - Kitchen N*^, W*^, E*^
  - Dining Room Overhead*^, Chandelier 1-6*^
  - Loft Curio Cabinet*, Chandelier 1-5*^
  - Tech Center
#### Parlor/main level  
  - Parlor
    - SW*^, NE*^
    - Hallway*
  - Deck\`^
  - Front Bathroom
  - My Bedroom^
  - His Bedroom 
    - NW, SE
    - Bathroom
      - Shower, Mirror 1-22
      - Closet A, B
#### Atrium/ground level
  - Atrium Overhead*^, Lamp*^
  - Garage N, S
#### Den/lower level
  - Den N^, W^, S^, E^, Lamp^
    - Hallway
      - W*, E*
      - Closet
  - Porch\`
  - Guest Room^
  - Spare Room^
  - Laundry Room^
  - Downstairs Bathroom
    - S, W, E
    - Shower
#### Basement/bottom level
  - Basement NW, NE, SW, SE
#### Sidewalk/outside
  - Sidewalk W\`, E\`
  - Front Door W\`, E\`
