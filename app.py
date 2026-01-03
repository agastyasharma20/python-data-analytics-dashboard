from flask import Flask
from models.database import create_table
from routes.dashboard import dashboard_bp

app = Flask(__name__)

# Create DB table on first run
create_table()

# Register routes
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=True)
