'''
# === COME SI PRESENTA UN GITHUB === #
• Hai 10 secodni per dire chi sei
• VANTATI → "Problema: ... | Come ho risolto: ..."
• Repo con il tuo nome GitHub (identico)
• Sempre in inglese
• Cosa fai: competenze
• Tech Stack: Linguaggi, Frameworks, Tools ecc..
• Progetti in evidenza: Massimo 4 - devono risolvere il problema
• Contatti: email, social: discord, sito internet.
• Extra: immagini...
'''
# GIT & GITHUB #
# Cos'è
'GIT: Software di CONTROLLO VERSIONE'
'GitHub: Un servizio online ospita le repo - dev social'

# Dove vive
'Git: sul tuo computer'
'GitHub: sul tuo computer + online'

# A cosa serve
'Git: Traccia le modifiche, creare i rami e fare unione di codici.'
'GitHib: Collaborazione, creare e mostrare projects, vedere altri repo...'

# === CONCETTI CHIAVE === #
'Repository: Cartella del progetto'

'Commit: è una "fotografia" delle modifiche'

'Branch: sono dei Rami delle versioni'

'Remote: Repo collegate in locale'

'Clone: Copiare la repo sul vostro PC'

'Fork: Copiare la repo di un altro utente sul TUO GitHub'

# ============================================================= #
# === COMANDI PRINCIPALI === #

# dentro al terminale #
'git config --global user.name "Sarah"'
'git config -- global user.email "la_tua_mail@gmail.com"'


# === CREARE O CLONARE UNA REPO === #
'git init' # Crea una repo locale
'gir clone https://github.com/nome_utente/La-Repo-Da-Clonare.git'

# === STATS === #
'git status' # mostra cosa è cmabiato
'git add file.py' # prepara un file
'git add .' # prepara tutto
'git commit -m "info del commit"' # salva tutto

# === COLLEGARE LA REPO === #
'git remote add origin https://github.com/Rp-ics/Telegram-AI-Bot.git'
'git remote -v'

# === PUSH === #
'git push origin main'
#           ↓     ↓
#    Nome Repo   Nome Branch

# === PRIMO PUSH === #
'git push -u origin main'

# === PULL === #
'git pull origin main'
#           ↓     ↓
#    Nome Repo   Nome Branch

