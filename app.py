import pandas as pd
import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

EXCEL_FILE = "Excel_Search_Main.xlsx"  

def load_faq_data():
    if os.path.exists(EXCEL_FILE):
        df = pd.read_excel(EXCEL_FILE)
        return df.fillna("")
    return pd.DataFrame()

faq_data = load_faq_data()

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
    results = search_faq(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)