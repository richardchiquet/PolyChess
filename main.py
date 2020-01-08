"""

"""


from chessboard import Echiquier
from ia import IA, Mouvement
import copy

# =============================================================================
# Gestion de l'interface - boucle du moteur
# =============================================================================


echiquier = Echiquier()
#echiquier.afficher()

<<<<<<< HEAD
demande_au_joueur = "Que voulez-vous faire ?"
liste_aide_joueur = {1 : (
                          "Pour jouer", 
                          [
                           "jouer [coordonnées départ] [coordonnées arrivée]", 
                           "[coordonnées départ] [coordonnées arrivée]"
                           ]
                          ), 
                     2 : (
                          "Pour connaitre les coups possibles", 
                          ["coups"]
                          ),
                     3 : (
                          "Pour connaitre la liste des coups possibles d'une piece", 
                          ["piece"]
                         ),
                     4 : (
                          "Pour afficher l'échiquier", 
                          ["afficher"]
                          ),
                     5 : (
                          "Pour afficher l'échiquier avec les coups possibles d'une piece", 
                          ["afficher [coordonnées]"]
                         )
                     }

aide_joueur = "\n".join(
                        [str(numero) 
                        + " - " 
                        + liste_aide_joueur[numero][0] 
                        + ", entrez : " 
                        + " ou ".join(liste_aide_joueur[numero][1]) 
                        + " ou " 
                        + str(numero) 
                        + [" [coordonnées départ] [coordonnées arrivée]" if numero == 1 else ""][0] for numero in liste_aide_joueur.keys()]
                       ) + "\n\n"

str_ne_plus_afficher_laide = "Pour ne plus afficher l'aide, entrez : fin aide\n\n"
str_afficher_laide = "Pour afficher l'aide, entrez : aide\n\n"
ne_plus_afficher_laide = False

#for numero_du_tour in range(50):
#    
#    #-- le joueur joue --
#     
#    #qu'est-ce qu'il veut faire ?
#    while True:
#        
#        if ne_plus_afficher_laide:
#            entree_joueur = input(str_afficher_laide)
#        else:
#            entree_joueur = input(aide_joueur + str_ne_plus_afficher_laide)
#        
#        #ne plus afficher l'aide
#        if entree_joueur == 'fin aide':
#            ne_plus_afficher_laide = True
##        elif entree_
#        
#        # 1 - si il veut jouer
#        if entree_joueur[:-6] in [element[:-43] for element in liste_aide_joueur[1][1]] + ['1']:
#            break
#        
#        # 2 - "Pour connaitre les coups possibles"
#        elif entree_joueur in liste_aide_joueur[2][1] + ['2']:
#            pass
#        
#        # 3 - "Pour connaitre la liste des coups possibles d'une piece"
#        elif entree_joueur in liste_aide_joueur[3][1] + ['3']:
#            pass
#        
#        # 4 - "Pour afficher l'échiquier"
#        elif entree_joueur in liste_aide_joueur[4][1] + ['4']:
#            pass
#        
#        # 5 - "Pour afficher l'échiquier avec les coups possibles d'une piece"
#        elif entree_joueur in liste_aide_joueur[5][1] + ['5']:
#            pass
#    
#    break
#   
#
    
    #verification de fin de partie
    
    
    #-- l'IA joue --
    #déplacement d'une piece
    
    
    #vérification de la fin de partie
=======
>>>>>>> 1c82805bc3d185cdcd6ecb6093f744855d076ad7

#==============================================================================
# PvP ou PvC
#==============================================================================






modeDeJeu = input("Voulez vous jouez contre L'ordinateur (entrer : JcIA) ou contre un joueur (entrer : JcJ) ?\n\n")
if modeDeJeu == "PvP":
    jouerEnModeJcJ()

elif modeDeJeu == "PvC":
    jouerEnModeJcIA()
        
    
    
    
    
    

demande_au_joueur = "Que voulez-vous faire ?"


