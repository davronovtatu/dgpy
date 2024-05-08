from app import DgFrameApp
from waitress import serve



app=DgFrameApp()

serve(app,host='0.0.0.0',port=8000)

