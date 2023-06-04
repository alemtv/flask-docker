import os

# App Initialization
from src import create_app
app = create_app(os.getenv("CONFIG_MODE"))

@app.route('/')
def hello():
    return '<h1>Hello from Flask & Docker!!!</h1>'

# Applications Routes
from src.cars import urls
from src.makers import urls

if __name__ == "__main__":
    app.run(debug=True)