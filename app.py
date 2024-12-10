from flask import Flask, render_template, request
import pickle
model = pickle.load(open('model/model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
   
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
   
    email_text = request.form.get('email-content')
    predictions = model.predict([email_text])
    predictions = 1 if predictions[0] == 1 else -1
    return render_template('index.html', predictions = predictions, email_text = email_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
