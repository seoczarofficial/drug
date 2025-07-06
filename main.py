from flask import Flask, request, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# Replace with your actual WordPress credentials
WP_SITE = "https://reverent-keller.66-175-239-111.plesk.page"
WP_USER = "akshay_6glzerdh"
WP_APP_PASSWORD = "ZIJ7jPcNvJBj1eq0tFFFKS5x"

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

    if response.status_code == 201:
        return jsonify({
            "message": f"✅ '{drug_name}' was successfully posted to WordPress.",
            "wordpress_post_url": response.json().get("link")
        })
    else:
        return jsonify({
            "error": f"❌ Failed to post '{drug_name}'.",
            "status": response.status_code,
            "response": response.text
        }), response.status_code
