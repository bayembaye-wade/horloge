import time

class Horloge:
    def __init__(self):
        self.en_pause = False
        self.mode_12h = False
        self.alarme = None
        self.heure_actuelle = (0, 0, 0)

    def afficher_heure(self, heures, minutes, secondes):
        if self.mode_12h:
            suffixe = "AM" if heures < 12 else "PM"
            heures = heures % 12 if heures % 12 != 0 else 12
            heure_format = "{:02d}:{:02d}:{:02d} {}".format(heures, minutes, secondes, suffixe)
        else:
            heure_format = "{:02d}:{:02d}:{:02d}".format(heures, minutes, secondes)

        print(heure_format)

    def regler_heure(self, heures, minutes, secondes):
        self.heure_actuelle = (heures, minutes, secondes)

    def regler_alarme(self, heures, minutes, secondes):
        self.alarme = (heures, minutes, secondes)

    def afficher_alarme(self):
        if self.alarme == self.heure_actuelle:
            print("Réveil ! L'heure de l'alarme est atteinte.")

    def choisir_mode_affichage(self, mode_12h):
        self.mode_12h = mode_12h

    def mettre_en_pause(self):
        self.en_pause = True

    def relancer(self):
        self.en_pause = False

    def actualiser(self):
        while not self.en_pause:
            maintenant = time.localtime()
            self.heure_actuelle = (maintenant.tm_hour, maintenant.tm_min, maintenant.tm_sec)
            self.afficher_heure(*self.heure_actuelle)
            self.afficher_alarme()
            time.sleep(1)

# Exemple d'utilisation
horloge = Horloge()

# Régler l'heure de départ
horloge.regler_heure(16, 30, 0)

# Régler l'alarme
horloge.regler_alarme(16, 31, 0)

# Choisir le mode 12 heures
horloge.choisir_mode_affichage(True)

# Lancer l'horloge
horloge.actualiser()