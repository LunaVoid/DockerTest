from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

# Route to get all users
@app.route('/')
def landing_page():
  # Pass any data you want to display on the page to the template
  page_title = "My Awesome Landing Page"
  return render_template('index.html', title=page_title)


# Run the app
if __name__ == '__main__':
  from waitress import serve
  serve(app, host="0.0.0.0", port=5050)
