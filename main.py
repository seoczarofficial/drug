from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# Replace with your actual WordPress credentials
WP_SITE = "https://reverent-keller.66-175-239-111.plesk.page"
WP_USER = "your-username"
WP_APP_PASSWORD = "your-app-password"

@app.route("/send-to-wordpress", methods=["POST"])
def send_to_wordpress():
    data = request.json
    drug_name = data.get("drug_name", "Untitled")
    content = data.get("content", "No content provided.")

    post_data = {
        "title": drug_name,
        "content": content,
        "status": "publish"
    }

    response = requests.post(
        f"{WP_SITE}/wp-json/wp/v2/posts",
        json=post_data,
        auth=HTTPBasicAuth(WP_USER, WP_APP_PASSWORD)
    )

    return jsonify({
        "status": response.status_code,
        "response": response.json()
    })