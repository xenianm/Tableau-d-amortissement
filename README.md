# Tableau-d-amortissement

## Consignes du TD
Écrire une fonction ```tableau_annuites (C0, r, n, periodicite, differe, mode)``` qui construit le tableau d’amortissement d’un emprunt remboursé sur années (terme échu) à un taux annuel. 

Elle doit : calculer l’annuité selon le mode choisi (annuité constante ou amortissement constant) ; pour chaque période , calculer et ranger chaque période dans une liste [t, I, M, A, C] , ajoutée à une liste tableau ;
afficher le tableau ligne par ligne, aligné, avec une ligne d’en-tête ;
retourner tableau .

## Précisions sur les arguments
periodicite : nombre de versements par an (1 pour annuel, 2 pour semestriel, 4 pour trimestriel, 12 pour mensuel). Il faudra donc adapter le
taux et le nombre de périodes en fonction de cette périodicité. Le taux sera tranformé proportionnellement à la périodicité, et le nombre de
périodes sera multiplié par la périodicité. L’argument périodicite est donc un entier strictement positif qui pourra prendre des valeurs 1, 2, 4
ou 12. Le taux d’intérêt périodique sera donc r / periodicite , et le nombre de périodes sera n * periodicite .

differe : nombre d’années de différé (0 pour aucun, 1 pour un différé d’un an, etc.) ;

mode : "annuite" pour annuités constantes, "amortissement" pour amortissement constant, "in fine" pour remboursement in fine.