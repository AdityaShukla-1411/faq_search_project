# FAQ Search Website (Flask + Excel)

## 📌 **Project Overview**
This project is a **FAQ Search Website** built using **Flask** and an **Excel sheet** as the database. Users can search for questions, and the website dynamically fetches relevant results from the Excel file. The FAQ data is stored in a shared **Google Drive or Dropbox** folder, allowing multiple team members to update it in real time.

## 🚀 **Features**
- 🔍 **Search Functionality**: Users can search for questions and get real-time answers.
- 📂 **Excel as Database**: The FAQ data is stored in an Excel file (`faq_data.xlsx`).
- 🔄 **Auto-Update**: Any changes made to the Excel file reflect instantly on the website.
- 🌍 **Multi-User Access**: Team members can edit the FAQ file using Google Drive/Dropbox.
- 🎨 **Professional UI**: Responsive and animated frontend with smooth UX.

---

## 🛠 **Setup Instructions**
### **1️⃣ Install Required Dependencies**
First, set up a virtual environment (**recommended**) and install dependencies.

```bash
# Create and activate a virtual environment
python -m venv venv  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

`requirements.txt` file should include all the necessary dependencies to run your Flask project.  


### **🔹 Explanation of Dependencies**
| **Package**  | **Purpose** |
|-------------|------------|
| `flask` | Core web framework for building the FAQ search API. |
| `pandas` | Handles Excel file processing. |
| `gdown` | Downloads the latest FAQ file from **Google Drive**. |
| `openpyxl` | Reads `.xlsx` (Excel) files. |
| `gunicorn` | Production WSGI server (needed for **Render Deployment**). |

### **🔹 Install Dependencies**
Run the following command in your terminal:
```bash
pip install -r requirements.txt
```

This will install all necessary packages for your project.

---

## **🔹 Deploy on Render (Using `requirements.txt`)**
1. **Push `requirements.txt` to GitHub**:
   ```bash
   git add requirements.txt
   git commit -m "Added requirements file"
   git push origin main
   ```
2. **Deploy to Render**:
   - In **Render**, set the **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - Set the **Start Command**:
     ```bash
     gunicorn app:app
     ```

---

### **2️⃣ Store the Excel File in a Shared Cloud Folder**
1. Upload `faq_data.xlsx` to **Google Drive** or **Dropbox**.
2. Share the folder with **edit access** for your team.
3. Find the local sync folder path:
   - Google Drive: `C:\Users\YourUsername\Google Drive\faq_data.xlsx`
   - Dropbox: `C:\Users\YourUsername\Dropbox\faq_data.xlsx`
4. Update the file path in `app.py`:

```python
EXCEL_FILE = "C:/Users/YourUsername/Google Drive/faq_data.xlsx"
```

### **3️⃣ Run the Flask Server**
```bash
python app.py
```
- The website will be available at **http://127.0.0.1:5000/**

---

## 🖥 **Project Structure**
```bash
📂 faq_search_project
├── 📂 templates          # HTML Frontend
│   ├── index.html       # Search Page
├── app.py               # Flask Backend
├── faq_data.xlsx        # FAQ Data (Excel File)
├── requirements.txt     # Python Dependencies
├── README.md            # Project Documentation
```

---

## 🌍 **How to Make This Publicly Accessible?**
To allow others to access the website:
1. Deploy the Flask app on **Render, Vercel, or AWS**.
2. Use **ngrok** to create a public link for local hosting:
   ```bash
   pip install ngrok
   ngrok http 5000
   ```
3. Share the **public URL** with your team.

---

## 🤝 **Contributing**
1. **Fork the Repository** 📌
2. **Clone your Fork** 🖥
   ```bash
   git clone https://github.com/yourusername/faq-search.git
   ```
3. **Make Changes & Push** 🚀
   ```bash
   git add .
   git commit -m "Updated search functionality"
   git push origin main
   ```

---