def jouerEnModeJcIA() :
    
    liste_aide_joueur = {1 : (
                              "Pour jouer", 
                              [
                               "jouer [coordonnées départ] [coordonnées arrivée]", 
                               "[coordonnées départ] [coordonnées arrivée]"
                               ]
                              ), 
                         2 : (
                              "Pour connaitre les coups possibles", 
                              ["coups"]
                              ),
                         3 : (
                              "Pour connaitre la liste des coups possibles d'une piece", 
                              ["piece"]
                             ),
                         4 : (
                              "Pour afficher l'échiquier", 
                              ["afficher"]
                              ),
                         5 : (
                              "Pour afficher l'échiquier avec les coups possibles d'une piece", 
                              ["afficher [coordonnées]"]
                             )
                         }
    
    aide_joueur = "\n".join(
                            [str(numero) 
                            + " - " 
                            + liste_aide_joueur[numero][0] 
                            + ", entrez : " 
                            + " ou ".join(liste_aide_joueur[numero][1]) 
                            + " ou " 
                            + str(numero) 
                            + [" [coordonnées départ] [coordonnées arrivée]" if numero == 1 else ""][0] for numero in liste_aide_joueur.keys()]
                           ) + "\n\n"
    
    str_ne_plus_afficher_laide = "Pour ne plus afficher l'aide, entrez : fin aide\n\n"
    str_afficher_laide = "Pour afficher l'aide, entrez : aide\n\n"
    ne_plus_afficher_laide = False

    for numero_du_tour in range(50):
        
        #-- le joueur joue --
         
        #qu'est-ce qu'il veut faire ?
        while True:
            
            if ne_plus_afficher_laide:
                entree_joueur = input(str_afficher_laide)
            else:
                entree_joueur = input(aide_joueur + str_ne_plus_afficher_laide)
            
            #ne plus afficher l'aide
            if entree_joueur == 'fin aide':
                ne_plus_afficher_laide = True
    #        elif entree_
            
            # 1 - si il veut jouer
            if entree_joueur[:-6] in [element[:-43] for element in liste_aide_joueur[1][1]] + ['1']:
                break
            
            # 2 - "Pour connaitre les coups possibles"
            elif entree_joueur in liste_aide_joueur[2][1] + ['2']:
                pass
            
            # 3 - "Pour connaitre la liste des coups possibles d'une piece"
            elif entree_joueur in liste_aide_joueur[3][1] + ['3']:
                pass
            
            # 4 - "Pour afficher l'échiquier"
            elif entree_joueur in liste_aide_joueur[4][1] + ['4']:
                pass
            
            # 5 - "Pour afficher l'échiquier avec les coups possibles d'une piece"
            elif entree_joueur in liste_aide_joueur[5][1] + ['5']:
                pass
        
        break
       
        
    
    #verification de fin de partie
    
    
    #-- l'IA joue --
    #déplacement d'une piece
    
    
    #vérification de la fin de partie
    

