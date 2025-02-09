import os
import pandas as pd
import gdown
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Google Drive File ID (Replace with your actual file ID)
FILE_ID = "101168630980204030872"  # Replace with your Google Drive File ID
EXCEL_FILE = "Excel_Search_Main.xlsx"

# Function to Download the Latest Excel File from Google Drive
def download_faq_data():
    url = f"https://docs.google.com/spreadsheets/d/1sDTDT1p8hT6c4Y394uIWJKYg-c72cTaQ/edit?usp=sharing&ouid=101168630980204030872&rtpof=true&sd=true"
    gdown.download(url, EXCEL_FILE, quiet=False)

# Load FAQ Data
def load_faq_data():
    if not os.path.exists(EXCEL_FILE):
        download_faq_data()
    df = pd.read_excel(EXCEL_FILE)
    return df.fillna("")  # Fill empty values with an empty string

faq_data = load_faq_data()

# Search Function
def search_faq(query):
    query = query.lower()
    if faq_data.empty:
        return []
    results = faq_data[faq_data.apply(lambda row: query in row.to_string().lower(), axis=1)]
    return results.to_dict(orient="records")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    # Fetch latest data before searching
    global faq_data
    download_faq_data()
    faq_data = load_faq_data()
    
    results = search_faq(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
