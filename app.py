from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

lessons = []
users = {"name": "admin", "pass": "12345678"}

points = 0

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        uname_check = users.get("name")
        upass_check = users.get("pass")
        if uname_check == username and upass_check == password:
            session
            return redirect("/home")
           
        else:
            return "User not found", 404   
    return render_template("login.html")

@app.route("/")
def index():
    return redirect("/login")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/posts")
def posts():
    return render_template("posts.html", lessons=lessons)

@app.route("/create_lesson", methods=["POST", "GET"])
def create_lesson():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        if title and content:
            lessons.append({"title": title, "content": content})
            return redirect(url_for('posts'))
    return render_template('create_lesson.html')

@app.route("/lesson/<int:lesson_id>")
def lesson_detail(lesson_id):
    if 0 <= lesson_id < len(lessons):
        lesson = lessons[lesson_id]
        return render_template("lessons.html", lesson=lesson, lesson_id=lesson_id)
    return "Lesson not found", 404



if __name__ == "__main__":
    app.run(debug=True)
