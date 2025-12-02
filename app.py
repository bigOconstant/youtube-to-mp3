from flask import Flask, render_template, request
import os
from urllib.parse import quote
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
        download_youtube_audio_as_mp3(user_input, output_path="./static/downloads")
        #return f"You downloaded: {user_input}"
        return render_template('index.html')
    
    # For GET requests, render the HTML page
    return render_template('index.html')

@app.route('/list')
def list_static_files():
    static_folder_path = os.path.join(app.root_path, app.static_folder) +"/downloads"
    
    # List all files and directories within the static folder
    all_items = os.listdir(static_folder_path)
    
    # Filter to only include files (and not subdirectories) if desired
    files_only = [item for item in all_items if os.path.isfile(os.path.join(static_folder_path, item))]

    url_safe = []
    for item in files_only:
        url_safe.append(quote(item)) # Example: double each item

    


    return render_template('list.html', items=files_only,safe=url_safe)
    
    #return f"Files in static folder: {files_only}"

if __name__ == '__main__':
    app.run(port=8111)
    #app.run(debug=True)