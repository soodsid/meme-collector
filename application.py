from flask import Flask,render_template,request,url_for
from bs4 import BeautifulSoup
import requests
import os

application=Flask(__name__)


@application.route('/', methods=['POST','GET'])
def query():
    if request.method=="GET":
        return render_template("/queryform.htm")
    else:
        folder='collection/'
        
        if not os.path.exists(folder):
            os.mkdir(folder)  
            
            
        query=request.form["query"]

        url="https://www.google.com/search?q="+query+"%20meme&tbm=isch"

        response=requests.get(url)
        
        soup=BeautifulSoup(response.content, 'html.parser')
        
        img_tags=soup.find_all('img')
        
        del (img_tags[0])
        
        for i in img_tags:
            imgsrc= i['src']
            imgdata=requests.get(imgsrc).content
            with open(os.path.join(folder, f"{query}_{img_tags.index(i)}.jpg"), "wb") as f:
                f.write(imgdata)
                
        return render_template("/queryform.htm", res="done")
            

        #checking if the conflict is working

        # conflict maaker

if __name__=="__main__":
    application.run(host='0.0.0.0', port=8000)
