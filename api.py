from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np



@app.route('/')
def home():
	return render_template('index.html')
app = Flask(__name__)
if __name__ == "__main__":
    app.run()