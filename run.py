from app import app

# creates a shell context that adds the database instance and models to the shell session (flask shell):
from app import db


@app.shell_context_processor
def make_shell_context():
    return {'db': db}


# app.run(debug=True, port=8001)