from flask import Flask, render_template, request
from questions import QUESTIONS

app = Flask(__name__)

@app.get("/")
def home():
    return render_template(
        "quiz.html", title="Online Exam System", version="v2",
        description="Version 2: Submit your answers to calculate your marks automatically.",
        questions=QUESTIONS
    )

@app.post("/submit")
def submit():
    score = sum(1 for q in QUESTIONS if request.form.get(q["id"]) == q["answer"])
    total = len(QUESTIONS)
    percentage = round(score / total * 100)
    return f"""<!doctype html><html><head><title>Exam Score</title>
    <style>body{{font-family:Arial;max-width:700px;margin:60px auto;padding:20px;background:#f4f7fb}}
    section{{background:white;padding:25px;border-radius:12px}}.score{{font-size:30px;color:#175cd3;font-weight:bold}}</style>
    </head><body><section><h1>Automatic Score</h1><p class="score">{score} / {total}</p>
    <p>Percentage: {percentage}%</p><p>Your marks were calculated automatically after submission.</p>
    <a href="/">Take exam again</a></section></body></html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
