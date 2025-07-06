# 🔍 Synapse - TCP Port Scanner in Python

**Synapse** is a simple and efficient TCP port scanner built with Python. It allows you to scan a range of TCP ports on a target host and optionally grab service banners for further analysis. Designed to be lightweight and easy to understand, this tool is ideal for cybersecurity learners and professionals alike.

---

## 📌 Features

- ✅ Fast and lightweight TCP scanning
- 🔎 Optional banner grabbing support
- ⏱️ Customizable timeout settings
- 🧠 Beginner-friendly code structure
- 💻 CLI-based interface

---

## 🧰 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/synapse.git
cd synapse
```

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

If you're using only Python standard libraries, you may not need this step. If any external libraries are used (like `colorama`), install with:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 📎 Basic Syntax

```bash
python synapse.py <target_ip> <start_port> <end_port>
```

### 📌 Example

```bash
python synapse.py 192.168.1.10 20 100
```

This command will scan TCP ports from 20 to 100 on the target IP `192.168.1.10`.

---

## 🧪 Sample Output

```
[TCP] Port 22 is OPEN → OpenSSH 7.9
[TCP] Port 80 is OPEN → Apache httpd
[TCP] Port 443 is CLOSED
```

---

## 📁 File Structure

```
synapse/
├── synapse.py           # Main TCP scanner script
├── README.md            # Documentation
└── requirements.txt     # Dependencies list (if needed)
```

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and share this code with proper attribution.

---

## 🙋‍♂️ Author

**Rishikesh M**  
GitHub: [@Rishikesh-m](https://github.com/Rishikesh-m)  
LinkedIn: [linkedin.com/in/yourname](https://linkedin.com/in/yourname)  
Website: [@Mockychuck](https://mockychuck.pages.dev)

---

> Feel free to contribute or suggest improvements by opening a pull request!
