import subprocess
import sys
import os

def install_dependencies():
    # List of required packages
    required_packages = ['imgviz', 'natsort', 'PyQt5', 'numpy', 'scipy', 'matplotlib']

    for package in required_packages:
        subprocess.run([sys.executable, "-m", "pip", "install", package])

def main():
    # Activate virtual environment
    venv_path ="/home/alan/Documents/python/bugbont/labelme/venv/" 
    activate_path = os.path.join(venv_path, 'bin', 'activate')
    
    activate_command = f'source {activate_path}' if os.name != 'nt' else f'activate {activate_path}'
    subprocess.run(activate_command, shell=True)

    # Install required dependencies
    install_dependencies()

    # Run labelme
    subprocess.run([sys.executable, "-m", "labelme"])

if __name__ == "__main__":
    main()
