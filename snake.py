import pygame
import random
import sys

menu = True

#variable couleur
bleu = (0, 0, 255)
noir = (0, 0, 0)
blanc = (255, 255, 255)
rouge = (222, 41, 22)
vert = (87, 213, 59)
violet = (108, 2, 119)

snake_largeur = 10

#variable taille fenetre
largeur_fenetre = 500
hauteur_fenetre = 400

#variable changement de direction
horizontal_changement = 0
vertical_changement = 0

horizontal_historique = 0
vertical_historique = 0

#variable temps pour vitesse du snake
temps = pygame.time.Clock()
vitesse = 15

#variable de la fonte du score
score_style_font = pygame.font.SysFont('Arial', 20)

#création de la fenetre de jeu
pygame.init()
#taille de la fenetre de jeu
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.update()
#nom de la fenetre de jeu
pygame.display.set_caption('Snake')

#fonction pour mettre le meilleur score dans le fichier score
def meilleur_score(score):
    fichier = open('score.txt', 'r')
    personal_best = int(fichier.read())
    fichier.close()
    if personal_best < int(score) :
        personal_best = score
    fichier = open('score.txt', 'w')
    fichier.write(str(personal_best))
    fichier.close()

#fonction pour prendre le score dans le fichier score
def affichage_meilleur_score():
    fichier = open('score.txt', 'r')
    score = fichier.read()
    fichier.close()
    return score

#focntion position du snake quand il grandit
def snake(snake_liste):
    for x in snake_liste:
        pygame.draw.rect(fenetre, violet, [x[0], x[1], snake_largeur, snake_largeur])

#fonction afficher socre et meilleur score sur la fenetre de jeu
def score_actuelle(score):
    score_affichage = score_style_font.render('score: '+ str(score), True, noir)
    fenetre.blit(score_affichage, [0,1])

    meilleur_score(score)
    pb_affichage = score_style_font.render('pb: ' + affichage_meilleur_score(), True, noir)
    fenetre.blit(pb_affichage, [420, 1])


#fonction affichage message
def message(msg, couleur, x, y, taille_police):
    # variable style écriture
    font_style = pygame.font.SysFont('arial', taille_police)
    #affichage du message sur la fenetre de jeu
    mess = font_style.render(msg, True, couleur)
    #postion du message sur la fenetre de jeu
    fenetre.blit(mess, [x, y])


