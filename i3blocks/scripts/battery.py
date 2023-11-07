#!/bin/python3

import subprocess

# You can also use  Upower for this purpose. But ACPI is the simplest one

acpi_output= subprocess.getoutput("acpi").strip()
battery_info=acpi_output.split(",")

battery_percentage=battery_info[1].strip()
battery_state= battery_info[0].split(":")[1].strip()

icon={
    "Charging": "",
    "Full": ""
}

print(f'{icon[battery_state]} {battery_percentage}')