def jouerEnModeJcJ():
    echiquier.afficher()
       
    liste_aide_joueur = {1 : (
                              "Pour jouer", 
                              [
                               "jouer [coordonnées départ] [coordonnées arrivée]", 
                               "[coordonnées départ] [coordonnées arrivée]"
                               ]
                              ), 
                         2 : (
                              "Pour connaitre les coups possibles", 
                              ["coups"]
                              ),
                         3 : (
                              "Pour connaitre la liste des coups possibles d'une piece", 
                              ["piece"]
                             ),
                         4 : (
                              "Pour afficher l'échiquier", 
                              ["afficher"]
                              ),
                         5 : (
                              "Pour afficher l'échiquier avec les coups possibles d'une piece", 
                              ["afficher [coordonnées]"]
                             )
                         }
    
    aide_joueur = "\n".join(
                            [str(numero) 
                            + " - " 
                            + liste_aide_joueur[numero][0] 
                            + ", entrez : " 
                            + " ou ".join(liste_aide_joueur[numero][1]) 
                            + " ou " 
                            + str(numero) 
                            + [" [coordonnées départ] [coordonnées arrivée]" if numero == 1 else ""][0] for numero in liste_aide_joueur.keys()]
                           ) + "\n\n"
    
    str_ne_plus_afficher_laide = "Pour ne plus afficher l'aide, entrez : fin aide\n\n"
    str_afficher_laide = "Pour afficher l'aide, entrez : aide\n\n"
    ne_plus_afficher_laide = False

    for numero_du_tour in range(50):
        
        #-- le joueur joue --
         
        #qu'est-ce qu'il veut faire ?
        print("C'est au joueur blanc de jouer" )
        while True:
            
            if ne_plus_afficher_laide:
                entree_joueur = input(str_afficher_laide)
            else:
                entree_joueur = input(aide_joueur + str_ne_plus_afficher_laide)
            
            #ne plus afficher l'aide
            if entree_joueur == 'fin aide':
                ne_plus_afficher_laide = True
    #        elif entree_
            
            # 1 - si il veut jouer
            if entree_joueur[:-6] in [element[:-43] for element in liste_aide_joueur[1][1]] + ['1']:
                break
            
            # 2 - "Pour connaitre les coups possibles"
            elif entree_joueur in liste_aide_joueur[2][1] + ['2']:
                for piece in echiquier.emplacmentPiecesblanche():
                    echiquier.listeCoupsPossiblesFormatCase(piece)
            
            # 3 - "Pour connaitre la liste des coups possibles d'une piece"
            elif entree_joueur in liste_aide_joueur[3][1] + ['3']:
                pass
            
            # 4 - "Pour afficher l'échiquier"
            elif entree_joueur in liste_aide_joueur[4][1] + ['4']:
                pass
            
            # 5 - "Pour afficher l'échiquier avec les coups possibles d'une piece"
            elif entree_joueur in liste_aide_joueur[5][1] + ['5']:
                pass
        
        echiquier.afficher()
        
        if echiquier.isEchecEtMat():
            print("Les blancs ont gagné" )
            break
        
            
        print("C'est au joueur noir de jouer" )
        while True:
            
            if ne_plus_afficher_laide:
                entree_joueur = input(str_afficher_laide)
            else:
                entree_joueur = input(aide_joueur + str_ne_plus_afficher_laide)
            
            #ne plus afficher l'aide
            if entree_joueur == 'fin aide':
                ne_plus_afficher_laide = True
    #        elif entree_
            
            # 1 - si il veut jouer
            if entree_joueur[:-6] in [element[:-43] for element in liste_aide_joueur[1][1]] + ['1']:
                break
            
            # 2 - "Pour connaitre les coups possibles"
            elif entree_joueur in liste_aide_joueur[2][1] + ['2']:
                pass
            
            # 3 - "Pour connaitre la liste des coups possibles d'une piece"
            elif entree_joueur in liste_aide_joueur[3][1] + ['3']:
                pass
            
            # 4 - "Pour afficher l'échiquier"
            elif entree_joueur in liste_aide_joueur[4][1] + ['4']:
                pass
            
            # 5 - "Pour afficher l'échiquier avec les coups possibles d'une piece"
            elif entree_joueur in liste_aide_joueur[5][1] + ['5']:
                echiquier.afficherCoupsPossibles(entree_joueur)
        
        echiquier.afficher()    
            
        if echiquier.isEchecEtMat():
            print("Les noirs ont gagné" )
            break
        
        
        
#        while echiquier == echiquiercopy:
            
            
            
            
            
            
            
            
    


#==============================================================================
# Appel de l'échiquier
#==============================================================================

echiquier = Echiquier()
#
#print(echiquier.listeCoupsPossiblesFormatCase('C7'))
#print(echiquier.listeCoupsPossiblesFormatCase('B7'))
#
##echiquier.afficherCoupsPossibles('D7')
#
#echiquier.deplacerPiece('A2', 'A3')
#echiquier.afficher()
#
#echiquier.deplacerPiece('C2', 'E4')
#echiquier.afficher() 
#
#echiquier.afficherCoupsPossibles('E4')
#
##print(echiquier.listeDeplacementsPossibles('A6'))
#
##print(echiquier.isEchecEtMat())
##print(echiquier.couleurEchecEtMat())



#==============================================================================
# Appel de l'IA
#==============================================================================


couleur = 'noir'
#
#
ia = IA(echiquier, 'noir')

#print(ia.meilleurMouvement(echiquier, couleur))

#possibilites = ia.nMeilleursMouvementsPoints(5)
possibilites = ia.arbre_nFils_pProfondeur()








#while not echiquier.isEchecEtMat():
#    
#    #au joueur blanc de déplacer une pièce
#    
#    #à l'IA de jouer
#
#    pass

#une fois la boucle finie


# =============================================================================
# Fonctions du main
# =============================================================================


#
#
#Fait jusqu'à présent (liste pas a jour) :
#    - classe Echiquier et classe Piece
#    - définition des pieces
#    - initialisation de l'échiquier
#    - gestion des déplacements dans l'échiquier
#    - vérification de l'échec et mat
#    
#À faire bientôt :
#    - déplacements possibles (fait pour pion dans Piece() mais pas les autres 
#           et ensuite compléter listeDeplacementsPossibles dans Echiquier())
#    - affichage des déplacements possibles
#

