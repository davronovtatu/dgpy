from app import DgFrameApp
from waitress import serve



app=DgFrameApp()





@app.route("/about")
def about(request,response):
    response.text="About page"

@app.route("/home")
def home(request,response):
    response.text="Home page"












serve(app,host='0.0.0.0',port=8000)