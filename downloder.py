import yt_dlp
import sys

def progress_bar(d):
    if d['status'] == 'downloading':
        progress = d['downloaded_bytes'] / d['total_bytes'] * 100
        bar = ('#' * int(progress // 2)).ljust(50)
        sys.stdout.write(f"\r[{bar}] {progress:.2f}% {d['filename']}")
        sys.stdout.flush()

def download_video(url, resolution='best'):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # ভিডিও নামের সেটআপ
        'format': resolution,  # কাস্টম রেজোলিউশন
        'progress_hooks': [progress_bar],  # প্রগ্রেস বার ফাংশন
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    print("Supported platforms:")
    print("1. YouTube")
    print("2. TikTok")
    print("3. Facebook")
    print("4. Instagram")
    print("5. Twitter")
    print("6. Vimeo")
    print("7. Dailymotion")
    print("8. SoundCloud")
    print("9. Reddit")
    print("10. PornHub")
    print("11. XHamster")
    print("12. Xvideos")
    print("13. Twitch")
    print("14. Mastodon")
    print("15. VK")
    print("16. Bilibili")
    print("17. 9GAG")
    print("18. Flickr")
    print("19. Picasa")
    print("20. LiveLeak")
    print("21. LBRY")
    print("22. Peertube")
    
    video_url = input("Enter video URL from the above platforms: ")
    resolution = input("Enter desired resolution (e.g., 1080p, 720p, 480p, best): ")
    download_video(video_url, resolution)
    print("\nDownload complete!")
