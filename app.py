from flask import Flask
from controllers.car_controllers import marca_bp

app = Flask(__name__)
app.register_blueprint(marca_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
