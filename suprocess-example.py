import subprocess

# List of commands to run
commands = [
    "ls -l",
    "pwd",
    "echo 'Hello, subprocess!'",
    "uname -a",
    "df -h",
    "ps aux",
    "whoami",
    "date",
    "echo 'Another subprocess example'",
    "ifconfig"
]

# Iterate through the list of commands and run each one
for command in commands:
    try:
        # Run the command using subprocess.run
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Print the command and its output
        print(f"Command: {command}")
        print(f"Output:\n{result.stdout}")
        print("=" * 40)

    except subprocess.CalledProcessError as e:
        # If the command returns a non-zero exit code, print the error
        print(f"Error running command '{command}': {e}")
        print("=" * 40)

~                                                                                       
~                                                                                       
~                                                                                       
~                                                                                       
"subprocess_example.py" 32L, 861B                                     1,1           All
[ttyd] 0:vim*                                    "student@bchd: ~/mycod" 20:50 13-Nov-23
