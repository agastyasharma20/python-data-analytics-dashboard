from flask import Flask
from config import Config
from models.database import create_table
from routes.dashboard import dashboard_bp

app = Flask(__name__)
app.config.from_object(Config)

create_table()
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)
