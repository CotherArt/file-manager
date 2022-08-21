# File-manager

author: CotherArt

Program to sort files in diferent folders

## Requeriments
- Python

# Download and execute

```
git clone https://github.com/CotherArt/file-manager.git
cd file-manager
python FileManager.py
```
<!-- # Windows no python
You can use the executable for Windows without needing to install python
```
git clone https://github.com/CotherArt/file-manager.git
cd file-manager/dist/FileManager/
FileManager.exe
``` -->

# Build project
Make an .exe file for Windows
## Python requeriments
- Pyinstaller

You need to have **pyinstaller** installed
`pip install pyinstaller`

To build the project, just run the following command:
## Windows
```
pyinstaller --add-data "config.txt;." .\FileManager.py
```
## Linux
```
pyinstaller --add-data "config.txt:." .\FileManager.py
```
Or just run the `./build.bat` file for Windows or `./build.sh` for Linux
Now you can run `./dist/FileManager/FileManager.exe`