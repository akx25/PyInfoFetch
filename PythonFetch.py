import sys
import os
import platform
from importlib.metadata import version, distributions, PackageNotFoundError


logo = r"""
            .::::::::::.
            ::``::::::::::.
            :::..:::::::::::
            ````````::::::::
.::::::::::::::::::::::: iiiiiii,
.:::::::::::::::::::::::::: iiiiiiiii.
 ::::::::::::::::::::::::::: iiiiiiiiii
 ::::::::::::::::::::::::::: iiiiiiiiii
 :::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii
 :::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii
 `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii
    `:::::: iiiiiiiiiiiiiiiiiiiiiii
            iiiiiiii,,,,,,,,
            iiiiiiiiiii''iii
            `iiiiiiiiii..ii
              `iiiiiiiiii`

____        _   _
|  _ \ _   _| |_| |__   ___  _ __
| |_) | | | | __| '_ \ / _ \| '_ \
|  __/| |_| | |_| | | | (_) | | | |
|_|    \__, |\__|_| |_|\___/|_| |_|
       |___/
""".strip("\n")



python = platform.python_version()

python_implementation = platform.python_implementation()

python_compiler = platform.python_compiler()

python_executable = sys.executable



try:
    pip = version("pip")
except PackageNotFoundError:
    pip = "Not installed"



packages = list(distributions())



python_path = os.getcwd()



website = ("python.org", "pypi.org")



info = [
    f"Python Version:        {python}",
    f"Python Implementation: {python_implementation}",
    f"Python Compiler:       {python_compiler}",
    f"Python Executable:     {python_executable}",
    f"Pip Version:           {pip}",
    f"Python Packages:       {len(packages)}",
    f"Python Path:           {python_path}",
    f"Websites:              {website[0]}, {website[1]}",
]



logo_lines = logo.splitlines()

width = max(len(line) for line in logo_lines)

info_offset = 3

for i in range(max(len(logo_lines), len(info) + info_offset)):

    left = logo_lines[i] if i < len(logo_lines) else ""

    info_index = i - info_offset

    if 0 <= info_index < len(info):
        right = info[info_index]
    else:
        right = ""

    print(
        f"\033[97m{left:<{width}}\033[0m    {right}"
    )



sys.stdout.flush()
