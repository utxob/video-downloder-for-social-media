import yt_dlp
import re
import os

def clean_filename(filename):
    """ফাইল নাম থেকে অবৈধ ক্যারেক্টার রিমুভ করবে"""
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def download_video(url, resolution='best'):
    """ভিডিও ডাউনলোড করার জন্য ফাংশন"""
    output_template = "%(title)s.%(ext)s"  # টাইটেল অনুযায়ী ফাইল নাম

    ydl_opts = {
        'format': resolution,  # বেস্ট কোয়ালিটি / নির্দিষ্ট রেজোলিউশন
        'outtmpl': {'default': output_template},  # সঠিক ফরম্যাট ব্যবহার করা হয়েছে
        'noplaylist': True,  # শুধুমাত্র ভিডিও ডাউনলোড করবে, প্লেলিস্ট নয়
        'quiet': False,  # প্রিন্ট মেসেজ দেখাবে
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        filename = clean_filename(info['title']) + "." + info['ext']
        ydl_opts['outtmpl']['default'] = filename  # ক্লিন ফাইল নাম সেট
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("📌 ভিডিওর URL দিন: ")
    resolution = input("📌 রেজোলিউশন দিন (যেমন: best, 1080p, 720p): ") or "best"
    
    print("\n⏳ ডাউনলোড শুরু হচ্ছে...\n")
    download_video(video_url, resolution)
    print("\n✅ 🎉 ডাউনলোড সম্পন্ন!")
