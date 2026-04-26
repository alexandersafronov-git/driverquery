Done as part of a test task.

A Python script that will run the "driverquery" utility
and save the results to a file, and then open this file
and output only drivers with the "File System " driver type.

Output format similar to original "driverquery" utility.

Requirements: Windows 10, english locale 

Installation
1) Install Python 3.14 (or above) x64 
2) Install  MS Visual Studio Build tools for C++
3) Install Git:  winget install --id Git.Git -e --source winget
4) Clone repository:
git clone https://github.com/alexandersafronov-git/driverquery && cd driverquery
5) Install dependencies: pip install -r requirements.txt
   
Verify installation: 
  pytest  -s -v

Usage examples:
 
driverquery.py

 driverquery.py --driver_type="Files System " --fo CSV