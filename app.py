from flask import Flask, render_template










@app.route('/color')
def color():
    return render_template('color.html')