from flask import Flask, render_template, request
from questions import QUESTIONS

app = Flask(__name__)

@app.get("/")
def home():
    return render_template(
        "quiz.html", title="Online Exam System", version="v3",
        description="Version 3: Take the quiz, receive your final score, and review each answer.",
        questions=QUESTIONS
    )

@app.post("/submit")
def submit():
    score = 0
    review = []
    for q in QUESTIONS:
        selected = request.form.get(q["id"], "")
        is_correct = selected == q["answer"]
        if is_correct:
            score += 1
        review.append({
            "question": q["question"],
            "selected_text": q["options"].get(selected, "No answer"),
            "correct_text": f'{q["answer"]}. {q["options"][q["answer"]]}',
            "is_correct": is_correct,
            "explanation": q["explanation"],
        })
    total = len(QUESTIONS)
    percentage = round(score / total * 100)
    message = "Great work!" if percentage >= 70 else "Keep practising and try again."
    return render_template("result.html", score=score, total=total,
                           percentage=percentage, message=message, review=review)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
