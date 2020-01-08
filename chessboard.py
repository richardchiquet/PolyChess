"""


"""

from functools import reduce
from rules import Piece


class Echiquier:
        
    
    def __init__(self):
        
        self.positions = \
            [Piece('Tour', 'noir'), 
             Piece('Cavalier', 'noir'), 
             Piece('Fou','noir'),
             Piece('Dame', 'noir'), 
             Piece('Roi','noir'),
             Piece('Fou', 'noir'), 
             Piece('Cavalier', 'noir'), 
             Piece('Tour', 'noir')] + \
                \
            [Piece('Pion', 'noir')] * 8 + \
                \
            [Piece()] * 8 * 4 + \
                \
            [Piece('Pion', 'blanc')] * 8 + \
                \
            [Piece('Tour', 'blanc'), 
             Piece('Cavalier', 'blanc'), 
             Piece('Fou','blanc'),
             Piece('Dame', 'blanc'), 
             Piece('Roi', 'blanc'),
             Piece('Fou', 'blanc'),
             Piece('Cavalier', 'blanc'), 
             Piece('Tour', 'blanc')]
            
#        self.positions = \
#            [Piece()] * 8 +  \
#                \
#            [Piece('Tour', 'noir'), Piece('Cavalier', 'noir'), 
#             Piece('Fou','noir'),
#             Piece('Dame', 'noir'), Piece('Roi','noir'),
#             Piece('Fou', 'noir'), 
#             Piece('Cavalier', 'noir'), Piece('Tour', 'noir')] + \
#                \
#            [Piece()] * 8 * 4 + \
#                \
#            [Piece('Tour', 'blanc'), Piece('Cavalier', 'blanc'), 
#             Piece('Fou','blanc'),
#             Piece('Dame', 'blanc'), Piece('Roi', 'blanc'),
#             Piece('Fou', 'blanc'),
#             Piece('Cavalier', 'blanc'), Piece('Tour', 'blanc')] + \
#                \
#            [Piece()] * 8
#            
    def get_piece(self, index):
        return self.positions[index]
                 
        
#==============================================================================
# Construction de l'échiquier
#==============================================================================
    
    def coordonnees():
        return [lettre + str(chiffre) for chiffre in range(1,9) for lettre in ['A','B','C','D','E','F','G','H']]
    
    
#==============================================================================
# Affichage
#==============================================================================
    
    
    def afficher(self):
    
        lettres = reduce(lambda ele1, ele2 : ele1 + ele2, ["  " + element + "  " for element in ['A','B','C','D','E','F','G','H']])
        interlignes = "    " + reduce(lambda ele1, ele2 : ele1 + ele2, ["-" * 4 + " "] * 8)
        
        print(" " * 60 + "/")
        print(" ".join(["—","-"] * 15))        
        print(" " * 60 + "\\")
        
        print("   " + lettres)
        print(interlignes)
        
        numLigne = 8
        indexPosition = 0
        
        for piece in self.positions:
            
#            print(ligne)
            
            if indexPosition % 8 == 0:
                print(str(numLigne), end = "  |")
            
            if piece.nom != piece.pieceVide:
                
                print(" " + piece.nomAffichage + " ", end = "|")
        
            else:
                
                print("    ", end = "|")
            
            
            if (indexPosition + 1) % 8 == 0:
                
                print("  " + str(numLigne))
            
                print(interlignes)
            
                numLigne -= 1
                
            indexPosition += 1
            
        print("   " + lettres)
    
        
    
