from flask import Blueprint, render_template, request, redirect
from models.database import get_connection
from services.analytics import get_summary

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        category = request.form["category"]
        score = request.form["score"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO records (name, age, category, score) VALUES (?, ?, ?, ?)",
            (name, age, category, score)
        )
        conn.commit()
        conn.close()

        return redirect("/dashboard")

    return render_template("form.html")

@dashboard_bp.route("/dashboard")
def dashboard():
    summary = get_summary()
    return render_template("dashboard.html", summary=summary)

