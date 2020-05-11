import random
from time import sleep
from os import system, name
import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("jogoforca.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = [],
        excludes = []
)


setup(
    name = "Jogo da Forca",
    version = "1.0",
    description = "Jogo da Forca",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
