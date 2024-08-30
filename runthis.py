import os
import subprocess
import sys

def create_virtualenv():
    # Determine the command to create a virtual environment based on the OS
    if os.name == 'nt':  # Windows
        venv_command = ['py', '-m', 'venv', 'venv']
    else:  # Linux/Mac
        venv_command = ['python3', '-m', 'venv', 'venv']

    subprocess.run(venv_command, check=True)
    print("Virtual environment created successfully.")

def activate_virtualenv():
    # Determine the command to activate the virtual environment based on the OS
    if os.name == 'nt':  # Windows
        activate_command = os.path.join('venv', 'Scripts', 'activate.bat')
    else:  # Linux/Mac
        activate_command = os.path.join('venv', 'bin', 'activate')

    # Use exec to replace the current process with the activated environment
    exec(open(activate_command).read(), dict(__file__=activate_command))
    print("Virtual environment activated.")

def install_requirements():
    # Install the required packages
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
    print("Requirements installed successfully.")

if __name__ == "__main__":
    create_virtualenv()
    activate_virtualenv()
    install_requirements()
