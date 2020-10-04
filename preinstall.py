import os
import string
import random
import platform

system = (platform.system() == "Linux")
python = "python3" if system else "python"

char_set = "".join([string.ascii_letters, string.digits, string.punctuation])

with open(f'{os.getcwd()}/mte_system/mte_system/secret_key.key', 'w') as file1:
    file1.write("".join(random.choice(char_set) for _ in range(50)))

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

    try:
        
        if command.split(" ")[0] == "dir":
            os.chdir(command.split(" ")[1])

            continue
        
        os.system(command)

    except KeyboardInterrupt:
        continue
