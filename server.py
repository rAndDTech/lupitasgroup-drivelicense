from flask import Flask, request, jsonify
from dictionario import AAMVA 
from pdf417decoderr import PDFDecoderLicense

app = Flask(__name__)

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our apilupitas-drivelicese!</h1>"




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    # app.run(threaded=True, port=5000)
    #app.run(host="0.0.0.0", port=5000)
   # app.run()
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    