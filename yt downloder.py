import yt_dlp
import sys

def progress_bar(d):
    if d['status'] == 'downloading':
        progress = d['downloaded_bytes'] / d['total_bytes'] * 100
        bar = ('#' * int(progress // 2)).ljust(50)
        sys.stdout.write(f"\r[{bar}] {progress:.2f}% {d['filename']}")
        sys.stdout.flush()

def download_video(url, resolution='best'):
    # ✅ Shorts লিংক ফিক্স
    if 'youtube.com/shorts/' in url:
        video_id = url.split('/')[-1].split('?')[0]
        url = f'https://www.youtube.com/watch?v={video_id}'

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': resolution,
        'progress_hooks': [progress_bar],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    print("Supported platforms:")
    print("1. YouTube")
    print("2. TikTok")
    print("3. Facebook")
    print("...")

    video_url = input("Enter video URL from the above platforms: ")
    resolution = input("Enter desired resolution (e.g., 1080p, 720p, 480p, best): ")
    download_video(video_url, resolution)
    print("\nDownload complete!")
