from cx_Freeze import setup, Executable

executables = [Executable('generator.py',
targetName='Генератор техкарт.exe',
base='Win32GUI',
icon='log.ico')]


includes = ['docxtpl', 'time', 'openpyxl', 'sys', 'PyQt5', 'os', 'logic', 'json']

zip_include_packages = ['docxtpl', 'time', 'openpyxl', 'sys', 'PyQt5', 'os', 'logic', 'json']

include_files = []

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
'include_files': include_files,
}
}

setup(name='generator.py',
version='0.0.1',
description='Генератор технологических карт',
executables=executables,
options=options)