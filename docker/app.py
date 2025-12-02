from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary in-memory database (resets on restart)
tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    deadline = request.form.get("deadline")

    if title and deadline:
        tasks.append({"title": title, "deadline": deadline})

    return redirect("/")

@app.route("/delete/<int:index>")
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

