# BattleCanvas.py

#
# Définition de la classe BattleCanvas qui va permettre de dessiner
# le jeu...
# Attention : Cette classe n'est pour l'instant pas compatible avec
# la classe Canvas vu en TP...
#

import pygame
from os.path import exists
from model.Constantes import *
from view.Constantes import *
from model.Coordonnees import type_coordonnees
from model.Joueur import type_joueur, getNomJoueur, placerBateauJoueur, getGrilleTirsAdversaire
from model.Joueur import getBateauxJoueur, reinitialiserBateauxJoueur, getGrilleTirsJoueur
from model.Bateau import getSegmentsBateau, estPlaceBateau, est_horizontal_bateau, getNomBateau, getTailleBateau


class BattleCanvas:
    def __init__(self, title: str = "BattleShip", logo: str = "Images/logo_64.png"):
        """
        Initialisation de la fenêtre de BattleShip

        :param title: Titre de la fenêtre (optionnel)
        :param logo: Nom de l'image servant d'icône pour la fenêtre (optionnel)
        """
        pygame.init()
        pygame.font.init()

        # Contenu de la fenêtre
        # Première "ligne" : Nom du joueur --> écriture centrée
        # Seconde "ligne" : Grille des tirs + Grille des bateaux
        # Troisième ligne : chaîne de caractères pour afficher une erreur possible
        # Quatrième ligne : chaîne de caractères affichant l'action requise

        # Chargement de l'icône de la fenêtre
        # Bricolage à cause des tests !
        if not exists(logo):
            logo = "../" + logo
        logo = pygame.image.load(logo)
        pygame.display.set_icon(logo)
        # Définition du titre de la fenêtre
        pygame.display.set_caption(title)
        # Définition de la taille d'un bord (horizontal et vertical)
        self.bord = 10
        # Calcul de la largeur de la fenêtre
        # 3 bords + 2 * taille de la grille
        width = 3 * self.bord + const.DIM * const.DIM_CASE_PX * 2
        # Définition de la hauteur du texte
        self.font_size = 20
        # Calcul de la hauteur de la fenêtre
        # 3 lignes + 1 grille + 5 bords
        height = 5 * self.bord + const.DIM * const.DIM_CASE_PX + 3 * self.font_size
        # Initialisation de la fonte
        self.bold_fonte = pygame.font.SysFont('Arial', self.font_size, bold=True)
        self.fonte = pygame.font.SysFont('Times New Roman', self.font_size)

        # Sauvegarde de la taille de la fenêtre
        self.size = (width, height)
        # Création de la fenêtre
        self.screen = pygame.display.set_mode(self.size)
        # Sauvegarde du titre de la fenêtre
        self.title = title
        # Chargement de toutes les images dans un dictionnaire nommé self.images
        self._load_images()
        # Definition des couleurs par défaut des phrases
        # Nom du joueur : Bleu
        self.player_color = pygame.Color(22, 30, 255)
        # Rendu de la chaîne de caractères du joueur
        self.player_surface = None
        # Problème ou remarques : Rouge
        self.remark_color = pygame.Color(255, 155, 84)
        # Rendu de la chaîne de caractères des remarques
        self.remark_surface = None
        # Action à faire : Vert
        self.action_color = pygame.Color(106, 255, 76)
        # Rendu de la chaîne de caractères des actions
        self.action_surface = None

        # Mémorisation du joueur affiché
        self.joueur = None

        # Rafraichissement de la fenêtre
        self.refresh()

    def refresh(self) -> None:
        """
        Redessine le contenu de la fenêtre

        :return: Rien
        """
        self.screen.fill(pygame.Color(124, 172, 255))
        self.dessine_fonts()
        self.dessine_grille(1)
        self.dessine_grille(2)
        if self.joueur is not None:
            self.dessine_bateaux()
            self.dessine_tirs()
        pygame.display.flip()

    def _load_images(self) -> None:
        """
        Charge les images utiles pour le jeu - Usage interne uniquement

        :return: Rien
        """
        self.images = dict()
        d = const.BATEAUX_IMGS[const.DIM_CASE_PX]
        for k in d:
            (horizontal, vertical) = d[k]
            # Bricolage à cause des tests
            if not exists(horizontal):
                horizontal = "../" + horizontal
                vertical = "../" + vertical
            # print(horizontal, vertical)
            self.images[k] = (pygame.image.load(horizontal).convert_alpha(),
                              pygame.image.load(vertical).convert_alpha())
        d = const.ETATS_IMGS[const.DIM_CASE_PX]
        for k in d:
            # Bricolage à cause des tests
            if not exists(d[k]):
                d[k] = "../" + d[k]
            self.images[k] = pygame.image.load(d[k]).convert_alpha()

    def dessine_bateaux(self):
        """
        Dessine les bateaux du joueur dans la première grille

        Usage interne uniquement
        Utilisation des fonctions :
         - getSegmentsBateau
         - getNomBateau

        :return: Rien
        """
        if self.joueur is not None:
            bateaux = getBateauxJoueur(self.joueur)
            for b in bateaux:
                if estPlaceBateau(b):
                    pos = getSegmentsBateau(b)
                    nom = getNomBateau(b)
                    # Récupération de la première case du bateau
                    coord = pos[0][const.SEGMENT_COORDONNEES]
                    num = 0 if est_horizontal_bateau(b) else 1
                    self.screen.blit(self.images[nom][num], self._get_screen_pos(coord, 1))
                    # Dessin des flammes si le bateau est touché
                    for (coord, état) in pos:
                        if état == const.TOUCHE:
                            self.screen.blit(self.images[état], self._get_screen_pos(coord, 1))

    def dessine_tirs(self) -> None:
        """
        Dessine l'état des tirs du joueur pour chaque case :
         - Rien si aucun tir n'a été effectué (None)
         - Une goutte d'eau si le tir est const.RATE
         - des flammes si le tir est const.TOUCHE
         - une 'flaque d'huile' si le tir est const.COULE

        A usage interne uniquement

        Utilisation des fonctions :
         - getGrilleTirsJoueur
         - getGrilleTirsAdversaire

        :return: Rien
        """
        if self.joueur is not None:
            grille = getGrilleTirsJoueur(self.joueur)
            for li in range(len(grille)):
                for co in range(len(grille[li])):
                    status = grille[li][co]
                    if status is not None:
                        self.screen.blit(self.images[status], self._get_screen_pos((li, co), 2))
            # Dessin des tirs de l'adversaire si la grille est présente
            grille = getGrilleTirsAdversaire(self.joueur)
            # print(f"Affichage de la grille adverse : {grille}")
            if grille is not None:
                for li in range(len(grille)):
                    for co in range(len(grille[li])):
                        status = grille[li][co]
                        if status is not None:
                            self.screen.blit(self.images[status], self._get_screen_pos((li, co), 1))

    def dessine_fonts(self)-> None:
        """
        Dessine les textes :
           Première ligne : nom du joueur - voir la méthode set_player_name(str)
           Seconde ligne : remarque éventuelle - voir la méthode set_remark(str)
           Troisième ligne : action à faire - voir la méthode set_action(str)

        Usage interne uniquement

        :return: Rien
        """
        # Affichage du nom du joueur
        if self.player_surface is not None:
            # Le texte est centré
            bw = (self.size[0] - self.player_surface.get_width()) // 2
            self.screen.blit(self.player_surface, (bw, self.bord))
        # Affichage des remarques/erreurs
        if self.remark_surface is not None:
            # Le texte est centré
            bw = (self.size[0] - self.remark_surface.get_width()) // 2
            self.screen.blit(self.remark_surface, (bw, 3*self.bord + const.DIM*const.DIM_CASE_PX + self.font_size))
        # Affichage de l'action attendue
        if self.action_surface is not None:
            self.screen.blit(self.action_surface, (self.bord, 4*self.bord + 2*self.font_size + const.DIM*const.DIM_CASE_PX))

    def _get_screen_pos(self, pos: tuple, num: int) -> tuple:
        """
        Retourne les coordonnées pixels correspond à la case de la grille donnée
        en paramètre en fonction de la grille visée.

        A usage interne uniquement

        :param pos: Position (ligne, colonne) dans la grille
        :param num: Numéro de la grille (1: position des bateaux, 2: position des tirs)
        :return: tuple (x,y) des coordonnées pixels correspondant
        """
        # Bord horizontal (dépend du numéro de la grille)
        bh = self.bord + (num - 1)*(const.DIM*const.DIM_CASE_PX + self.bord)
        # Bord vertical
        bv = 2*self.bord + self.font_size
        return bh + pos[1]*const.DIM_CASE_PX, bv + pos[0]*const.DIM_CASE_PX

    def _get_cell(self, num: int, px: tuple) -> tuple:
        """
        Retourne un tuple (ligne, colonne) correspondant à la case logique contenant le pixel px

        Usage interne uniquement

        :param num: Numéro de la grille (1 ou 2)
        :param px: tuple (x, y) des coordonnées du point
        :return: Tuple ((ligne, colonne), bouton) de la case logique correspondante
        """
        # Bord horizontal (dépend du numéro de la grille)
        bh = self.bord + (num - 1)*(const.DIM*const.DIM_CASE_PX + self.bord)
        # Bord vertical
        bv = 2*self.bord + self.font_size
        return (px[1] - bv) // const.DIM_CASE_PX, (px[0] - bh) // const.DIM_CASE_PX

    def dessine_grille(self, num: int = 1) -> None:
        """
        Dessine une grille vide

        Usage interne uniquement

        :param num: Numéro de la grille, 1 = grille de gauche, 2 = grille de droite
        :return: Rien
        """
        w = const.DIM*const.DIM_CASE_PX
        p = const.DIM_CASE_PX
        # Bord vertical
        bh = 2*self.bord + self.font_size
        b = self.bord + (num - 1)*(w + self.bord)
        for y in range(0, w, p):
            for x in range(0, w, p):
                self.screen.blit(self.images[const.FOND], (x+b, y+bh))
        # Dessin de la grille
        black = pygame.Color(0, 0, 0)
        for x in range(0, w + p, p):
            # Ligne horizontale
            pygame.draw.line(self.screen, black, (b, x+bh), (b+w, x+bh))
            # Ligne verticale
            pygame.draw.line(self.screen, black, (b+x, bh), (b+x, bh+w))

    def set_player_name(self, name: str, color: pygame.Color = None) -> None:
        """
        Définit le nom du joueur à afficher (première ligne)

        Usage interne uniquement

        :param name: Nom du joueur à afficher
        :param color: Couleur du texte (optionnel)
        :return: Rien
        """
        if name is not None:
            self.player_surface = self.bold_fonte.render(name, True, self.player_color if color is None else color)
            self.refresh()

    def set_remark(self, remark: str = None, color: pygame.Color = None) -> None:
        """
        Définit l'erreur/remarque à afficher (Seconde ligne)

        :param remark: Erreur/remarque à afficher ou rien pour effacer la remarque
        :param color: Couleur du texte (optionnel)
        :return: Rien
        """
        if remark is not None:
            self.remark_surface = self.bold_fonte.render(remark, True, self.remark_color if color is None else color)
            self.refresh()
        elif self.remark_surface is not None:
            self.remark_surface = None
            self.refresh()

    def set_action(self, action: str = None, color: pygame.Color = None) -> None:
        """
        Définit l'action à afficher (Seconde ligne)

        :param action: Action à afficher ou rien pour effacer l'action
        :param color : Couleur du texte (optionnel)
        :return: Rien
        """
        if action is not None:
            self.action_surface = self.bold_fonte.render(action, True, self.action_color if color is None else color)
            self.refresh()
        elif self.action_surface is not None:
            self.action_surface = None
            self.refresh()

    def afficher(self, joueur: list = None) -> None:
        """
        Cette méthode permet d'afficher le jeu du joueur donné en paramètre

        Utilisation des fonctions :
         - getNomJoueur

        :param joueur: Joueur à afficher
        :return: Rien
        """
        if joueur != self.joueur:
            if joueur is not None and not type_joueur(joueur):
                raise ValueError("BattleCanvas.afficher: le paramètre n'est pas un joueur")
            self.set_player_name(getNomJoueur(joueur) if joueur is not None else None)
            self.joueur = joueur
            self.refresh()

    def placer_bateaux(self) -> None:
        """
        Cette méthode permet de positionner les bateaux du joueur affiché.

        Il faut que le joueur soit déjà affiché avant d'appeler cette méthode

        Utilisation des fonctions :
         - getBateauxJoueur
         - estPlaceBateau
         - reinitialiserBateauxJoueur
         - getNomBateaux
         - getTailleBateau
         - placerBateauJoueur

        :return: Rien
        :raise RuntimeError si aucun joueur n'est affiché avant l'appel de cette méthode
        """
        if self.joueur is None:
            raise RuntimeError("Aucun joueur n'est affiché")
        lst_bateaux = getBateauxJoueur(self.joueur)
        # On vérifie qu'aucun bateau n'est placé
        if any([estPlaceBateau(b) for b in lst_bateaux]):
            # Au moins un bateau est placé
            reinitialiserBateauxJoueur(self.joueur)
            self.refresh()
        for bateau in lst_bateaux:
            # On affiche un message pour savoir si le bateau doit être placé verticalement ou horizontalement
            msg = f"Placement de {getNomBateau(bateau)} ({getTailleBateau(bateau)} cases) : voulez-vous le placer horizontalement ou verticalement ?"
            horizontal = self.display_message(msg, ["Horizontalement", "Verticalement"]) == 0
            self.set_action("Choisissez la première case dans la grille de gauche")
            # boucle permettant de choisir une case correcte
            ok = False
            while not ok:
                pos, _ = self.get_clicked_cell(1)
                if not placerBateauJoueur(self.joueur, bateau, pos, horizontal):
                    self.display_message("Le bateau ne peut pas être positionné ici.", ["OK"])
                else:
                    ok = True
            self.refresh()
        self.set_action()

    def get_clicked_cell(self, num: int) -> tuple:
        """
        Attend un click dans la grille dont le numéro est donné en paramètre (1 ou 2)
        et retourne un tuple (ligne, colonne) de la case cliquée

        :param num: Numéro de la grille (1 ou 2)
        :return: Un Tuple ((ligne, colonne), bouton) contenant la position de la case cliquée et le bouton cliqué.
        :raise ValueError si le numéro de la grille n'est pas correct
        """
        if num != 1 and num != 2:
            raise ValueError("Le numéro de la grille doit être 1 ou 2 uniquement")
        position = "gauche" if num == 1 else "droite"
        waiting = True
        res = None
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # On a cliqué sur la fenêtre
                    # On récupère les lignes, colonnes logiques correspondant au click en fonction du numéro de grille
                    res = self._get_cell(num, (event.pos[0], event.pos[1])), event.button
                    if not type_coordonnees(res[0]):
                        res = None
                        self.set_remark("Cliquez dans la grille " + position)
                    else:
                        waiting = False
                        self.set_remark()
        return res

    def display_message(self, message: str, boutons: list = ["Ok"]) -> int:
        """
        Affiche une boîte de dialogue et retourne le numéro de bouton (commençant à 0) cliqué

        :param message: Message de la boîte de dialogue
        :param boutons: Liste des boutons (chaînes de caractères)
        :return: Numéro du bouton cliqué
        """

        # Largeur maximale de la boîte de dialogue : 4/5 de la largeur de la fenêtre
        w_max = 3*self.size[0]//4
        # Premier rendu du message
        txt = self.bold_fonte.render(message, True, (0, 0, 0))
        message_list = [txt]
        if txt.get_width() > w_max:
            # Il faut découper le message !
            # Nombre de caractères :
            nb = (w_max * len(message)) // txt.get_width()
            txt = None
            # Découpe du message
            msgs = message.split(' ')
            # Construction des découpes
            s = ""
            message_list = []
            for m in msgs:
                if len(s) + len(m) <= nb:
                    s = m if len(s) == 0 else s + " " + m
                else:
                    message_list.append(self.bold_fonte.render(s, True, (0, 0, 0)))
                    s = m
            if s is not None:
                message_list.append(self.bold_fonte.render(s, True, (0, 0, 0)))
        # Calcul de la largeur max des textes
        w_t = max([m.get_width() for m in message_list]) + 2*self.bord
        # Création des boutons
        btns = []
        for s in boutons:
            btns.append(self.bold_fonte.render(s, True, (0, 0, 0)))
        # Calcul de la largeur totale des boîtes des boutons
        w = sum([s.get_width() + 2*self.bord for s in btns]) + self.bord*len(btns)
        # print("w =", w, "w_max =", w_max)
        bouton_list = []
        if w > w_max:
            # Il faut découper les boutons sur plusieurs lignes
            w = 0
            lst = []
            for btn in btns:
                _w = btn.get_width() + 3*self.bord
                if w + _w < w_max:
                    lst.append(btn)
                    w += _w
                else:
                    bouton_list.append(lst)
                    w = _w
                    lst = [btn]
            bouton_list.append(lst)
        else:
            bouton_list.append(btns)
        # print("len(bouton_list) =", len(bouton_list))
        # Calcul de la largeur max des boutons
        w_b = max([sum([b.get_width() for b in lst]) + self.bord*(len(lst)+1) for lst in bouton_list])
        # Largeur de la boîte de dialogue
        w_boite = max(w_t, w_b)
        # Calcul de la hauteur de la boîte de dialogue
        h_boite = len(message_list)*self.font_size + (len(message_list)+1)*self.bord + \
            len(bouton_list)*(self.font_size + 3*self.bord) + self.bord
        # On peut maintenant dessiner la boîte de dialogue
        x_boite = (self.size[0] - w_boite) // 2
        y_boite = (self.size[1] - h_boite) // 2
        # Dessin du fond de la boîte
        self.screen.fill((255, 255, 255), (x_boite, y_boite, w_boite, h_boite))
        # Dessin du cadre de la boîte
        pygame.draw.rect(self.screen, (0, 0, 0), (x_boite, y_boite, w_boite, h_boite), 1)
        # Affichage du texte
        y = y_boite + self.bord
        for m in message_list:
            self.screen.blit(m, (x_boite + (w_boite - m.get_width())//2, y))
            y += self.font_size + self.bord
        # Affichage des boutons
        # On construit en même temps les cadres des boutons
        y += self.bord
        btn_cadre = []
        for lst in bouton_list:
            w = sum([btn.get_width() for btn in lst]) + 3*len(lst)*self.bord
            space = (w_boite - w) // 2
            x = space + x_boite
            for btn in lst:
                # Calcul de la largeur du bouton
                w = btn.get_width() + 2*self.bord
                # Calcul de la hauteur du bouton
                h = self.font_size+ 2*self.bord
                # Stockage du cadre et du "texte" du bouton
                btn_cadre.append((x, y, x+w, y+h, btn))
                # Dessin du bouton
                self._display_button(btn_cadre[-1])
                x += w + self.bord
            y += 3*self.bord + self.font_size
        # Mise a jour de la fenêtre
        pygame.display.flip()
        # On attend que l'utilisateur clique sur un bouton...
        # On empêche la sortie de l'application ?...
        clicked_btn = -1
        # Animation du bouton lorsque la souris est dessus
        over_btn = -1
        while clicked_btn == -1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
                    (x, y) = event.pos
                    # On recherche si la position se trouve sur un des boutons
                    over = -1
                    for (n, (x1, y1, x2, y2, _)) in enumerate(btn_cadre):
                        if x1 <= x <= x2 and y1 <= y <= y2:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                clicked_btn = n
                            else:
                                over = n
                    if event.type == pygame.MOUSEMOTION:
                        # On regarde s'il faut redessiner le bouton
                        refresh = False
                        if over != over_btn:
                            if over_btn != -1:
                                # On remet le bouton dans son état normal
                                self._display_button(btn_cadre[over_btn])
                                refresh = True
                            over_btn = over
                            if over_btn != -1:
                                # On active le nouveau bouton
                                self._display_button(btn_cadre[over_btn], actif=True)
                                refresh = True
                        if refresh:
                            pygame.display.flip()
        # On efface la boîte de dialogue
        self.refresh()
        return clicked_btn

    def _display_button(self, cadre: tuple, actif: bool = False, actualise: bool = False):
        """
        Usage interne uniquement : Dessine un bouton avec son texte

        :param cadre: tuple (x1, y1, x2, y2, btn) définissant le cadre du bouton (pt sup gauche, pt inf droit) et le
        contenu (btn) de type pygame.Surface
        :param actif: True si la souris est au-dessus du bouton
        :param actualise: True s'il faut rafraîchir la fenêtre immédiatement
        :return: Rien
        """
        # Récupération du cadre et du contenu
        (x1, y1, x2, y2, btn) = cadre
        w = x2 - x1
        h = y2 - y1
        # Dessin du fond du bouton
        col = (134, 255, 13) if actif else (192, 192, 192)
        self.screen.fill(col, (x1, y1, w, h))
        # Dessin du cadre
        pygame.draw.rect(self.screen, (0, 0, 0), (x1, y1, w, h), 2 if actif else 1)
        # Dessin du texte
        self.screen.blit(btn, (x1 + self.bord, y1 + self.bord))
        if actualise:
            pygame.display.flip()

