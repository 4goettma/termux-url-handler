import subprocess
listeners = ['^(http(s)?://)?((www\.)?(m\.)?youtube.(de|com)|youtu.be)/.*$']
path = './download/YouTube'

def handle(url):
    status = subprocess.call(['yt-dlp', '--all-subs', '--output', f'{path}/%(title)s-[%(uploader)s]-%(id)s.%(ext)s', url])
    title = subprocess.run(['yt-dlp', '--get-title', url],capture_output=True).stdout.decode('utf-8').rstrip()
    return title, status