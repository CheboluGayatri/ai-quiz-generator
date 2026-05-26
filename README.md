# 🧠 AI Quiz Generator

A simple quiz application built using Python and Streamlit.

Users can:
- Answer quiz questions
- Check correct/wrong answers
- Move using Next button
- View score and progress
- Restart the quiz
- Save scores automatically

---

# 📁 Project Files

```text
AI-Quiz-Generator/
│
├── app.py
├── questions.txt
├── scores.txt
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Project

```bash
streamlit run quiz.py  --server.port 8503
```

---

# 📝 Question Format

Add questions inside `questions.txt`

Example:

```text
What is Python?|programming language
Who developed Python?|guido van rossum
What keyword is used to create function?|def
```

Format:

```text
Question|Answer
```

---

# ✨ Features

- Random Questions
- Progress Bar
- Sidebar Dashboard
- Answer Validation
- Next Question Button
- Final Score
- Score Saving
- Restart Quiz

---

# 💾 Score Saving

Scores are saved automatically in:

```text
scores.txt
```

---

# 🛠️ Technologies Used

- Python
- Streamlit

---

# 👨‍💻 Author

Gayatri Chebolu