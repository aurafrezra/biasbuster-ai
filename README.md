# 🧠 BiasBuster AI

**BiasBuster AI** is an intelligent, interactive web app that detects and explains various types of cognitive, social, and political biases present in user-provided text. Built with Flask and powered by AI, it serves as an educational and awareness tool for individuals, researchers, and developers to better understand human biases.

---

## 🌟 Features

- 🔍 **Bias Detection** – Analyzes input text for cognitive, social, or political biases.
- 📊 **Graphical Output** – Pie chart showing percentages of detected bias types.
- 🎯 **Bias Type Explanation** – Detailed and beginner-friendly definitions of each bias.
- 🧩 **Bias Context** – Shows where the bias occurs in the text.
- 🌗 **Dark Mode** – Eye-comfortable, visually rich interface.
- 💬 **Instant Feedback** – Fast, responsive bias report generation.

---

## 🚀 Live Demo

🌐 Visit the live app here: [https://biasbusterai.onrender.com](https://biasbusterai.onrender.com)

---

## 🖼️ Screenshots


(screenshots/input-page.png)

(screenshots/output-report.png)

(screenshots/dark-mode.png)

> Upload your screenshots into a `screenshots/` folder in your repo and replace the paths above.

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/aurafrezra/biasbuster-ai.git
cd biasbuster-aiInstall required packages:

bash
Copy
Edit
pip install -r requirements.txt
Run the app locally:

bash
Copy
Edit
python app.py
🧰 Technologies Used
Frontend: HTML5, CSS3, Bootstrap, Chart.js

Backend: Python, Flask

Design: Responsive layout with dark mode and large visual cards

Data Representation: Pie chart (Chart.js) for bias type visualization

✍️ Example Input
text
Copy
Edit
"I just know she’s not good at math because she’s a girl."
🧠 Detected Biases:

Gender Bias

Confirmation Bias

📊 Pie Chart: 60% Gender Bias, 40% Confirmation Bias

📄 Project Structure
cpp
Copy
Edit
biasbuster-ai/
├── static/
│   ├── style.css
│   └── chart.css
├── templates/
│   ├── index.html
│   └── result.html
├── app.py
├── requirements.txt
└── README.md
💡 Future Improvements
Add multilingual support

Add PDF report generation

Train custom ML model for bias classification

Add user account + history dashboard

🙏 Acknowledgements
Inspired by ethical AI initiatives and behavioral psychology.

Built by Afreen Shaik (aurafrezra)

