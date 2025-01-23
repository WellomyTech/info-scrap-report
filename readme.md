# 🌟 Project Guide to Run Locally 🌟

Welcome to the **Project Setup Guide**! Follow the steps below to get the project up and running on your local machine. 🚀

---

## 🛠️ Prerequisites

Before you start, make sure you have the following installed:

1. **Python 3.11 or above** 🐍
2. A package manager like `pip` 📦

---

## 🚀 Steps to Run the Project

### 1️⃣ Clone the Repository
Make sure you've cloned the repository from the source.

---

### 2️⃣ Create a `.env` File
Inside the **main project folder**, create a `.env` file and add the following variables:

```plaintext
OPEN_AI_API=<Your OpenAI API Key>
GOOGLE_SEARCH_API=<Your Google Search API Key>
SEARCH_ENGINE_ID=<Your Search Engine ID>
```

> 📝 **Note**: Replace `<Your OpenAI API Key>`, `<Your Google Search API Key>`, and `<Your Search Engine ID>` with your actual API credentials.

---

### 3️⃣ Install Required Libraries
Run the following command to install all necessary dependencies:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application
Start the application by running:

```bash
python app.py
```

> ⚠️ Ensure you are using **Python version 3.11 or above** to avoid compatibility issues.

---

### 5️⃣ Access the Application
Once the application is running, open your browser and visit:

**http://localhost:5000**

---

## 📄 Generating Documents

- The process of generating a `.docx` file may take **3–4 minutes**.
- Once the process is complete, the file will be **automatically downloaded** to your system. 📥

---

## 🌐 Hosting the Application Online (Optional)

To host the app publicly, follow these steps:

1. Download **ngrok** from [ngrok official website](https://ngrok.com/). 🔗
2. Run the following command while the app is running locally:

   ```bash
   ngrok http 5000
   ```

3. Ngrok will provide a public URL (e.g., `https://xyz123.ngrok.io`) that you can share to access the application over the internet. 🌍

---

## 🏁 You're All Set!

Enjoy using the application! If you face any issues, feel free to reach out. 🤝

---

### 📧 Contact
For any queries, please contact info@wellomytech.com. ✉️
```