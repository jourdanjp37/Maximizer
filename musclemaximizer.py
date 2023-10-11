import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk
import os
import webbrowser

class MuscleMaximizerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MuscleMaximizer-Coach sportif humoristique! Auteur Jean-Philippe Jourdan")
        self.geometry("600x800")

        # Variables pour stocker les informations saisies par l'utilisateur
        self.objectif_var = tk.StringVar()
        self.niveau_var = tk.StringVar()
        self.temps_var = tk.StringVar()
        self.sexe_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.poids_var = tk.StringVar()
        self.taille_var = tk.StringVar()
        self.signe_zodiaque_var = tk.StringVar()

        self.img = self.load_image()

        # Afficher l'image dans une étiquette
        label_image = tk.Label(self, image=self.img)
        label_image.pack(pady=10)

        def load_image(self):
            try:
                chemin_image = "C:\\Users\\jourdan\Desktop\\musclemaximizer\\hamburger.png"
                img = Image.open(chemin_image)
                img = img.resize((100, 100))  # Resize the image to fit the window
                img = ImageTk.PhotoImage(img)
                return img
            except Exception as e:
                print("Error loading the image:", e)
                return None

        # Formulaire pour saisir les informations
        objectif_label = tk.Label(self, text="Objectif :")
        objectif_label.pack()
        objectif_options = ["Prise de masse musculaire", "Perte de poids", "Maintien du poids"]
        objectif_menu = ttk.Combobox(self, textvariable=self.objectif_var, values=objectif_options, state="readonly")
        objectif_menu.pack()

        niveau_label = tk.Label(self, text="Niveau de forme physique :")
        niveau_label.pack()
        niveau_options = ["Débutant", "Intermédiaire", "Avancé"]
        niveau_menu = ttk.Combobox(self, textvariable=self.niveau_var, values=niveau_options, state="readonly")
        niveau_menu.pack()

        temps_label = tk.Label(self, text="Temps disponible pour s'entraîner (en jours) :")
        temps_label.pack()
        temps_entry = tk.Entry(self, textvariable=self.temps_var)
        temps_entry.pack()

        sexe_label = tk.Label(self, text="Sexe :")
        sexe_label.pack()
        sexe_options = ["Homme", "Femme"]
        sexe_menu = ttk.Combobox(self, textvariable=self.sexe_var, values=sexe_options, state="readonly")
        sexe_menu.pack()

        age_label = tk.Label(self, text="Âge :")
        age_label.pack()
        age_entry = tk.Entry(self, textvariable=self.age_var)
        age_entry.pack()

        poids_label = tk.Label(self, text="Poids (en kg) :")
        poids_label.pack()
        poids_entry = tk.Entry(self, textvariable=self.poids_var)
        poids_entry.pack()

        taille_label = tk.Label(self, text="Taille (en cm) :")
        taille_label.pack()
        taille_entry = tk.Entry(self, textvariable=self.taille_var)
        taille_entry.pack()

        # Formulaire pour saisir le signe du zodiaque
        signe_zodiaque_label = tk.Label(self, text="Signe du zodiaque :")
        signe_zodiaque_label.pack()
        signe_zodiaque_options = ["Bélier", "Taureau", "Gémeaux", "Cancer", "Lion", "Vierge", "Balance", "Scorpion", "Sagittaire", "Capricorne", "Verseau", "Poissons"]
        signe_zodiaque_menu = ttk.Combobox(self, textvariable=self.signe_zodiaque_var, values=signe_zodiaque_options, state="readonly")
        signe_zodiaque_menu.pack()

        # Bouton pour générer le programme
        generer_button = tk.Button(self, text="Générer le programme", command=self.generer_programme)
        generer_button.pack(pady=20)

        # Label pour le message de don
        self.don_message = tk.Label(self, text="Pour continuer à répandre le bonheur dans le monde informatique:")
        self.don_message.pack()

        # Bouton pour faire un don
        don_button = tk.Button(self, text="Offrez-moi un café", command=self.faire_don)
        don_button.pack()

        self.mainloop()

    def load_image(self):
        try:
            chemin_image = "hamburger.png"  # Assurez-vous que l'image hamburger.png est présente dans le même répertoire que le script
            img = Image.open(chemin_image)
            img = img.resize((200, 200))  # Resize the image to fit the window
            img = ImageTk.PhotoImage(img)
            return img
        except Exception as e:
            print("Error loading the image:", e)
            return None

    def generer_programme(self):
        # Récupérer les informations saisies par l'utilisateur
        objectif = self.objectif_var.get()
        niveau = self.niveau_var.get()
        temps_disponible = int(self.temps_var.get())
        sexe = self.sexe_var.get()
        age = int(self.age_var.get())
        poids = float(self.poids_var.get())
        taille_cm = float(self.taille_var.get())

        # Conversion de la taille en mètres
        taille = taille_cm / 100

        # Calcul de l'IMC (Indice de Masse Corporelle)
        imc = poids / (taille ** 2)

        # Choix du légume en fonction de l'IMC
        legumes = {
            "asperge": (18.5, 24.9),    # Poids idéal pour asperge : 18.5 à 24.9
            "courgette": (25, 29.9),    # Poids idéal pour courgette : 25 à 29.9
            "patate douce": (30, 34.9), # Poids idéal pour patate douce : 30 à 34.9
            "citrouille": (35, float('inf'))  # Poids idéal pour citrouille : 35 et plus
        }

        legume_choisi = None
        for legume, (poids_min, poids_max) in legumes.items():
            if poids_min <= imc <= poids_max:
                legume_choisi = legume
                break

        if not legume_choisi:
            legume_choisi = random.choice(list(legumes.keys()))

        # Choix de l'adjectif approprié en fonction du poids
        adjectif = ""
        if imc < 18.5:
            adjectif = "Anorexique"
        elif 18.5 <= imc < 25:
            adjectif = "en forme"
        elif 25 <= imc < 30:
            adjectif = "Playboy"
        else:
            adjectif = "sumotori"

        # Calcul du nombre de calories nécessaires en fonction de l'objectif
        if sexe == "Homme":
            maintenance_calories = 10 * poids + 6.25 * (taille * 100) - 5 * age + 5
        else:
            maintenance_calories = 10 * poids + 6.25 * (taille * 100) - 5 * age - 161

        if objectif == "Prise de masse musculaire":
            calories_objectif = maintenance_calories + 300
        elif objectif == "Perte de poids":
            calories_objectif = maintenance_calories - 500
        else:
            calories_objectif = maintenance_calories

        # Calcul du nombre d'hamburgers équivalents par jour
        calories_par_hamburger = 350  # Nombre moyen de calories dans un hamburger
        hamburgers_equivalents = calories_objectif / calories_par_hamburger

        # Calculer le nombre d'heures de sommeil nécessaires
        heures_sommeil = self.calculer_heures_sommeil(objectif, niveau)

        # Choix du jour favorable en fonction du signe du zodiaque
        signe_zodiaque = self.signe_zodiaque_var.get()
        jours_favorables_zodiaque = {
            "Bélier": ["Lundi", "Mercredi"],
            "Taureau": ["Mardi", "Jeudi"],
            "Gémeaux": ["Mercredi", "Vendredi"],
            "Cancer": ["Jeudi", "Samedi"],
            "Lion": ["Vendredi", "Dimanche"],
            "Vierge": ["Samedi", "Lundi"],
            "Balance": ["Dimanche", "Mardi"],
            "Scorpion": ["Lundi", "Mercredi"],
            "Sagittaire": ["Mardi", "Jeudi"],
            "Capricorne": ["Mercredi", "Vendredi"],
            "Verseau": ["Jeudi", "Samedi"],
            "Poissons": ["Vendredi", "Dimanche"]
        }

        jours_favorables_zodiaque = jours_favorables_zodiaque.get(signe_zodiaque, ["Lundi", "Mardi"])

        # Adapter les jours d'entraînement au jour favorable
        jours_entrainement = jours_favorables_zodiaque[:temps_disponible]

        # Exemple de génération de programme d'entraînement basé sur les informations saisies
        exercices_haut_corps = {
            "Pompes": "3 séries de 10 répétitions",
            "Triceps Dips": "3 séries de 12 répétitions",
            "Traction sur barre fixe": "3 séries de 8 répétitions"
        }
        exercices_bas_corps = {
            "Squats": "3 séries de 10 répétitions",
            "Fentes": "3 séries de 10 répétitions",
            "Gainage": "3 séries de 30 secondes"
        }
        exercices_abdos = {
            "Crunchs": "3 séries de 15 répétitions",
            "Levés de jambes": "3 séries de 12 répétitions"
        }
        exercices_cardio = {
            "Course à pied": "20 minutes",
            "Jumping Jacks": "3 séries de 30 secondes",
            "Corde à sauter": "3 séries de 1 minute"
        }

        programme = {}
        for jour in jours_entrainement[:temps_disponible]:
            exercices_jour = []
            if len(programme) % 2 == 0:
                exercices_jour.append(random.choice(list(exercices_haut_corps.items())))
                exercices_jour.append(random.choice(list(exercices_abdos.items())))
            else:
                exercices_jour.append(random.choice(list(exercices_bas_corps.items())))
                exercices_jour.append(random.choice(list(exercices_cardio.items())))

            programme[jour] = exercices_jour

        # Récupérer la phase lunaire
        phase_lunaire, effet_phase_lunaire = self.get_phase_lunaire()

        # Afficher le résultat dans une fenêtre pop-up
        result_popup = tk.Toplevel(self)
        result_popup.title("Auteur Jean-Philippe Jourdan - Programme d'entraînement personnalisé")
        result_popup.geometry("600x400")

        result_text = f"Objectif : {objectif}\nNiveau de forme physique : {niveau}\nTemps disponible : {temps_disponible} jours\nSexe : {sexe}\nÂge : {age}\n\n"
        result_text += f"IMC (Indice de Masse Corporelle) : {imc:.2f}\n\n"
        result_text += f"Vous avez un IMC de {imc:.2f}, vous ressemblez à une {legume_choisi} {adjectif} !\n\n"
        result_text += f"Nombre de calories nécessaires par jour : {calories_objectif:.0f} calories\n"
        result_text += f"Nombre d'hamburgers équivalents par jour : environ {hamburgers_equivalents:.1f} hamburgers\n\n"
        result_text += f"Nombre d'heures de sommeil nécessaires : environ {heures_sommeil:.1f} heures\n\n"
        result_text += f"Jours favorables pour l'entraînement : {', '.join(jours_entrainement)}\n\n"
        result_text += f"Phase lunaire : {phase_lunaire} (Favorable pour {'prendre de la masse' if objectif == 'Prise de masse musculaire' else 'maigrir'})\n"
        result_text += f"Effet de la phase lunaire : {effet_phase_lunaire}\n\n"

        result_text += "Programme d'entraînement :\n"
        for jour, exercices in programme.items():
            result_text += f"{jour} : {exercices[0][0]} - {exercices[0][1]} ; {exercices[1][0]} - {exercices[1][1]}\n"

        result_text += f"\nN'oubliez pas de manger vos Hamburgers ! Vous avez un IMC de {imc:.2f}, donc vous ressemblez à une {legume_choisi}. Bon entraînement !"

        result_label = tk.Label(result_popup, text=result_text, font=("Helvetica", 12))
        result_label.pack(padx=20, pady=10)

        # Enregistrer les résultats dans un fichier texte sur le bureau de Windows
        results_file_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'Votre Mémo Résultats.txt')
        with open(results_file_path, 'w', encoding='utf-8') as file:
            file.write(result_text)

         # Bouton pour générer le programme
        generer_button = tk.Button(self, text="Générer le programme", command=self.generer_programme)
        generer_button.pack(pady=20)

        # Appel de la méthode pour afficher la fenêtre de dons
        self.afficher_fenetre_principale()

        # Début de la boucle principale
        self.mainloop()

    def get_phase_lunaire(self):
        # Phases lunaires ludiques avec leurs effets
        phases_ludiques = {
            "Pleine Lune": "Favorable pour prendre de la masse musculaire et avoir une forte énergie",
            "Lune Rousse": "Favorable pour maigrir et éliminer les toxines",
            "Lune des Amoureux": "Favorable pour se détendre et améliorer son sommeil",
            "Lune Blanche": "Favorable pour la créativité et la concentration",
            "Lune Bleue": "Favorable pour se ressourcer et se reposer",
            "Lune d'Or": "Favorable pour se motiver et se fixer des objectifs",
            "Lune Noire": "Favorable pour se recentrer et méditer",
            "Lune d'Argent": "Favorable pour améliorer sa souplesse et son équilibre"
        }

        # Choix aléatoire d'une phase lunaire ludique
        phase_lunaire = random.choice(list(phases_ludiques.keys()))
        effet_phase_lunaire = phases_ludiques[phase_lunaire]

        # Ajout d'un numéro de semaine/mois
        numero_temps = random.randint(1, 4)  # Choix aléatoire du numéro de semaine/mois
        temps_label = "ème semaine"
        if numero_temps == 1:
            temps_label = "ère semaine"
   
        phase_lunaire += f" ({numero_temps} {temps_label} du mois)"

        return phase_lunaire, effet_phase_lunaire

    def calculer_heures_sommeil(self, objectif, niveau):
        # Exemple de calcul du nombre d'heures de sommeil nécessaires
        heures_sommeil = 7.0
        if objectif == "Prise de masse musculaire":
            heures_sommeil += 1.0
        elif objectif == "Perte de poids":
            heures_sommeil -= 0.5
        
        if niveau == "Débutant":
            heures_sommeil += 0.5
        elif niveau == "Avancé":
            heures_sommeil -= 0.5

        return heures_sommeil
    
    def faire_don(self):
        webbrowser.open("https://www.paypal.com/donate/?hosted_button_id=HFV7MQW36JXWJ")

if __name__ == "__main__":
    app = MuscleMaximizerApp()
    app.mainloop() 