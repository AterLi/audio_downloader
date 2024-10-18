# YouTube Audio Downloader

## Disclaimer

**IMPORTANT:** Using this script to download copyrighted content without permission is illegal. Always ensure you have the right to download and use the content. The authors of this script are not responsible for any misuse or legal issues arising from improper use.

## Description

This Python script allows you to download audio from YouTube videos and save them as MP3 files. It uses the `pytubefix` library to interact with YouTube and download audio streams.

## Features

- Download audio from YouTube videos
- Convert downloaded audio to MP3 format
- Handle multiple URLs in a playlist
- Basic error handling for file exists and invalid links

## Requirements

- Python 3.x
- pytubefix library

## Installation

1. Clone this repository or download the script.
2. Install the required library

## Usage

1. Open the `main.py` file.
2. Add your desired YouTube video URLs to the `play_list` array.
3. Run it.
4. The script will download the audio from each video in the playlist and save it as an MP3 file in the `./downloaded_files` directory.

## Acknowledgements

This script uses the pytubefix library, a fork of the original pytube library, due to an error in pytube as of 10.18.2024.