#         A    B    C    D    E    F    G    H  
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    8  | Tn | Cn | Fn | Dn | Rn | Fn | Cn | Tn |  8
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    7  | in | in | in | in | in | in | in | in |  7
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    6  |    |    |    |    |    |    |    |    |  6
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    5  |    |    |    |    |    |    |    |    |  5
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    4  |    |    |    |    |    |    |    |    |  4
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    3  |    |    |    |    |    |    |    |    |  3
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    2  | ib | ib | ib | ib | ib | ib | ib | ib |  2
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#    1  | Tb | Cb | Fb | Db | Rb | Fb | Cb | Tb |  1
#        ---- ---- ---- ---- ---- ---- ---- ---- 
#         A    B    C    D    E    F    G    H  
    




    def afficherCoupsPossibles(self, nomCase):
    
        lettres = reduce(lambda ele1, ele2 : ele1 + ele2, ["  " + element + "  " for element in ['A','B','C','D','E','F','G','H']])
        interlignes = "    " + reduce(lambda ele1, ele2 : ele1 + ele2, ["-" * 4 + " "] * 8)
        
        coupsPossibles = self.listeCoupsPossibles(nomCase)
        
        couleur = self.positions[self.nomCaseToIndex(nomCase)].couleur
        couleurOpposee = 'noir' if couleur == 'blanc' else 'blanc'
        
        print(" " * 60 + "/")
        print(" ".join(["—","-"] * 15))        
        print(" " * 60 + "\\")

        print("   " + lettres)
        print(interlignes)
        
        numLigne = 8
        indexPosition = 0
        
        for piece in self.positions:
            
#            print(ligne)
            
            if indexPosition % 8 == 0:
                print(str(numLigne), end = "  |")
                
            
            if indexPosition == self.nomCaseToIndex(nomCase):
                
                print("#" + piece.nomAffichage + "#", end = "|")
                
            elif indexPosition in coupsPossibles:
                
                if  piece.couleur == couleurOpposee:
                    
                    print("<" + piece.nomAffichage + ">", end = "|")
                
                else:
                    
                    print(" <> ", end = "|")
            
            elif piece.nom != piece.pieceVide:
                
                print(" " + piece.nomAffichage + " ", end = "|")
        
            else:
                
                print("    ", end = "|")
                
            
            
            if (indexPosition + 1) % 8 == 0:
                
                print("  " + str(numLigne))
            
                print(interlignes)
            
                numLigne -= 1
                
            indexPosition += 1
            
        print("   " + lettres)
    

 
 
    
#==============================================================================
# Déplacement
#==============================================================================
    
    def deplacerPiece(self, nomCaseDepart, nomCaseArrivee):
        
        indexDep = self.nomCaseToIndex(nomCaseDepart)
        indexArr = self.nomCaseToIndex(nomCaseArrivee)
        
        if indexArr in self.listeCoupsPossibles(nomCaseDepart):
            self.positions[indexArr] = self.positions[indexDep]
            self.positions[indexDep] = Piece()  
        
    def deplacerPieceEnIndex(self, indexDepart, indexArrivee):
        
        if indexArrivee in self.listeCoupsPossibles(self.indexToNomCase(indexDepart)):
            self.positions[indexArrivee] = self.positions[indexDepart]
            self.positions[indexDepart] = Piece()  
        
    
#==============================================================================
# Vérification déplacement dans la zone
#==============================================================================

    def listeCoupsPossibles(self, nomCase):
        
        indexCase = self.nomCaseToIndex(nomCase)
        
        return self.listeCoupsPossiblesEntreeIndex(indexCase)

    
    def listeCoupsPossiblesEntreeIndex(self, indexCase):
        
        if self.positions[indexCase].nom == self.positions[indexCase].pieceVide:
            return []
        
        if self.positions[indexCase].nom == 'Pion':
            return self.positions[indexCase].listeCoupsPossiblesPion(indexCase, self)
            
        if self.positions[indexCase].nom == 'Tour':
            return self.positions[indexCase].listeCoupsPossiblesTour(indexCase, self)
        
        if self.positions[indexCase].nom == 'Fou':
            return self.positions[indexCase].listeCoupsPossiblesFou(indexCase, self)
        
        if self.positions[indexCase].nom == 'Cavalier':
            return self.positions[indexCase].listeCoupsPossiblesCavalier(indexCase, self)
        
        if self.positions[indexCase].nom == 'Dame':
            return self.positions[indexCase].listeCoupsPossiblesDame(indexCase, self)
        
        if self.positions[indexCase].nom == 'Roi':
            return self.positions[indexCase].listeCoupsPossiblesRoi(indexCase, self)  
        

    def listeCoupsPossiblesFormatCase(self, nomCase):
        
        return [self.indexToNomCase(index) for index in self.listeCoupsPossibles(nomCase)]


    def listePiecesPouvantEtreDeplacees(self, couleur):
        
        liste = []
        
        for index in range(64):
            
            if self.positions[index].couleur == couleur:
                
                if len(self.listeCoupsPossibles(self.indexToNomCase(index))) > 0:
                    
                    liste.append(index)
        
        return liste
        

