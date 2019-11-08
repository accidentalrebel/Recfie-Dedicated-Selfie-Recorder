# Recfie - Dedicated Selfie Recorder
The code for Recfie, a custom-made foot pedal activated device that enables quick and easy recording of myself talking.

More details about the hardware project [on Hackaday.io](https://hackaday.io/project/168246-recfie-dedicated-selfie-recorder).

## What it does
The script does the following:
  * Mounts the USB and accesses the files recorded from Recfie
  * Files are copied then automatically converted and compressed to a destination folder
  * The generated files are connected together into one whole video file
  * The file is played automatically to inspect for corrupted segments
  * After inspecting the full video, the script asks if the original files can be deleted
  
## Technical details
  * Uses `HandbrakeCLI` for conversion and compression
  * Uses `ffmpeg` for concatenating video files
