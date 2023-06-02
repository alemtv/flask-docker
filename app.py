import os
from src import create_app 

app = create_app(os.getenv("CONFIG_MODE"))

@app.route('/')
def hello():
    return '<h1>Hello from Flask & Docker!!</h1>'

if __name__ == "__main__":
    app.run()