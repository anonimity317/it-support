from website import create_app
from flask import Flask, render_template

app = create_app()


if __name__ in '__main__':
    app.run(debug=True)


    