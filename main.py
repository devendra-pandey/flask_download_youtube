from flask import Flask , render_template , request
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

        
            




    






if __name__ == '__main__':
   app.run(debug = True)