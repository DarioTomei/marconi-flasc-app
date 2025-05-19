import os

from flask import Flask, render_template

app = Flask(__name__, template_folder="src")
posts =[

    {"title": "baghì", "content": "Miao Miao"},
    {"title": "Lavandino", "content": "Il lavandino è un elemento fondamentale nel bagno, utilizzato per lavarsi le mani, fare la barba, pettinare i capelli e altre attività quotidiane di igiene personale."},
    {"title": "Specchio", "content": "Posizionato sopra il lavandino, serve per vedere il proprio riflesso durante le routine di igiene e per prepararsi."} ,
    {"title": "Water (WC)", "content": "Utilizzato per l'eliminazione dei rifiuti corporei."},
    {"title": "Bidet", "content": "Presente in molte culture, serve per l'igiene intima dopo l'utilizzo del WC."},
    {"title": "Doccia o Vasca da bagno", "content": "Utilizzati per lavare il corpo completamente. La doccia è più rapida, la vasca permette un bagno rilassante."},
    {"title": "Mobiletto/Ripiani", "content": "Per riporre asciugamani, prodotti per l'igiene personale, medicinali e altri oggetti."},
    {"title": "Porta asciugamani", "content": "Per appendere e asciugare gli asciugamani."}   ,
    {"title": "Tappetino da bagno", "content": "Posizionato fuori dalla doccia o vasca per assorbire l'acqua ed evitare di scivolare."},
    {"title": "Cestino", "content": "Per gettare rifiuti come salviette, cotone idrofilo, ecc."}
]
@app.route("/")
def index():
    return render_template('index.html',posts=posts)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
