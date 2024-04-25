from pytube import YouTube

# Function to download video from a list of URLs
def download_videos(video_urls):
    for url in video_urls:
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio=True).first()
            print(f"Downloading {yt.title}...")
            stream.download(output_path='audio2')
        except Exception as e:
            print(f"Error downloading {url}: {e}")

# List of video URLs
video_urls = [
"https://www.youtube.com/watch?v=wQ4KMNdPNVI",
"https://www.youtube.com/watch?v=hIZA377wuUI",
"https://www.youtube.com/watch?v=QmDH3-Ig8rs",
"https://www.youtube.com/watch?v=mEarUUtYzgs",
"https://www.youtube.com/watch?v=IbFB-PWpL18",
"https://www.youtube.com/watch?v=jEUdaUChPzY",
"https://www.youtube.com/watch?v=uUQtlMQm8nk",
"https://www.youtube.com/watch?v=_9JnVZEYNR8",
"https://www.youtube.com/watch?v=lBRK4qO1xJI",
"https://www.youtube.com/watch?v=xDuEu4aVlwo",
"https://www.youtube.com/watch?v=8nEchNFw9TQ",
"https://www.youtube.com/watch?v=lTg-fAJpMSE",
"https://www.youtube.com/watch?v=hJsQNBo48Uo",
"https://www.youtube.com/watch?v=bkUBCX6nkzk",
"https://www.youtube.com/watch?v=cli0nyejP-8",
"https://www.youtube.com/watch?v=qtxr4DFQhh0",
"https://www.youtube.com/watch?v=vmrFu0AuSVA",
"https://www.youtube.com/watch?v=NTOdy3f12A0",
"https://www.youtube.com/watch?v=tJ6dDHNEBf8"
]

# Download videos
download_videos(video_urls)
