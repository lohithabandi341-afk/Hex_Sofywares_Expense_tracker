from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        date = request.form["date"]
        category = request.form["category"]
        amount = float(request.form["amount"])
        description = request.form["description"]

        expenses.append({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })

        return redirect("/")

    total = sum(exp["amount"] for exp in expenses)
    return render_template("index.html", expenses=expenses, total=total)

if __name__ == "__main__":
    app.run(debug=True)
