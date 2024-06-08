from flask import Flask, render_template, request, send_file
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    brand = request.form['brand']
    model = request.form['model']
    year = request.form['year']
    mileage = request.form['mileage']
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    # Luo sähköpostipohjan sisältö
    email_content = f"""From: {email}
To: 
Subject: Autoni tiedot
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8

Hei,

Tässä ovat autoni tiedot:

Merkki: {brand}
Malli: {model}
Vuosimalli: {year}
Ajetut kilometrit: {mileage}

Omat tietoni:
Nimi: {name}
Puhelinnumero: {phone}
Sähköposti: {email}

Ystävällisin terveisin,
{name}
"""

    buffer = BytesIO()
    buffer.write(email_content.encode('utf-8'))
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='sahkopostipohja.eml', mimetype='message/rfc822')

if __name__ == '__main__':
    app.run(debug=True)
