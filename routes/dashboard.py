from flask import Blueprint, render_template, request, redirect, send_file
from services.analytics import get_summary, export_to_csv
from models.database import get_connection


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Fetch & clean inputs
            name = request.form.get("name", "").strip()
            age = request.form.get("age", "").strip()
            category = request.form.get("category", "").strip()
            score = request.form.get("score", "").strip()

            # Basic validation
            if not name or not category:
                return "Invalid input", 400

            if not age.isdigit() or not score.isdigit():
                return "Age and score must be numbers", 400

            age = int(age)
            score = int(score)

            if age <= 0 or score < 0:
                return "Invalid age or score values", 400

            # Insert into database
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO records (name, age, category, score) VALUES (?, ?, ?, ?)",
                (name, age, category, score)
            )
            conn.commit()
            conn.close()

            return redirect("/dashboard")

        except Exception as e:
            return f"Unexpected error: {str(e)}", 500

    return render_template("form.html")


@dashboard_bp.route("/dashboard")
def dashboard():
    selected_category = request.args.get("category")
    summary = get_summary(selected_category)

    return render_template(
        "dashboard.html",
        summary=summary,
        selected_category=selected_category
    )
@dashboard_bp.route("/export")
def export_data():
    selected_category = request.args.get("category")
    file_path = export_to_csv(selected_category)
    return send_file(file_path, as_attachment=True)
@dashboard_bp.route("/api/data")
def api_data():
    selected_category = request.args.get("category")
    summary = get_summary(selected_category)

    if not summary:
        return {"message": "No data available"}, 404

    return summary
