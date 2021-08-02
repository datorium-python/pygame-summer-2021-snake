from cx_Freeze import setup, Executable
import sys

# klases nosaukums ar lielo burtu
# visam parejam maizais burts

build_exe_options = {
    'packages': ['pygame'],
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Snake',
    version='1.0',
    description='Snake',
    options={'build_exe': build_exe_options},
    executables=[Executable('main.py', base=base)]
)
