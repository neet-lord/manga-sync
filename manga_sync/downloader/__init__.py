import subprocess

def download(
    url,
    start_chapter,
    end_chapter,
    proxy,
    log
):
    command = [
        'manga-py',
        '-s',
        url,
        '-c',
        start_chapter,
    ]
    
    process = subprocess.Popen(
        command,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE
    )

    process.wait()