#foncion boucle de jeu
def bouclejeu():
    global menu
    global vertical_historique
    global horizontal_historique
    global vitesse
    perdu = False
    jeu_ferme = False

    #position de depart du serpent
    horizontal = largeur_fenetre/2
    vertical  = hauteur_fenetre/2

    #variable changement de direction
    horizontal_changement = 0
    vertical_changement = 0

    #taille du serpent
    snake_liste = []
    snake_longeur = 1

    #position des points sur la fenetre de jeu
    point_horizontal = round(random.randrange(0, largeur_fenetre - snake_largeur) / 10)*10
    point_vertical = round(random.randrange(0, hauteur_fenetre - snake_largeur) / 10)*10

    #boucle de jeu
    while not jeu_ferme:
        #boucle menu
        while menu:
            fenetre.fill(vert)
            message("Bienvenue", noir, 160, 50, 40)
            message("Meilleur score : " + affichage_meilleur_score(), noir, 100, 130, 40)
            message("Jouer appuyer sur J", noir, 150, 175, 25)
            message("quitter appuyer sur Q", rouge, 140, 300, 25)
            pygame.display.update()

            for evenement in pygame.event.get():
                # condition pour femrer la fenetre avec le bouton fermer
                if evenement.type== pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_q:
                        menu = False
                        jeu_ferme = True
                        perdu = False

                    if evenement.key == pygame.K_j:
                        menu = False
                        bouclejeu()

        #boucle perdu menu
        while perdu:
            message("Perdu !!", rouge,190, 80, 40)
            message("score : "+str(snake_longeur-1), rouge,180,120,40)
            message("Meilleur score : " + affichage_meilleur_score(), rouge, 110, 160, 40)
            message("rejouer appuyer sur R", noir,160, 210, 20)
            message("quitter appuyer sur Q", noir,163, 235, 20)
            message("menu appuyer sur M", noir, 165, 260, 20)
            pygame.display.update()

            for evenement in pygame.event.get():
                # condition pour femrer la fenetre avec le bouton fermer
                if evenement.type== pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_q:
                        jeu_ferme = True
                        perdu = False
                    if evenement.key == pygame.K_r:
                        bouclejeu()
                    if evenement.key == pygame.K_m:
                        menu = True
                        bouclejeu()

        #boucle jeu en cours
        for evenement in pygame.event.get():
            #condition pour femrer la fenetre avec le bouton fermer
            if evenement.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evenement.type == pygame.QUIT:
                perdu = True
            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_LEFT:
                    horizontal_changement = -snake_largeur
                    vertical_changement = 0
                    vertical_historique = 0
                    if horizontal_historique == 1 and vertical_historique == 0:
                        horizontal_changement = snake_largeur

                elif evenement.key == pygame.K_RIGHT:
                    horizontal_changement = snake_largeur
                    vertical_changement = 0
                    vertical_historique = 0
                    if horizontal_historique == -1 and vertical_historique == 0:
                        horizontal_changement = -snake_largeur

                elif evenement.key == pygame.K_UP:
                    vertical_changement = -snake_largeur
                    horizontal_changement = 0
                    horizontal_historique=0
                    if vertical_historique == 1 and horizontal_historique == 0:
                        vertical_changement = snake_largeur

                elif evenement.key == pygame.K_DOWN:
                    horizontal_changement = 0
                    vertical_changement = snake_largeur
                    horizontal_historique = 0
                    if vertical_historique == -1 and horizontal_historique == 0:
                        vertical_changement = -snake_largeur

        #si le serpent sorts de la fenetre de jeu
        if horizontal >= largeur_fenetre or horizontal < 0 or vertical >= hauteur_fenetre or vertical < 0:
            perdu = True
            meilleur_score(snake_longeur-1)
        #condition pour ne pas allé dans le sens opposé et perdre la partie
        if horizontal_changement == -snake_largeur:
            horizontal_historique = -1
        if horizontal_changement == snake_largeur:
            horizontal_historique = 1
        if vertical_changement == -snake_largeur:
            vertical_historique = -1
        if vertical_changement == snake_largeur:
            vertical_historique=1

        #variable changement de direction
        horizontal += horizontal_changement
        vertical += vertical_changement
        fenetre.fill(vert)
        #oon actualise la postion du serpent sur la fenetre
        pygame.draw.rect(fenetre, rouge, [point_horizontal, point_vertical, 10, 10])

        #condition si la tete du serpent touche son corps partie perdu
        snake_tete = []
        snake_tete.append(horizontal)
        snake_tete.append(vertical)
        snake_liste.append(snake_tete)
        if len(snake_liste) > snake_longeur:
            del snake_liste[0]

        for x in snake_liste[:-1]:
            if x == snake_tete:
                perdu = True
                meilleur_score(snake_longeur-1)

        #fonction actualisation de la postion et taille du snake
        snake(snake_liste)

        #fonction affichage score
        score_actuelle(snake_longeur-1)

        #si une pomme est mangé, elle est repositionner a un endroit aléatoire
        if horizontal == point_horizontal and vertical == point_vertical:
            point_horizontal = round(random.randrange(0, largeur_fenetre - snake_largeur) / 10) * 10
            point_vertical = round(random.randrange(0, hauteur_fenetre - snake_largeur) / 10) * 10
            snake_longeur +=1

        #vitesse du snake
        temps.tick(vitesse)
        # update affichage de la fenetre
        pygame.display.update()
    pygame.quit()
    quit()

bouclejeu()
