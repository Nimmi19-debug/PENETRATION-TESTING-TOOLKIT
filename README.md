# PENETRATION-TESTING-TOOLKIT

"COMPANY": CODTECH IT SOLUTIONS

"NAME": KAGITHA YAMINI

"INTERN ID": CTO6DL1372

"DOMAIN": CYBER SECURITY & ETHICAL HACKING

"DURATION": 6 WEEKS

"MENTOR": NEELA SANTHOSH

"DESCRIPTION": TASK 3:Penetration Testing Toolkit

This project is a modular Penetration Testing Toolkit developed using HTML, CSS, JavaScript, and Python (Flask) in Visual Studio Code. The toolkit is designed to simulate common penetration testing techniques such as Port Scanning and Brute Force Attacks through an interactive web interface.

The frontend (index.html) allows users to input a target host or username, which is then sent to the Python backend (app.py) using JavaScript’s fetch() API. The backend handles logic for both tools using custom Python modules located in the scanner/ directory.

The Port Scanner module (port_scanner.py) scans ports in the range 20–1024 on a given host using Python’s socket library. It identifies open ports by attempting TCP connections.

The Brute Force Simulator module (brute_forcer.py) simulates a password guessing attack. It uses a fixed password list to test against a simulated login until it finds the correct one.

Results from both tools are returned in JSON format and displayed dynamically on the web interface.

Technologies Used:
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask, socket)
Editor: Visual Studio Code

"OUTPUT":

![Image](https://github.com/user-attachments/assets/878873ea-be0a-4c81-b2f9-beda0f2d7344)
