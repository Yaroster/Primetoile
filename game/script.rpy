define n = Character("Narrateur", color="#ffffff")
define a = Character('Adriorpa', color="#c8ffc8")
define h = Character('Harlund', color="#d3d3d3")

# Le jeu commence ici
label start:

    n "Vous sentez la brise matinale vous secouer la tête"

    show windhelm_boats
    with dissolve

    n "La houle d'une charette vous cajole, mettant a rude épreuve votre devoir de réveil"
    n "Soudainement, vous entendez la voix roque de Commandant de bord..."

    scene windhelm_boats_blur
    show harlund with dissolve

    h "Hors de mon bateau les dunmer !"
    hide harlund with dissolve
    show harlund at left with dissolve
    show adriorpa at right with dissolve
    a "Q-quoi déjà ?"
    h "Houste je dis !"

    menu:
        n "Que voulez-vous faire ?"
        "Le menacer":
            jump mechant
        "Quitter le bateau":
            jump normal

    label mechant:
        a "Je vais vous refaire le visage l'ami"
        h "Comment dunmer ? Veux-tu retourner à l'enfer d'où tu viens ?"
        h "N'oublie pas à qui Solsteim appartient vraiment, si ce n'était pour le Haut-Jarl, les vicieux serpents que vous êtes auraient étés renvoyés chez eux"
        h "Maudits impériaux..."
        hide harlund with dissolve
        show adriorpa with moveoutleft
        
        n "Trop fatigué pour débattre, vous décidez de quitter le navire"

        jump suite_1

    label normal:
        a "Bien, passez une bonne journée"
        n "Malgré le dégoût de ne pas avoir lancé un trait au Commandant Harlund, votre fatigue vous empêche de répliquer et vous vous dirigez petit à petit hors du quai"

    label suite_1:
        n "... puis vous vous dirigez petit à petit vers les portes de la ville."
    return
