#!/usr/bin/env python3
import os, shutil, subprocess, sys
from datetime import datetime

USB_PATH = "/run/media/arebel/2004-1014/DCIM/DCIMA/"
TEMP_USB_PATH = "/home/arebel/videos/recfie/temp/"
UNPROCESSED_PATH = "/home/arebel/videos/recfie/unprocessed/"
FINAL_PATH = "/home/arebel/videos/recfie/final/"
QUEUE_FILE_PATH = "/home/arebel/videos/recfie/conversion-queue.txt"

source_path = TEMP_USB_PATH

def get_sorted_files(path):
    files = os.listdir(path)
    files.sort()
    return files

files_to_process = get_sorted_files(source_path)

print("Converting files...")
for f in files_to_process:
    file_name = f.split(".")[0]
    cmd = "HandBrakeCLI -i " + source_path + f + " -o " + UNPROCESSED_PATH + file_name + ".mp4"
    print("Sending command: " + cmd)
    subprocess.call(cmd, shell=True)

print("\nConcatenating files...")
concat_string = ""
for f in get_sorted_files(UNPROCESSED_PATH):
    concat_string += "file '" + UNPROCESSED_PATH + f + "'\n"

concat_string = concat_string[0:len(concat_string) - 1]
print("Adding to queue...\n" + concat_string)
    
with open(QUEUE_FILE_PATH, "w+") as f:
   f.write(concat_string)

print("Queue added.")

print("\nConcatenating files...")
cmd = "ffmpeg -f concat -safe 0 -i " + QUEUE_FILE_PATH  + " -c copy " + FINAL_PATH + datetime.today().strftime("%Y-%m-%d_%H-%M-%S") + ".mp4"
print(cmd)
subprocess.call(cmd, shell=True)
print("Files concatenated.")

print('Removing files in ' + UNPROCESSED_PATH)
for f in os.listdir(UNPROCESSED_PATH):
    os.remove(UNPROCESSED_PATH + f)

print('Removing files in ' + source_path)
for f in os.listdir(source_path):
    os.remove(source_path + f)
