# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define k = Character('Kūro', color="#c8ffc8")
define e = Character('Elō', color="#c8ffc8")
define y = Character('', color="#5c5c5c")


# Le jeu commence ici
label start:

    y "{i}Cuius est solum, eius est usque ad coelum et ad inferos.{/i}"
    pause(1.0)
    # play music "crack.ogg"
    # play music "panic.ogg"
    # show bg craquelement with dissolve
    y "Une lumière opaline éclipse la Terre..."
    show image "space1.png" with fade
    y "Et l'astre fraternel balaye de sa poudre les habitants de notre planète..."
    # effet flash
    # <vidéo du Craquèlement>
    pause(1.0)
    y "C'est le Craquèlement."
    # play music "panic_sad.ogg"
    # effect flash
    pause(1.0)
    y "Sous la poudre de lune, l'humanité survit...\nDans de vastes souterrains nouvellement formés"
    # show image souterrains avec nappes phreatiques et plantes
    y "Les nappes phréatiques et les épilithes de ces nouveaux environnements permettent à des sociétés nouvelles de naître"
    #
    y "En vingt-mille ans à peine, des villes entières sont érigées sous-terre, certaines interconnectées par de larges canaux rocheux"
    return
