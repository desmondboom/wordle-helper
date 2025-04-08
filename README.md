# 🧩 Wordle Helper CLI

A simple and interactive command-line tool to help you solve Wordle puzzles.  
Supports pattern-based word matching, required and excluded letters, and multilingual prompts (English / 中文).

[中文版本](./README_zh.md)

---

## 🚀 Features

- Pattern input with `_` representing unknown letters (e.g. `_a_im_`)
- Required letters (must appear somewhere in the word)
- Excluded letters (must not appear)
- Interactive Q&A mode (multi-round)
- Language selection: English or Chinese
- Automatically downloads English word list from NLTK

---

## 📦 Installation

### 1. Clone the project

```bash
git clone https://github.com/your-username/wordle-helper.git
cd wordle-helper
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🕹️ How to Use

```bash
python wordle_helper.py
```

You will be prompted to select a language and then answer:

```
Select language / 选择语言: (en/zh): en

🎯 Welcome to the Wordle Helper (Interactive Mode)

Enter your pattern (use _ for unknown letters, e.g. _a_im_):
Enter required letters (comma-separated, e.g. e,o):
Enter excluded letters (comma-separated, e.g. t,s,r):
```

After each round, you can choose whether to continue or exit.

---

## 📂 Project Structure

```
wordle-helper/
├── wordle_helper.py      # Main CLI script
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## 📌 Dependencies

- Python 3.7+
- `nltk` (for the English word list)

The word list will be downloaded automatically the first time you run the script.

---

## 🧠 Future Ideas

- Support green/yellow/gray logic like real Wordle
- Prioritize common words using frequency data
- Export results to a file
- Add GUI or web interface

Pull requests welcome! 🚀

---

## 📜 License

MIT License
