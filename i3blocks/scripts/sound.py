#!/bin/python3

import subprocess

# Here I am using PulseAudio CMD tool pactl.
# You can also use ALSA tool called amixer
# A guide can be found in this blog post: https://megamorf.gitlab.io/2018/12/16/set-audio-volume-from-command-line/


raw_sound_level= subprocess.getoutput("pactl --  get-sink-volume @DEFAULT_SINK@").strip()

# If sound is muted
sound_muted = subprocess.getoutput("pactl --  get-sink-mute @DEFAULT_SINK@")
if_sound_muted = sound_muted.split(":")[1].strip()

sound_level_list= raw_sound_level.split(",")
left_sound_level= sound_level_list[0].split("/")[1].strip()
right_sound_level= sound_level_list[1].split("/")[1].strip()



if if_sound_muted=="yes":
    print(" 0%")

elif left_sound_level== right_sound_level:
    floatsound = float(left_sound_level.strip("%"))
    if floatsound >= 80:
        print(f' {round(floatsound)}%')
    elif floatsound >=30 and floatsound<80:
        print(f' {round(floatsound)}%')
    elif floatsound <30:
        print(f' {round(floatsound)}%')

else:
    print("Sound Balance Error")
