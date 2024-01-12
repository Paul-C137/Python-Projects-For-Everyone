#!/usr/bin/env python3

#This program uses a Batch file to download YouTube videos to a folder on your cpmputer
#Parent | Bla7857

import os
import subprocess
import time

def main():
    # Step 1: Read URLs from file
    urls_file_path = os.path.join(os.path.expanduser('~'), 'Documents01', 'youtube_videos', 'video_url.txt')
    with open(urls_file_path, 'r') as file:
        urls = file.readlines()

    # Step 2: Show progress bar for 0.5 seconds
    show_progress_bar()

    # Step 3: Download videos one by one
    output_folder = '~/Documents01/youtube_videos/'
    for url in urls:
        url = url.strip()  # Remove newline characters
        download_video(url, os.path.join(os.path.expanduser('~'), 'Documents01', 'youtube_videos'))

    # Step 4: Print video names
    print_video_names(output_folder)

    # Step 7: Print custom message in red color
    print_colored_message('You Have Run The Jewels ** Vandalize** GIMME THE LOOT', 'red')

    # Step 8: Exit the program
    exit_program()

def show_progress_bar():
    for _ in range(5):
        print('=', end='', flush=True)
        time.sleep(0.1)
    print()

def download_video(url, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Download video using YT-DLP
    subprocess.run(['yt-dlp', '-o', f'{output_folder}/%(title)s.%(ext)s', url])

def print_video_names(output_folder):
    print('Video Names:')
    for filename in os.listdir(output_folder):
        video_name = os.path.splitext(filename)[0]
        print(video_name)



def print_colored_message(message, color):
    print(f'\033[1;31;40m{message}\033[0m')  # Set text color to red

def exit_program():
    # You can add any necessary cleanup or farewell messages here
    exit()


if __name__ == '__main__':
    main() 