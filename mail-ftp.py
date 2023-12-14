import imaplib
import email
from ftplib import FTP

# Informations de connexion au serveur IMAP
imap_server = 'serveur_mail.com'
username = 'votre_email'
password = 'votre_mot_de_passe'

# Informations de connexion au serveur FTP
ftp_server = 'ftp.example.com'
ftp_username = 'votre_nom_utilisateur'
ftp_password = 'votre_mot_de_passe'

# Se connecter au serveur IMAP
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(username, password)
mail.select('inbox')

# Recherche des e-mails non lus
result, data = mail.search(None, 'UNSEEN')

# Parcourir tous les e-mails non lus
for num in data[0].split():
    result, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]
    
    # Parsing de l'e-mail
    msg = email.message_from_bytes(raw_email)
    
    # Vérifier les pièces jointes
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        
        # Si c'est une pièce jointe
        filename = part.get_filename()
        if filename:
            # Sauvegarder la pièce jointe dans un fichier local
            with open(filename, 'wb') as f:
                f.write(part.get_payload(decode=True))
                print(f"Pièce jointe {filename} enregistrée.")
                
            # Se connecter au serveur FTP
            ftp = FTP(ftp_server)
            ftp.login(ftp_username, ftp_password)
            
            # Chemin distant sur le serveur FTP où vous souhaitez placer le fichier
            remote_path = '/dossier_sur_le_serveur/'
            
            # Changement de répertoire distant
            ftp.cwd(remote_path)
            
            # Ouverture du fichier en mode lecture binaire
            with open(filename, 'rb') as file:
                # Utilisation de la commande STOR pour envoyer le fichier vers le serveur FTP
                ftp.storbinary('STOR ' + filename, file)
                print(f"Fichier {filename} envoyé avec succès vers le serveur FTP.")
            
            # Fermeture de la connexion FTP
            ftp.quit()

# Fermer la connexion IMAP
mail.close()
mail.logout()
