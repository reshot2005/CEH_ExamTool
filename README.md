# CEH Exam Tool — Mock Test CLI (Python)

A fast, terminal-first **CEH mock test** tool written in Python. Practice timed quizzes, track your scores by domain, and export your results — all using simple JSON question banks (your own content, **no dumps**).

> **Author:** [github.com/reshot2005](https://github.com/reshot2005)

---

## ✨ Features

 
- **Practice mode** (instant feedback, optional explanations)  
- **Domain-wise tracking** (e.g., Recon, Scanning, Enumeration…)  
- **Shuffled questions & answer randomization**  
- **Pause/Resume** sessions with autosave  
- **Import/Export** scores (`.json`/`.csv`)  
- **Result breakdown**: accuracy, time/Q, weak topics  
- **Review mode**: revisit flagged/wrong questions  
- **Clean ANSI UI** with a colorful ASCII banner

---

## 🧰 Tech Stack

- Python 3.0+
- Standard library only (optional: `rich` for prettier UI)

---

## 📦 Installation

```bash
git clone https://github.com/reshot2005/CEH_ExamTool.git
cd CEH_ExamTool
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
## QUICK START
```bash
python CEH_ExamTool.py

```
