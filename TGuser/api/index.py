from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/check')
def check_username():
    user = request.args.get('u')
    if not user:
        return jsonify({"error": "No username provided"}), 400
    
    url = f"https://t.me/{user}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if 'tgme_page_extra' not in response.text and 'If you have Telegram' in response.text:
        return jsonify({"username": user, "Can Claim": True, "status": "Available"})
    else:
        return jsonify({"username": user, "Can Claim": False, "status": "Taken"})

# Yeh line Vercel ko batati hai ki Flask app yahan hai
app.run()