from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lessons = []

@app.route("/")
def index():
    return render_template("home.html", lessons=lessons)

@app.route("/create_lesson", methods=["POST", "GET"])
def create_lesson():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if title and content:
            lessons.append({"title": title, "content": content})
            return redirect(url_for('index'))
    return render_template('create_lesson.html')

@app.route("/lesson/<int:lesson_id>")
def lesson_detail(lesson_id):
    if 0 <= lesson_id < len(lessons):
        lesson = lessons[lesson_id]
        return render_template("lessons.html", lesson=lesson, lesson_id=lesson_id)
    return "Lesson not found", 404

if __name__ == "__main__":
    app.run(debug=True)
