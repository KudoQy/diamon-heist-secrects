from flask import Flask, render_template, request

app = Flask(__name__)

# --- Challenge 1: Heist: Vault Audit - Client-Side Secrets (Inspect Challenge) ---
@app.route('/')
def index():
    """
    Renders the main challenge page. This page contains hidden elements and JavaScript
    variables for the 'Inspect' challenge. It also holds the subtle hint for the 'cURL' challenge.
    """
    return render_template('index.html')

# --- Challenge 2: Heist: The Legacy Data Transfer (cURL Challenge) ---
@app.route('/legacy_transfer')
def legacy_transfer():
    """
    This endpoint serves the flag for the 'cURL' challenge.
    It requires a specific custom HTTP header to be present with a correct value.
    """
    required_header_name = 'X-Vault-Access-Key'
    required_header_value = 'GEEZER_DRILL_CODE_1985' # The secret value for the custom header

    # Check if the incoming request has the required custom header and its value
    if request.headers.get(required_header_name) == required_header_value:
        # If the header is correct, return the flag for this challenge
        return "HEIST{H3ad3r_Drill_Acc3ss_Gr@nted}", 200 # Flag and 200 OK status
    else:
        # If the header is missing or incorrect, deny access with a helpful message
        return "Access Denied: Invalid or missing digital signature for legacy transfer. This endpoint requires specific 'non-standard means' of access.", 403 # 403 Forbidden status

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
# --- For Local Testing ---
# If you want to run this application directly using Python, uncomment the lines below.
# When deploying to platforms like Render, Gunicorn typically handles this.
# if __name__ == '__main__':
#     app.run(debug=True) # debug=True allows for automatic reloading on code changes
