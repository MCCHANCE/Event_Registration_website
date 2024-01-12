from app import app

@app.route('/home')
def home():
    return "Hello MCCHANCE, please like and subscribe"