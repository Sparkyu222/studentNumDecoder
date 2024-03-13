import tabula as tb
import pandas as pd
import sys
import re

# Vérification du nombre d'arguments passé au script
if (len(sys.argv) < 3) or (len(sys.argv) > 3)  :
    print(f'Syntaxe: {sys.argv[0]} <CSV> <PDF>')
    exit(1)

# REGEX pour trouver le numéro étudiant
regex = r'^\d{8}$'

# Lecture du CSV
# CSV qui contient les numéros étudiants ainsi que leurs info associés (nom, prénoms, etc...)
# Schéma obligatoire du CSV : numéro étudiant, nom, prénom
csv = sys.argv[1]
studIdList = pd.read_csv(csv)

# Lecture du PDF, détermination des tableaux
pdf = sys.argv[2]
allTables = tb.read_pdf(pdf, pages="all")

# On prends seulement le premier tableau et on convertie toutes les valeurs en strings
table = allTables[0].astype(str)

# On itère sur chaque colonnes
for col in table.columns:
    # Puis on itère sur chaque lignes dans la colonne
    for i, value in enumerate(table[col]):
        # On vérifie si on match avec le regex d'un numéro étudiant sur la cellule
        if re.match(regex, value):
            # Si c'est le cas, on recherche à quel numéro il correspond
            for j, id in enumerate(studIdList.iloc[:, 0]):
                # Si cela correspond alors on remplace le numéro par le nom et le prénom de l'étudiant
                if (value == str(id)):
                    table.loc[i, col] = studIdList.iloc[j, 1] + " " + studIdList.iloc[j, 2]
                    break

print("")
print("")
print("---")
print("")
print("")

# Enfin, on affiche le Dataframe
print(table)