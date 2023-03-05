PROJET OSINT

Ce script Python utilise la bibliothèque whois pour interroger un serveur Whois et récupérer des informations sur un nom de domaine.

Installation
Pour utiliser ce script, vous devez avoir Python 3.x installé sur votre ordinateur, ainsi que la bibliothèque Python whois. Pour installer whois, vous pouvez utiliser la commande suivante :

pip3 install python-whois

Utilisation
Pour utiliser ce script, exécutez la commande suivante :

python3 osint.py <nom_de_domaine>

où <nom_de_domaine> est le nom de domaine pour lequel vous souhaitez récupérer des informations Whois.

Le script affichera alors les informations de domaine disponibles, telles que le registraire, les dates de création et d'expiration, les serveurs de noms, les statuts, les adresses e-mail et les informations DNSSEC.

Les informations seront affichées dans la console en Markdown, et vous pouvez les rediriger dans un fichier ou les convertir en HTML pour une lecture plus facile.

