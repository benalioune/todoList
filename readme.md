# add dependancies 
- pytest pour les tests 


# Tests
## Installation de pytest

- test files
python -m pip install --upgrade pip 
pip install pytest
pytest --version

## Créer un fichier de test
Dans le dossier "tests", créer un nouveau fichier appelé "test_add.py" et ajouter ce code :
python  
python3
python3.9
print("Hello World")
## Exécuter des tests avec la commande pytest

- Ouvrir une console dans VSCode (F12) puis exécuter
bash: pytest test_add.py
ou simplement
pytest test_add.py

## Les assertions
Les assertions sont utilisées pour définir les résultats attendus. Si l'assertion est vraie, alors tout est bien. Sinon, il y a une erre
Les assertions sont utilisées pour vérifier si un élément est vrai ou non
python
assert True, "This is true"
assert False, "This is false"
La dernière assertion ne s'exécutera pas car elle est fausse. Pour que cela fonctionne, il faut utiliser l'argument "-x" qui arrête à
La ligne ci-dessus va lever une exception AssertionError car l'expression est fausse
