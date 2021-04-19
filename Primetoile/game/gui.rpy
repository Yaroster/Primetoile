﻿################################################################################
## Initialisation
################################################################################

## L'instruction init offset fait exécuter les instructions d'initialisation de
## ce fichier tavant les instructions init des autres fichiers.
init offset = -2

## Appelé gui.init réinitialise les styles à leurs valeurs par défaut et
## initialise la largeur et la hauteur du jeu.
init python:
    gui.init(2560, 1440)



################################################################################
## Variables de Configuration du GUI
################################################################################


## Couleurs ####################################################################
##
## Les couleurs du texte dans l’interface.

## Une couleur utilisée dans l’interface pour mettre l’accent sur un texte
## (surbrillance).
define gui.accent_color = u'#000000'

## La couleur utilisée pour le texte d’un bouton quand il n’a jamais été
## sélectionné ou survolé.
define gui.idle_color = u'#aaaaaa'

## La petite couleur est utilisé pour les textes courts qui nécessitent d’être
## assombris ou éclairés pour obtenir le même effet.
define gui.idle_small_color = u'#888888'

## Cette couleur est utilisée pour les boutons et les barres qui sont survolées.
define gui.hover_color = u'#000000'

## Cette couleur est utilisé pour le texte d’un bouton sélectionné, mais qui n’a
## pas le focus. Un bouton est sélectionné s’il est sur l’écran actuel ou si
## c’est la valeur de préférence.
define gui.selected_color = u'#555555'

## La couleur utilisée pour le texte d’un bouton qui ne peut pas être
## sélectionné.
define gui.insensitive_color = u'#aaaaaa7f'

## Couleurs utilisées pour les portions de barres qui ne sont pas remplies.
## Elles ne sont pas utilisées directement, mais quand les fichiers d’images
## sont régénérés.
define gui.muted_color = u'#666666'
define gui.hover_muted_color = u'#999999'

## Les couleurs utilisées pour les dialogues et les menus de choix.
define gui.text_color = u'#fff'
define gui.interface_text_color = u'#000'


## Polices et tailles de police ################################################

## Les polices utilisées pour le texte du jeu.
define gui.text_font = "DejaVuSans.ttf"

## Les polices utilisées pour le nom des personnages.
define gui.name_text_font = "DejaVuSans.ttf"

## Les polices utilisées pour les textes « hors du jeu ».
define gui.interface_text_font = "DejaVuSans.ttf"

## La taille normale pour les dialogues.
define gui.text_size = 44

## La taille pour le nom des personnages.
define gui.name_text_size = 60

## La taille du texte dans l’interface de jeu.
define gui.interface_text_size = 44

## La taille des libellés dans l’interface de jeu.
define gui.label_text_size = 48

## La taille du texte dans la zone de notification.
define gui.notify_text_size = 32

## La taille du titre du jeu.
define gui.title_text_size = 100


## Menu du jeu et menu principal ###############################################

## Les images utilisées pour le menu principal et le menu du jeu.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogue ####################################################################
##
## Ces variables contrôlent comment les dialogues sont affichés une ligne à la
## fois.

## La hauteur de la fenêtre contenant les dialogues.
define gui.textbox_height = 370

## L’emplacement vertical de la zone de texte à l’écran. 0.0 pour le haut, 0.5
## pour le centre et 1.0 pour le bas.
define gui.textbox_yalign = 1.0


## L’emplacement relatif à la zone de texte du nom du personnage en train de
## parler. La valeur peut être un nombre entier de pixels depuis la gauche ou le
## haut ou 0.5 pour le centre.
define gui.name_xpos = 480
define gui.name_ypos = 0

## L’alignement horizontal du nom du personnage. La valeur peut être 0.0 pour un
## alignement à gauche, 0.5 pour le centrer et 1.0 pour un alignement à droite.
define gui.name_xalign = 0.0

