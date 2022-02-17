from flask import Flask
from flask import render_template
from flask import request
#import funkcji z głównego pliku
from Chain import tworz_blok, sprawdz_integralnosc


app = Flask(__name__)


#dekorator
@app.route('/', methods=['POST', 'GET'])
def indeks ():
    if request.method =='POST':
        Od_kogo = request.form.get('Od_kogo')
        Do_kogo = request.form.get('Do_kogo')
        Ilosc = request.form.get('Ilosc')
        
        tworz_blok(Od_kogo=Od_kogo, Do_kogo=Do_kogo, Ilosc=Ilosc)

    return render_template('index.html')

@app.route('/checking')
def sprawdz():

    wyniki = sprawdz_integralnosc()
    return render_template('index.html', wyniki_sprawdzenia=wyniki )

# 

#Flask automatycznie włączy się jeśli pliki się zmienią
if __name__ == '__main__':
    app.run(debug=True)
