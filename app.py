from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the web form
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SupplySide Global Schedule URL Creator</title>
</head>
<body>
    <h1>SupplySide Global Schedule URL Creator</h1>
    <p>Copy the Swapcard URL that you want to link to. If you have filters or searches, make sure you copy the entire URL. Paste that URL below:</p>
    <form method="POST">
        <label for="swapcard_url">Swapcard URL:</label><br>
        <input type="text" id="swapcard_url" name="swapcard_url" style="width: 60%;" placeholder="Enter your Swapcard URL" required><br><br>
        <button type="submit">Get New URL</button>
    </form>
    {% if new_url %}
        <h3>Here is your link to the filtered iframe schedule. Make sure to test the link to make sure it works as expected.</h3>
        <p>
            <input type="text" value="{{ new_url }}" style="width: 60%;" readonly><br><br>
            <button onclick="navigator.clipboard.writeText('{{ new_url }}')">Copy to Clipboard</button>
        </p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    new_url = None
    if request.method == "POST":
        old_url = request.form.get("swapcard_url")
        # Process the URL
        if "/planning" in old_url or "/plannings" in old_url:
            split_url = old_url.split("/planning", 1)
            remaining_url = "/planning" + split_url[1]
            # Don't encode the URL - let the browser handle it naturally
            new_url = f"https://www.supplysideglobal.com/en/expo/event-information/schedule.html?page={remaining_url}"
    return render_template_string(HTML_TEMPLATE, new_url=new_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
