from flask import Flask

app = Flask(_name_)

@app.route('/')
def hello():
    return '\n\n\t\tBHUMIKA 21BCS7843'

if _name_ == '_main_':
    app.run(debug=True)
