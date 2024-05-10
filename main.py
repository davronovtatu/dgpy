from app import DgFrameApp
from waitress import serve



app=DgFrameApp()





@app.route("/about")
def about(request,response):
    response.text="About page"

@app.route("/home")
def home(request,response):
    response.text="Home page"


@app.route("/hello/{name}")
def greeting(request,response,name):
    response.text=f"Hello {name}"











serve(app,host='0.0.0.0',port=8000)