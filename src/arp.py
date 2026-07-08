import platform
import subprocess


def show_arp_table():

    command = ["arp", "-a"]

    subprocess.run(command)