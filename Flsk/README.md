# Flask Notes

python3 -m venv {Virtual env name}

source activate venv name

source deactivate venv name

pip install flask-bootstrap

bootstrap = bootstrap(app)

export FLASK_APP=hello.py

flask db migrate -m "xxx" (Just like a git commit)

flask db downgrade removes last migration