## La largeur, profondeur et les bords de la zone contenant le nom du personnage
## ou « None » pour le dimensionner automatiquement.
define gui.namebox_width = None
define gui.namebox_height = None

## Les bordures de la zone contenant le nom du personnage dans l’ordre suivant
## gauche, haut, droite, bas.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Si « True » (vrai), l’arrière plan de zone du nom sera en mosaïque, si
## « False »(faux), l’arrière plan de la zone du nom sera mis à l’échelle.
define gui.namebox_tile = False


## L’emplacement du dialogue relatif à la zone de texte. La valeur peut être un
## nombre entier de pixels depuis la gauche ou le haut ou 0.5 pour le centre.
define gui.dialogue_xpos = 536
define gui.dialogue_ypos = 100

## La largeur maximale en pixels de la zone de dialogue.
define gui.dialogue_width = 1488

## L’alignement horizontal de la zone de dialogue. La valeur peut être 0.0 pour
## un alignement à gauche, 0.5 pour le centrer et 1.0 pour un alignement à
## droite.
define gui.dialogue_text_xalign = 0.0


## Boutons #####################################################################
##
## Ces variables, ainsi que les fichiers d’image dans gui/button, contrôlent la
## façon d’afficher les boutons et leur aspect.

## La largeur et la hauteur d’un bouton en pixels. Si aucune valeur n’est
## renseignée (None), Ren’Py calcule la taille.
define gui.button_width = None
define gui.button_height = None

## Les bordures de chaque côté du bouton dans l’ordre suivant gauche, haut,
## droit, bas.
define gui.button_borders = Borders(8, 8, 8, 8)

## Si « True » (vrai), l’image d’arrière plan sera en mosaïque, si
## « False »(faux), elle sera mise à l’échelle.
define gui.button_tile = False

## La police utilisée par le bouton.
define gui.button_text_font = gui.interface_text_font

## La taille du texte utilisée pour le bouton.
define gui.button_text_size = gui.interface_text_size

## La couleur du texte des boutons dans différents états.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## L'alignement horizontal du texte des boutons. (0.0 est à gauche, 0.5 est au
## centre, 1.0 est à droite).
define gui.button_text_xalign = 0.0


## Ces variables surchargent les paramètres par défaut pour différents types de
## boutons. Veuillez consulter la documentation de l’interface de jeu (GUI) pour
## les types de boutons disponibles et leurs usages.
##
## Ces personnalisations sont utilisées par l’interface par défaut :

define gui.radio_button_borders = Borders(36, 8, 8, 8)

define gui.check_button_borders = Borders(36, 8, 8, 8)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(20, 8, 20, 8)

define gui.quick_button_borders = Borders(20, 8, 20, 0)
define gui.quick_button_text_size = 28
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Vous pouvez également ajouter vos propres personnalisations en ajoutant des
## variables correctement nommées. Par exemple, vous pouvez décommanter la ligne
## suivante pour personnaliser la largeur du bouton de navigation.

# define gui.navigation_button_width = 250


## Boutons pour les choix ######################################################
##
## Les boutons pour les choix (Choice buttons) sont utilisés dans le jeu pour
## permettre au joueur de choisir telle ou telle action, tel ou tel dialogue.

define gui.choice_button_width = 1580
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(200, 10, 200, 10)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## Boutons des emplacements de fichiers. #######################################
##
## Un bouton d’emplacement de fichier est un type spécial de bouton. Il contient
## une vignette et un texte décrivant le contenu de la sauvegarde présente dans
## l’emplacement. Un emplacement de sauvegarde utilise une image dans gui/
## button, comme les autres types de bouton.

## Le bouton d’emplacement de sauvegarde.
define gui.slot_button_width = 552
define gui.slot_button_height = 412
define gui.slot_button_borders = Borders(20, 20, 20, 20)
define gui.slot_button_text_size = 28
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## La largeur et la hauteur des vignettes de sauvegarde utilisée pour les
## emplacements de sauvegarde.
define config.thumbnail_width = 512
define config.thumbnail_height = 288

