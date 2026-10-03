import sys
import os
import platform
from importlib.metadata import version, distributions, PackageNotFoundError

print("\033[97m" r"""
                                                                          
                                .::::::::::.                                   
                              .::``::::::::::.                                 
                              :::..:::::::::::                                 
                              ````````::::::::                                 
                      .::::::::::::::::::::::: iiiiiii,                        
                  .:::::::::::::::::::::::::: iiiiiiiii.                       
                  .::::::::::::::::::::::::::: iiiiiiiiii.                      
                  .::::::::::::::::::::::::::: iiiiiiiiii.                      
                  .:::::::::: ,,,,,,,,,,,,,,,,,iiiiiiiiii.                      
                  .:::::::::: iiiiiiiiiiiiiiiiiiiiiiiiiii.                      
                   `::::::::: iiiiiiiiiiiiiiiiiiiiiiiiii`                      
                      `:::::: iiiiiiiiiiiiiiiiiiiiiii`                         
                              iiiiiiii,,,,,,,,                                 
                              iiiiiiiiiii''iii                                 
                              `iiiiiiiiii..ii`                                 
                                `iiiiiiiiii`                                   
                                                                               
                      ____        _   _                                        
                     |  _ \ _   _| |_| |__   ___  _ __                         
                     | |_) | | | | __| '_ \ / _ \| '_ \                        
                     |  __/| |_| | |_| | | | (_) | | | |                       
                     |_|    \__, |\__|_| |_|\___/|_| |_|                       
                            |___/                                              
                                                                                 
                                                                          
                                                                """ "\033[0m")


# Python
python = platform.python_version()
print(f"Python Version:        {python}")

python_implementation = platform.python_implementation()
print(f"Python Implementation: {python_implementation}")

python_compiler = platform.python_compiler()
print(f"Python Compiler:       {python_compiler}")

python_executable = sys.executable
print(f"Python Executable:     {python_executable}")


# Pip
try:
    pip = version("pip")
except PackageNotFoundError:
    pip = "Not installed"

print(f"Pip Version:           {pip}")


# Python Packages
packages = list(distributions())
print(f"Python Packages:       {len(packages)}")


# Python Path
python_path = os.getcwd()
print(f"Python Path:           {python_path}")


# Websites
website = ("python.org", "pypi.org")
print(f"Websites:              {website[0]}, {website[1]}")

print("")
print("")

# Return to PowerShell / Terminal
sys.stdout.flush()
