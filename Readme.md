# Youtube to MP3 converter

Simple web app to download music from youtube videos

# dependencies

Needs ffmpeg. 

on Ubuntu,

```
sudo apt install ffmpeg
```

# Set up environment

```
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

URL=http://localhost:5000 python app.py

```

Default port is 5000. 

Go to http://localhost:5000

You can download in either mp3 or m4a format.

List all your downloaded mp3s in http://localhost:5000/list



