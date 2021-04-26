# StayAwake  
Stay Awake is a simple app that keeps your computer from going to sleep.
  
![](app.gif)  
![](trayMessage.png)  
![](trayMenu.png)  
  
## Features

1. Lightweight  
1. Simple one-button GUI  
1. Minimize to tray  
1. Runs in background  
  
## Specs

1. Python >= 3.8  
1. Dependencies: PyQt5, PyAutoGUI  
1. Compatibility: Windows, MacOS, Linux (only tested on Windows)  

## Installation

1. Clone repository  
1. Install dependencies using pip and requirements.txt file  
  
  ```bash
  pip install -r requirements.txt
  ```

1. Run and enjoy being AFK!!  
  
## How to make an executable

  1) ```pip install pyinstaller```  
  2) ```pyinstaller --onefile app.py --icon=StayAwake.ico --windowed --noconsole --name="Stay Awake"```  
  
## Download and run instantly without any code

https://github.com/alvsanand/StayAwake/releases  

## Development

Un order to run in development mode:

- Windows:

  ```cmd
  python -m venv venv

  .\env\Scripts\activate

  pip install -r requirements.txt
  ```

- MacOS / Linux:

  ```bash
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt

  python app.py
  ```
