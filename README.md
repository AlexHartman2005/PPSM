# PPSM

Security engineers must document ports, protocols, and services that applications and servers require, using Ports-Protocol-Service Matrix (PPSM). Building and maintaining this matrix by hand is time-consuming and often leaves entries missing or incorrect. This project uses a Python application to use NMAP to scan which helps to automate PPSM creation. The application accepts network scan results from NMAp in XML format, or in our case manual user entry. It parses each host’s open ports into records and organizes them into an editable table with the following fields: ports, protocol, service, source IP, source name, destination IP, and destination name. Users can add, modify, or delete entries and then export the finished matrix as a CSV file. Automating this workflow is expected to reduce documentation time and improve the accuracy of PPSM. The application is limited to the hosts and networks reachable from the user’s device, depending on NMAP and its output format. It reflects network state only at the time of scan.



# Instructions

To be able to use the program you will need to install both nmap and python on your machine. instructions on how to download both are below



1. Downloading python (if pip and python are already downloaded you can skip)

   A. Windows
      1. Check if python is installed with 'python --version' in command prompt

      2. To install you can type 'wignet install Python.Python.3.13' in command prompt or go to the official page 'https://www.python.org/downloads/windows'

      3. Check if pip is installed with 'python -m pip --version' in command prompt
         3a. if pip is missing type in 'python -m ensurepip --upgrade' in command prompt
         3b. then type 'python -m pip install --upgrade pip' in command prompt

      4. Make sure that both pip and python are installed with 'python --version' and
         'python -m pip --version' into command prompt


   B. Mac
      1. Check if python is installed with 'python3 --version' in terminal

      2. If homebrew is installed type 'brew install python' in terminal
         2a. If not you can go to the official page 'https://www.python.org/downloads/macos'

      3. Check if pip is installed with 'python3 -m pip --version' in terminal
         3a. if pip is missing type in 'python3 -m ensurepip --upgrade' inside terminal
         3b. then type 'python3 -m pip install --upgrade pip' in terminal

      4. Make sure that both pip and python are installed with 'python3 --version' and 'python3 -m pip --version' inside terminal

   
   C. Linux
      1. Check if python is installed with 'python3 --version' in terminal

      2. To download both python and pip type in 'sudo apt update' and 'sudo apt install python3 python3-pip python3-venv -y' into terminal

      3. Make sure that both pip and python are installed with 'python3 --version' and 'python3 -m pip --version' inside terminal


2. Downloading Nmap
   A. Windows
      1. To install type 'winget install Insecure.Nmap' in command prompt or go to the official page 'https://nmap.org/download#windows'

      2. Check if it is installed properly by typing 'nmap --version' in command prompt


   B. Mac
      1. To install type 'brew install nmap' in terminal, if you dont have homebrew installed either install homebrew or go to the official page 'https://nmap.org/download#macosx'
      2. Check if it is installed properly by typing 'nmap --version' in terminal


   C. Linux
      1. To install type 'sudo apt update' then 'sudo apt install nmap' into terminal or go to the official page 'https://nmap.org/download#linux-rpm'
      2. Check if it is installed properly by typing 'nmap --version' in terminal


# How to Use

1. Users will enter the IP address when prompted
2. The program will show  all the services connected to that IP address and will ouput a csv table that the user will be able to look at
3. Users will also be able to add network services directly if it was not captured by the scan or for planned systems

