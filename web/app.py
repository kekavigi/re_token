from flask import Flask, render_template, url_for, request

app = Flask(__name__)


test_word = """Saya membeli barang seharga Rp 5.000 di Jl. Prof. Soepomo no. 67.
Hey, prof. , yang manakah penulisan yang benar, "Prof. Sutomo" atau "prof. Sutomo"?
Apakah saya dapat memasukan atau memasukkan?
tejaring (terjaring) sindikat narkoba tahun 2017
ke arah mana saya harus pergi? kearah mana?"""


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        raw_text = request.form['raw_text']
        return render_template(
                    'index.html',
                    input_text=raw_text,
                    output_text=saran(raw_text),
                    koreksi=korek)
    else:
        return render_template(
                    'index.html',
                    input_text='<b>Anda</b> dapat menuliskan teks <i>di sini.</i>',
                    identifikasi='',
                    koreksi='')

if __name__ == '__main__':
    app.run()
