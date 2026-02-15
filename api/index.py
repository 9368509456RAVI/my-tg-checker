from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>API is Online!</h1><p>Use /check?u=username</p>"

@app.route('/check')
def check_username():
    user = request.args.get('u')
    if not user:
        return jsonify({"error": "No username provided"}), 400
    
    url = f"https://t.me/{user}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        # Sahi logic: Agar page title mein username nahi hai aur contact text hai
        if 'If you have Telegram' in response.text and user not in response.text:
            return jsonify({"username": user, "Can Claim": True, "status": "Available"})
        else:
            return jsonify({"username": user, "Can Claim": False, "status": "Taken"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Sabse Important: Vercel ke liye app ko export karna
app = app
