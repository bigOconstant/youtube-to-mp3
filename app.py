from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__)

def download_youtube_audio_as_mp3(url, output_path='.'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192', # You can adjust the quality
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Downloaded audio from '{url}' to '{output_path}'")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle the POST request data
        user_input = request.form.get('user_input') # 'user_input' is the name attribute from your HTML form input
        print("Downloading ",user_input)
        download_youtube_audio_as_mp3(user_input, output_path="./downloads")
        return f"You downloaded: {user_input}"
    
    # For GET requests, render the HTML page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8111)
    #app.run(debug=True)