from flask import Flask, request, jsonify
from chatter.core import train, reply
app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    return reply(request.data.decode('utf-8'))

@app.route('/train', methods=['POST'])
def doTrain():
    train()
    return "Training complete"
'''
<form action="/~bbarif/alpha-art" method="get">
  <label for="str">Name:</label>
  <input id="str" type="text" name="str">
  <button type="submit">Submit</button>
</form>
'''

if __name__ == '__main__':
    try:
        
        app.run(server='gunicorn', host='localhost', port=5000)
    except:
        app.run(host='localhost', port=5000)
