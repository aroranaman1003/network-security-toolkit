import platform
import subprocess


def ping_host(host):

    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", host]
    else:
        command = ["ping", "-c", "4", host]

    subprocess.run(command)