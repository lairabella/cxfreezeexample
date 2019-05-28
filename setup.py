from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.

# Packages = Packages we need to use. Example: numpy, usb

buid_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
base = None

setup(  name="APP NAME",
        version="0.1",
        description="Example",
        options={"buid_exe": buid_exe_options},
        executables=[Executable("example.py", base=base)] 
        )
