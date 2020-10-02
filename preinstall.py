import os

commands = [
    "pip install pylint django",
    "dir mte_system",
    "python3 manage.py makemigrations", 
    "python3 manage.py migrate",
    "python3 manage.py createsuperuser"
]

for command in commands: 
    if command.split(" ")[0] == "dir": 
        os.chdir(command.split(" ")[1])
        continue

    os.system(command)