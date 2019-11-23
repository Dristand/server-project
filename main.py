from flask import Flask, render_template, request, render_template_string
from base64 import b64encode, b64decode

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        encoded = ''
        decoded = ''
        if "encode" in request.form:
            toEncode = request.form['encode']
            try:
                encoded = b64encode(toEncode.encode()).decode()
            except:
                encoded = 'error'
        if "decode" in request.form:
            toDecode = request.form['decode']
            try:
                decoded = b64decode(toDecode.encode()).decode()
            except:
                decoded = 'error'

        s = render_template('a.html', context={
            "encoded" : encoded,
            "decoded" : decoded,
            })
        return render_template_string(s)
        
    return render_template('a.html', context='')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)