## Le nombre de colonnes et de lignes pour la grille des emplacements de
## sauvegarde.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positionnement et espacement ################################################
##
## Ces variables contrôlent l’espacement et le positionnement des différents
## éléments de l’interface utilisateur.

## La position sur le côté gauche des boutons de navigation, relatif au côté
## gauche de l'écran.
define gui.navigation_xpos = 80

## La position vertical du l’indicateur de saut des dialogues.
define gui.skip_ypos = 20

## La position verticale de la zone de notification.
define gui.notify_ypos = 90

## L’espacement entre les différents choix du menu.
define gui.choice_spacing = 44

## Boutons dans la section de navigation du menu principal et du menu de jeu.
define gui.navigation_spacing = 8

## Contrôle l’espacement entre les préférences.
define gui.pref_spacing = 20

## Contrôle l’espacements entre les boutons de préférences.
define gui.pref_button_spacing = 0

## L’espacement entre les boutons de page.
define gui.page_spacing = 0

## L’espacement entre les emplacements de sauvegarde.
define gui.slot_spacing = 20

## La position du texte du menu principal.
define gui.main_menu_text_xalign = 1.0


## Cadres ######################################################################
##
## Ces variables contrôlent le look des cadres qui peuvent contenir les
## composants de l’interface utilisateur quand un overlay ou une fenêtre ne sont
## pas présents.

## Frames génériques.
define gui.frame_borders = Borders(8, 8, 8, 8)

## Le cadre qui est utilisé par les écrans de confirmation.
define gui.confirm_frame_borders = Borders(80, 80, 80, 80)

## Le cadre qui est utilisé par l’écran de saut des dialogues.
define gui.skip_frame_borders = Borders(32, 10, 100, 10)

## Le cadre qui est utilisé par la zone de notification.
define gui.notify_frame_borders = Borders(32, 10, 80, 10)

## Est-ce que les arrière-plans des cadres doivent être en mosaïque ?
define gui.frame_tile = False


## Barres, ascenseurs et curseurs ##############################################
##
## Ceux-ci contrôlent le look et la taille des barres, des ascenseurs et des
## curseurs.
##
## Le GUI par défaut utilise uniquement des sliders et des barres de scrolling
## verticales. Toutes les autres barres ne sont utilisées que dans des screens
## écrits par l'utilisateur.

## La hauteur des barres, des ascenseurs et des curseurs horizontaux. La largeur
## des barres, des ascenseurs et des curseurs verticaux.
define gui.bar_size = 50
define gui.scrollbar_size = 24
define gui.slider_size = 50

## « True » (Vrai)  si les images de barres doivent être en mosaïques.
## « False »(Faux) si elles doivent être mise à l'échelle (étirement).
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Bordures horizontales.
define gui.bar_borders = Borders(8, 8, 8, 8)
define gui.scrollbar_borders = Borders(8, 8, 8, 8)
define gui.slider_borders = Borders(8, 8, 8, 8)

## Bordures verticales.
define gui.vbar_borders = Borders(8, 8, 8, 8)
define gui.vscrollbar_borders = Borders(8, 8, 8, 8)
define gui.vslider_borders = Borders(8, 8, 8, 8)

## Que faire avec les ascenseurs non utilisables dans le GUI ? « hide » les
## cache tandis que « None » les affiche.
define gui.unscrollable = "hide"


## Historique ##################################################################
##
## L’écran de l’historique affiche les dialogues que le joueur vient de lire.

## Le nombre de blocs que l’historique de dialogue Ren’Py va conserver.
define config.history_length = 250

## La hauteur de l’écran historique ou « None » pour calculer la hauteur au prix
## d’une légère perte de performance.
define gui.history_height = 280

## La position, largeur et alignement du label donnant le nom du personnage en
## train de parler.
define gui.history_name_xpos = 310
define gui.history_name_ypos = 0
define gui.history_name_width = 310
define gui.history_name_xalign = 1.0

