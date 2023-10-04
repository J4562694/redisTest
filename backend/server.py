from app import createApp
from flask import render_template

app= createApp()

if __name__== '__main__':
    app.run(debug=True)