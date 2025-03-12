from flask import Flask, render_template,session
from python import app
from python.Fonctions import inscriptionetu,inscriptionprof,connexionprof,connexionetudiant,ajouter_devoir,infodev,soumettrefichier,infocopiecode,notercopie,updatenote,timeline_prof,afficher_note, generer_statistiques

@app.route('/')
def index():
    return render_template('accueil.html')

@app.route('/connectionprofpage')
def Connexionprof():
    return render_template('connexion_prof.html')

@app.route('/connectionetudiantpage')
def Connexionetu():
    return render_template('connexion_etudiant.html')

@app.route('/inscriptionetudiantcode', methods=['POST'])
def Inscription():
    return inscriptionetu()

@app.route('/connexionprofcode', methods=['POST'])
def ConnexionProf():
    return connexionprof()

@app.route('/connexionetudiantcode', methods=['POST'])
def ConnexionEtudiant():
    return connexionetudiant()

@app.route('/inscriptionprofcode', methods=['POST'])
def Inscriptionprof():
    return inscriptionprof()

@app.route('/inscriptionprofpage')
def Inscriptionprofpage():
    return render_template('inscription_prof.html')

@app.route('/inscriptionetudiantpage')
def Inscriptionetupage():
        return render_template('inscription_etudiant.html')


@app.route('/pageEtudiant')
def ConnexionP():
    return render_template('pageEtudiant.html')


@app.route('/info_devcode',methods=['POST'])
def Infodev():
    return infodev()

@app.route('/InscriptionProf')
def InscriptionP():
    return render_template('InscriptionP.html')

@app.route('/Profil')
def Profil():
    return render_template('Profil.html')

@app.route('/ajouterun_devoir', methods=['POST'])
def Ajouterundevoir():
    return ajouter_devoir()

@app.route('/info_copiecode',methods=['POST'])
def copiecode():
    return infocopiecode()

@app.route('/notercopie',methods=['POST'])
def Notercopie():
    return notercopie()

@app.route('/updatenote',methods=['POST'])
def Updatenote():
    return updatenote()

@app.route('/ajouterun_devoir', methods=['POST'])
def Ajoutdevoir_route():
    return ajouter_devoir()


@app.route('/soumettre',methods=['POST'])
def Soumettre():
    return soumettrefichier()


@app.route('/timeline')
def timeline_route():
    return timeline_client()

@app.route('/timelineP')
def timelineprof_route():
    return timeline_prof()

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/examen')
def examen_route():
    return render_template('examen.html')

@app.route('/accueilp')
def accueilp_route():
    return render_template('accueilp.html')

@app.route('/ajoutdevoirpage')
def AjoutAdmin_route():
    return render_template('Ajoutdevoir.html',sess_username=session['username'],sess_id=session['id'])

@app.route('/copie')
def copie_examen():
    return timeline_prof()

@app.route('/notep')
def note_prof():
    return afficher_note()

@app.route('/statistiquesp')
def statistiques():
    return generer_statistiques()





@app.route('/deconnexion')
def deconnect():
    return render_template('accueilp.html')

