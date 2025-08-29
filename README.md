# Visual-Cryptography-Tool-for-Secret-Image-Sharing
A Visual Cryptography Tool using Flask &amp; OpenCV. Encrypts images into secret shares and reconstructs them for secure sharing. Simple web interface with upload, encrypt, and decrypt features.
# Visual Cryptography Tool 🔐🖼️

## 📌 Description
A Visual Cryptography Tool built with **Flask** and **OpenCV** that splits an image into **two secret shares** for secure sharing.  
The original image is revealed **only when both shares are combined**, ensuring confidentiality.

---

## ⚙️ Tools & Technologies Used
- **Python 3**
- **Flask** → Web framework for backend
- **OpenCV** → Image encryption & processing
- **NumPy** → Matrix & pixel operations
- **HTML/CSS + Bootstrap** → Frontend UI
- **Jinja2** → Template rendering

---

## ✨ Features
- Upload grayscale or color images.
- Encrypt images into two random-looking shares.
- Decrypt images back using both shares.
- Simple and responsive web interface.
- Download both encrypted shares and decrypted output.
- Secure sharing: One share reveals nothing without the other.

---

## ✅ Advantages
- Provides **high security** with visual secret sharing.
- **No complex computation** is required to decrypt—just overlay shares.
- Lightweight and **easy to deploy** using Flask.
- Suitable for academic, research, and practical security use cases.

---

## ⚠️ Limitations
- Works best for **binary/grayscale** images; limited support for high-quality colored images.
- Repeated encryption/decryption may cause **quality loss**.
- Requires **both shares**; one share alone cannot reconstruct the image.

---

## 🔄 How It Works
1. **Upload** → User uploads an input image.  
2. **Encryption** → The system splits the image into **two shares**:  
   - Each share looks like random noise.  
   - Individually, they reveal nothing.  
   - When combined, the original image is revealed.  
3. **Decryption** → Overlay both shares → Get the original image back.  

---

## 📖 Example Problem & Process
**Problem**: A university wants to share exam answer scripts securely. No single department should access the full document alone.  

**Process**:  
1. Upload scanned answer script.  
2. Tool generates **Share1.png** and **Share2.png**.  
3. Department A keeps Share1, Department B keeps Share2.  
4. Only when they overlay both shares → full answer script is visible.  

---

## 🌍 Real-World Applications
- **Secure Government Communication** → Classified images/maps shared across multiple departments.  
- **Banking & Financial Sector** → Secure transfer of scanned documents like cheques, contracts.  
- **Medical Field** → Sharing patient medical scans (MRI, X-rays) between hospitals securely.  
- **Military & Defense** → Confidential maps or strategies split into shares for distributed access.  
- **Authentication Systems** → Share-based image verification for two-factor authentication.  
- **Educational Use** → Secure distribution of question papers and answer sheets.  

---

## 🛠️ Environment Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone <repo-url>
cd CNS

------
### 2️⃣ Create Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

You can install everything directly from requirements.txt:

pip install -r requirements.txt


Or install packages manually:

pip install flask==3.0.3
pip install opencv-python==4.10.0
pip install numpy==2.0.1

4️⃣ Run the Application
python app.py

5️⃣ Access in Browser

Open 👉 http://127.0.0.1:5000

📷 Demo Screens (to be added)

Upload Page → Encrypt Image

Download Generated Shares

Combine Shares → Decrypt Result
