# Constantes.py

#
# Définition des constantes utilisées dans ce module
#
import const

#
# Définition de la taille des cases en pixel et de l'image correspondante
#  (adapter le nom des images en fonction de la taille des cases...)
#
const.DIM_CASE_PX = 64

# Dictionnaire des images en fonction de la dimension, puis en fonction du nom du bateau.
# Le dictionnaire renvoie un Tuple (image horizontale, image verticale)
const.BATEAUX_IMGS = { 40:
                          {
                              const.PORTE_AVION: ("Images/porte_avion_40.png", "Images/porte_avion_40d.png"),
                              const.CUIRASSE: ("Images/cuirasse_40.png", "Images/cuirasse_40d.png"),
                              const.CROISEUR: ("Images/croiseur_40.png", "Images/croiseur_40d.png"),
                              const.TORPILLEUR: ("Images/torpilleur_40.png", "Images/torpilleur_40d.png"),
                              const.SOUS_MARIN: ("Images/sous_marin_40.png", "Images/sous_marin_40.png")
                          },
                       64:
                        {
                               const.PORTE_AVION: ("Images/porte_avion_64.png", "Images/porte_avion_64d.png"),
                               const.CUIRASSE: ("Images/cuirasse_64.png", "Images/cuirasse_64d.png"),
                               const.CROISEUR: ("Images/croiseur_64.png", "Images/croiseur_64d.png"),
                               const.TORPILLEUR: ("Images/torpilleur_64.png", "Images/torpilleur_64d.png"),
                               const.SOUS_MARIN: ("Images/sous_marin_64.png", "Images/sous_marin_64.png")
                           }
}

const.ETATS_IMGS = { 40:
                        {
                            const.FOND: "Images/water_40.png",
                            const.RATE: "Images/rate_40.png",
                            const.TOUCHE: "Images/touche_40.png",
                            const.COULE: "Images/coule_40.png"
                        },
    64:
        {
            const.FOND: "Images/water_64.png",
            const.RATE: "Images/rate_64.png",
            const.TOUCHE: "Images/touche_64.png",
            const.COULE: "Images/coule_64.png"
        }
}


