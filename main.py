from app import App
from waitress import serve



app=App()

serve(app,host='0.0.0.0',port=8000)

