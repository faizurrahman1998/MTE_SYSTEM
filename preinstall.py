import os
import platform

system = (platform.system() == "Linux")
python = "python3" if system else "python"

commands = [
    "pip install pylint django" if system else "python -m pip install pylint django",
    "dir mte_system",
    f"{python} manage.py makemigrations", 
    f"{python} manage.py migrate",
    f"{python} manage.py createsuperuser", 
    f"{python} manage.py runserver"
]

for command in commands: 

    print(f"executing command: {command}")
    
    if command.split(" ")[0] == "dir":
        os.chdir(command.split(" ")[1])

        continue
        
    os.system(command)

