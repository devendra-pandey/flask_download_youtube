from flask import Flask , render_template , request,jsonify
import youtube_dl


app = Flask(__name__)


ydl_opts = {}

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.get('Name')
      
      print(result)
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("***********" , ydl)
        
        channel = 1
        while (channel == int(1)):
            link_of_the_video = result
            zxt = link_of_the_video.strip()
            video_download = ydl.download([zxt])
            print("chevk" , video_download)
            return render_template('result.html')



from pytube import YouTube

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        link = request.json.get('link')

        try:
            youtube_object = YouTube(link)
            youtube_object = youtube_object.streams.get_highest_resolution()
            youtube_object.download()
            return jsonify({'message': 'Download completed successfully'})
        except:
            return jsonify({'message': 'An error occurred during download'})


if __name__ == '__main__':
   app.run(debug = True)