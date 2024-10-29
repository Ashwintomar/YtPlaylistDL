# YouTube Playlist Downloader

This project is a web application that allows users to download and convert songs from a YouTube playlist into MP3 format. Using `yt-dlp` and `moviepy`, this app simplifies playlist downloading and conversion, enabling quick access to audio files offline.

## Features

- Download audio from YouTube playlists in MP3 format.
- Select the number of songs to download from the playlist.
- Progress tracking for each download and conversion.
- User-friendly interface built with Streamlit.

## Installation

### Prerequisites

Make sure you have Python 3.6 or later installed.

### Step-by-Step Installation

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Ashwintomar/yt_dl.git
   cd yt_dl
   ```

2. **Install Dependencies**  
   Install all required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

   > **Note:** This application uses `ffmpeg` for audio extraction. If you don't have `ffmpeg` installed, please [download and install it here](https://ffmpeg.org/download.html).

3. **Run the Application**  
   Launch the Streamlit app:
   ```bash
   streamlit run main.py
   ```

## Usage

1. **Enter the YouTube Playlist Link**  
   Provide a link to a YouTube playlist that you want to download.

2. **Select the Number of Songs**  
   Choose how many songs you wish to download from the playlist.

3. **Choose Output Directory**  
   Specify the directory where the downloaded files will be saved.

4. **Start Downloading**  
   Click the "Download Songs" button to begin downloading and converting the selected number of songs from the playlist.

5. **Progress Tracking**  
   The application will show the download progress for each song in the playlist.

## Requirements

The `requirements.txt` file includes all the dependencies needed to run this project:
- `streamlit`
- `yt-dlp`
- `moviepy`
- `tqdm`
- `streamlit-option-menu`

## Disclaimer

This tool requires `ffmpeg` for audio extraction. Please ensure it is installed on your system. You can download `ffmpeg` from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Acknowledgments

- This project uses the open-source libraries `yt-dlp` and `moviepy` for video download and conversion.
- The UI is built with Streamlit, providing a clean and interactive interface.

---

Enjoy downloading your favorite playlists!
