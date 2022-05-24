import subprocess, os
listeners = ['^(http(s)?://)?(www\.)?video.golem.de/.*$']
path = './download/video.golem.de'

def handle(url):
    status = subprocess.call(['yt-dlp', '--output', f'{path}/%(title)s-%(id)s.%(ext)s', url])
    title = subprocess.run(['yt-dlp', '--get-title', url],capture_output=True).stdout.decode('utf-8').rstrip()
    return title, status