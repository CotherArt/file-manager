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
cd file-manager/dist
FileManager.exe
``` -->
# Build project
Make an .exe file for Windows
## Python requeriments
- Pyinstaller

You need to have **pyinstaller** installed
`pip install pyinstaller`

To build the project, just run the following command:
```
pyinstaller --onefile .\FileManager.py .\fileformats.py
```
Or just run the `.\build.bat` file for Windows