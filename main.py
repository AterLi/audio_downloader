# Temporarily, this package has an issue

# From pytube import YouTube.
# Using pytubefix instead.
from pytubefix import YouTube
import os

# Add in this list links to desired music/video
play_list = ["Link1", "Link2", "And_so_on"]

# Count downloaded mp3 files
downloaded_count = 0


def download_from_yt(url, total):
    global downloaded_count
    try:
        # url input from user
        yt = YouTube(url)

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # destination to save file
        destination = './downloaded_files'

        # downloaded_files the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    # except UnboundLocalError:
    # 	print("❌ downloaded_files failed", yt.title)
    except FileExistsError:
        downloaded_count += 1
        print("❌ File already exists, pytube may try to downloaded_files in mp4 format if mp3 exists:", yt.title)
    except:
        print("❌ Something went wrong, maybe invalid link")
    else:
        downloaded_count += 1
        print("✅", yt.title, " has been successfully downloaded.")
    finally:
        print(f"Downloaded mp3 files: {downloaded_count}/{total}")


for song in play_list:
    download_from_yt(song, len(play_list))



