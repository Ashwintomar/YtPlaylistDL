import os
import streamlit as st
import yt_dlp
from moviepy.editor import AudioFileClip
from tqdm import tqdm
from streamlit_option_menu import option_menu

def download_top_n_songs(playlist_link, n, output_dir):
    try:
        # Parse the playlist link
        ydl_opts = {
            'extract_flat': True,
            'dump_single_json': True,
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            playlist_info = ydl.extract_info(playlist_link, download=False)
            video_urls = [entry['url'] for entry in playlist_info['entries'][:n]]

        # Create a directory to save the MP3 files
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Initialize progress bar
        progress_bar = st.progress(0)
        progress_text = st.empty()

        # Download and convert each video to MP3
        for i, url in enumerate(video_urls):
            try:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Update progress bar
                progress = (i + 1) / n
                progress_bar.progress(progress)
                progress_text.text(f"Downloaded and converted {url} to MP3")
            except Exception as e:
                st.error(f"Error processing {url}: {e}")

        # Close progress bar
        progress_bar.progress(1.0)
        st.success(f"Successfully downloaded top {n} songs from the playlist.")

    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("YouTube Music Playlist Downloader")

    # Sidebar for user inputs
    st.sidebar.header("Settings")
    playlist_link = st.sidebar.text_input("Enter YouTube Music Playlist Link")
    n = st.sidebar.number_input("Number of Songs to Download", min_value=1, value=5)
    output_dir = st.sidebar.text_input("Download Folder", value="downloaded_songs")

    # Visualize playlist
    if playlist_link:
        try:
            ydl_opts = {
                'extract_flat': True,
                'dump_single_json': True,
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                playlist_info = ydl.extract_info(playlist_link, download=False)
                st.header("Playlist Songs")
                for i, entry in enumerate(playlist_info['entries'][:n]):
                    try:
                        st.write(f"{i+1}. {entry['title']}")
                    except Exception as e:
                        st.error(f"Error parsing title of {entry['url']}: {e}")
        except Exception as e:
            st.error(f"Error parsing playlist: {e}")

    # Download button
    if st.sidebar.button("Download Songs"):
        download_top_n_songs(playlist_link, n, output_dir)

if __name__ == "__main__":
    main()