## La position, largeur et alignement de la zone de dialogue.
define gui.history_text_xpos = 340
define gui.history_text_ypos = 4
define gui.history_text_width = 1480
define gui.history_text_xalign = 0.0


## Mode NVL ####################################################################
##
## L’écran du mode NVL affiche les dialogues prononcés par les personnages eux-
## mêmes en mode NVL.

## Les bordures de l’arrière-plan de la fenêtre en mode NVL.
define gui.nvl_borders = Borders(0, 20, 0, 40)

## Le nombre maximum d'entrées en mode NVL que Ren'Py affichera. Quand plus
## d'entrées sont affichées, les plus anciennes seront retirées.
define gui.nvl_list_length = 6

## La hauteur d’une entrée en mode NVL. Initialisez-la à « None » pour que la
## hauteur des entrées s’ajuste automatiquement.
define gui.nvl_height = 230

## L’espacement entre les entrées en mode NVL quand gui.nvl_height est à
## « None » et entre les entrées en mode NVL et le menu en mode NVL.
define gui.nvl_spacing = 20

## La position, largeur et alignement du label donnant le nom du personnage en
## train de parler.
define gui.nvl_name_xpos = 860
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 300
define gui.nvl_name_xalign = 1.0

## La position, largeur et alignement de la zone de dialogue.
define gui.nvl_text_xpos = 900
define gui.nvl_text_ypos = 16
define gui.nvl_text_width = 1180
define gui.nvl_text_xalign = 0.0

## La position, profondeur et l’alignement du text nvl_tought (Le texte prononcé
## par le personnage nvl_narrator).
define gui.nvl_thought_xpos = 480
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1560
define gui.nvl_thought_xalign = 0.0

## La position de nvl menu_buttons.
define gui.nvl_button_xpos = 900
define gui.nvl_button_xalign = 0.0

## Localisation (traduction et adaptation aux langues et cultures) #############

## Ceci contrôle où un saut de ligne est autorisé. La valeur par défaut convient
## à la plupart des langues. Une liste des valeurs disponible peut être trouvée
## sur https://www.renpy.org/doc/html/style_properties.html#style-property-
## language

define gui.language = "unicode"


################################################################################
## Appareils mobiles
################################################################################

init python:

    ## Ceci augmente la taille des boutons d’accès rapide pour les rendre plus
    ## accessibles sur les tablettes et les téléphones.
    if renpy.variant("touch"):

        gui.quick_button_borders = Borders(80, 28, 80, 0)

    ## Ceci change la taille et l’espacement de différents élements de la GUI
    ## pour s’assurer qu’ils soient visibles sur les téléphones.
    if renpy.variant("small"):

        ## Tailles des polices.
        gui.text_size = 60
        gui.name_text_size = 72
        gui.notify_text_size = 50
        gui.interface_text_size = 60
        gui.button_text_size = 60
        gui.label_text_size = 68

        ## Ajuste la position de la zone de texte.
        gui.textbox_height = 480
        gui.name_xpos = 160
        gui.dialogue_xpos = 180
        gui.dialogue_width = 2200

        ## Changer la taille et l'espacement de diverses choses.
        gui.slider_size = 72

        gui.choice_button_width = 2480
        gui.choice_button_text_size = 60

        gui.navigation_spacing = 40
        gui.pref_button_spacing = 20

        gui.history_height = 380
        gui.history_text_width = 1380

        gui.quick_button_text_size = 40

        ## Remplit le canvas du bouton.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Mode NVL.
        gui.nvl_height = 340

        gui.nvl_name_width = 610
        gui.nvl_name_xpos = 650

        gui.nvl_text_width = 1830
        gui.nvl_text_xpos = 690
        gui.nvl_text_ypos = 10

        gui.nvl_thought_width = 2480
        gui.nvl_thought_xpos = 40

        gui.nvl_button_width = 2480
        gui.nvl_button_xpos = 40
