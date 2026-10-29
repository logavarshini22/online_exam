from flask import Flask, render_template, request
from questions import QUESTIONS

app = Flask(__name__)

@app.get("/")
def home():
    return render_template(
        "quiz.html", title="Online Exam System", version="v1",
        description="Version 1: Attempt the multiple-choice quiz. This version focuses on conducting the test.",
        questions=QUESTIONS
    )

@app.post("/submit")
def submit():
    # v1 accepts and acknowledges submitted answers; scoring is added in v2.
    answered = sum(1 for q in QUESTIONS if request.form.get(q["id"]))
    return f"""<!doctype html><html><head><title>Submission received</title>
    <style>body{{font-family:Arial;max-width:700px;margin:60px auto;padding:20px;background:#f4f7fb}}
    section{{background:white;padding:25px;border-radius:12px}}</style></head><body><section>
    <h1>Exam submitted successfully</h1><p>You answered {answered} of {len(QUESTIONS)} questions.</p>
    <p>Version 1 records the submission. Automatic scoring is introduced in v2.</p>
    <a href="/">Back to exam</a></section></body></html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