#==============================================================================
# Fin du jeu
#==============================================================================

    def isEchecEtMat(self):
        return len(list(filter(lambda piece : piece.nom == 'Roi', self.positions))) < 2
    
    
    def couleurEchecEtMat(self):
        
        if not self.isEchecEtMat():
            return None
        
        return 'blanc' if list(filter(lambda piece : piece.nom == 'Roi', self.positions))[0].couleur == 'noir' else 'noir'


#==============================================================================
# Autres fonctions
#==============================================================================
    
    def nomCaseToIndex(self, nomCase):
        
        if not type(nomCase) is str:
            return 'erreur saisie'
        
        lettres = ['A','B','C','D','E','F','G','H']
        lig, col = 8 - int(nomCase[1]), lettres.index(nomCase[0]) + 1
        
        return lig * 8 + col - 1
    
    
    def indexToNomCase(self, indexCase):
        
        return ['A','B','C','D','E','F','G','H'][indexCase % 8] + str(8 - indexCase // 8)
    
    #print("‎• or <>")
    
    def listeIndexMangeantLaPiece(self, indexPiece):
        listeIndex = []
        
        for indexDepart in self.listePiecesPouvantEtreDeplacees(self.positions[indexPiece].couleurOpposee):
            
            for indexArrivee in self.listeCoupsPossiblesEntreeIndex(indexDepart):
                
                if indexArrivee == indexPiece:
                    
                    listeIndex.append(indexDepart)
                    break
                
        
        return listeIndex

    
    def leDeplacementMangeUnePiece(self, indexArrivee):
        return self.positions[indexArrivee].couleur != self.positions[0].pieceVide
    


    def nombreDePiecesAdversesPouvantMangerLaPiece(self, index):
        return len(self.listeIndexMangeantLaPiece(index))
    
    def emplacmentPiecesBlanche(self):
        return [self.indexToNomCase(element) for element in[index for index in range(8*8-1) if self.positions[index].couleur == 'blanc']]
    
    def emplacementPiecesnoires(self):
        return [self.indexToNomCase(element) for element in[index for index in range(8*8-1) if self.positions[index].couleur == 'noir']]
    
# =============================================================================
# fonction pour les calculs de points de l'IA
# =============================================================================
    
     #moins de points si la piece peut se faire manger
    def coefficientPointsSiPeutEtreMangee(self, indexArrivee, couleur):
        
        nbPiecePouvantManger = self.nombreDePiecesAdversesPouvantMangerLaPiece(indexArrivee)
        
        #si len = 0
        if nbPiecePouvantManger == 0:
            return 1
        
        #si len = 1
        if nbPiecePouvantManger == 1:
            return 1.5
        
        #si len > 1
        if nbPiecePouvantManger > 1 :
            return 1.5 + .2 * (nbPiecePouvantManger - 1)
            
        
        
    #moins de points si elle n'a aucune piece de la meme couleur autour
    def coefficientPointsSiPieceMemeCouleurProche(self, indexArrivee, couleur):
            
        pass
    
