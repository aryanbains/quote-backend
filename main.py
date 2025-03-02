from flask import Flask, Response, request
from flask_cors import CORS
import random
import json

app = Flask(__name__)

# Configure CORS to allow all origins. 
# For production, you might want to restrict this to specific domains.
CORS(app, resources={r"/*": {"origins": "*"}})

# Load quotes from the JSON Lines file
with open("quotes.jsonl", "r", encoding="utf-8") as f:
    quotes = [json.loads(line) for line in f]

@app.route('/', methods=['GET'])
def get_random_quote():
    random_quote = random.choice(quotes)
    # Return JSON, ensuring non-ASCII characters are preserved
    return Response(json.dumps(random_quote, ensure_ascii=False), mimetype='application/json')

if __name__ == '__main__':
    # Host and port can be changed as needed. 
    # '0.0.0.0' allows external connections in many hosting environments.
    app.run(debug=True, host='0.0.0.0', port=5000)