# TP_CRYPTO
Exercice1:

On remarque en appliquant la fonction MD5 sur “ENSEA” la sortie est toujours la même de 32 caractères a savoir: 

f4c963b6a36060c5f2c4c493a2465d0a 

En changeant un seul caractère on change toute la chaîne de sortie. C'est à dire que si je réécris ENSEA j'aurai la même sortie.

De même en appliquant SHA1 on obtient un résultat similaire avec les mêmes caractéristiques mais avec 40 caractères:
181d3d33921baea651ce3722ba1e26d572446106

Après avoir hacher un grand texte on retrouve toujours le même nombre de caractère avec les deux fonctions respectives. On en conclut que la taille du message de sortie 
ne change pas.
C'est le même constant lorsqu'on change un petit peu notre long texte. 
C'est l'effet avalanche qui est observé.

En se posant la question du fait que notre nombre d'entrée est "infini" alors que le nombre de sortie est de 16^32 ce qui est ironiquement ridicule par rapport à notre
nombre d'entrée. La raison de pourquoi ces modèles ne sont plus sur est la collision. C'est le fait que deux entrées différentes peuvent avoir la même sortie.
De manière concrète il est possible (même si il faut se lever tôt) d'envoyer deux message différent et d'avoir la même sortie. 
Par exemple:
0xd131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70

et

0xd131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70

Pour des alternatives conseillés nous avons vu sha-256 qui est beaucoup utilisé. Il produit des mot de 32 octets soit 64 caractères hexadécimaux.


Enfin une fonction de hachage salé est une fonction qui effectue un hachage un peu différent sur une seule étape. Lorsque l'utilisateur annonce sont entrée, un "salt" se rajoute
à l'entrée ce qui a pour effet de différencier la sortie d'un mot de passe d'un utilisateur avec un autre. L'exemple générique serait par exemple azerty1234, pour un utilisateur,
on aurait une entrée comme celle ci: #ds2&qazerty1234 et pour une autre entrée égale on pourrait avoir: ç54s#dazerty1234.


Exercice2:

En regardant le certificat, on peut identifier plusieurs champs qui sont demandés dans l'énoncé.

Émetteur :
Le certificat a été émis par Google Trust Services. On voit qu’il est situé aux États-Unis et que le nom courant de l’autorité qui a signé ce certificat est WE1. C’est donc cette autorité qui garantit l’authenticité du document.

Sujet :
Le sujet correspond au site qui est certifié, ici ddnet.org(site de jeu opensource). Dans les champs alternatifs, on retrouve ddnet.org et *.ddnet.org, ce qui montre que le certificat couvre aussi les sous-domaines.

Période de validité :
La date “Not Before” indique à partir de quand le certificat est considéré comme valide : 04 Nov 2025, 03:13:13 GMT.
La date “Not After” indique quand il expire : 02 Feb 2026, 04:12:58 GMT.
Au-delà de ces dates, je suppose que l'ayant droit du site devra refaire une maneuvre vis-à-vis de ce certificat.

Clé publique et algorithme associé :
Le certificat utilise une clé elliptique (Elliptic Curve) de 256 bits. La valeur publique est affichée en hexadécimal dans le certificat(04:6D:E2:3C:3A:A2:44:35:43:E6:39:E9:E4:8C:EB:44:69:32:86:45:C4:A8:67:33:62:07:65:C7:D2:31:93:EB:26:00:CD:50:92:51:06:70:D7:7B:3D:01:68:A8:BE:7B:2F:9E:27:29:15:51:20:E9:52:8B:1C:84:A8:9E:E2:1F:34).
Cette clé serait celle que le serveur expose pour que les clients puissent établir une connexion sécurisée.

Algorithme de signature :
L’autorité a signé le certificat avec ECDSA with SHA-256. Cela veut dire que la partie hachage est faite via SHA-256(Qu'on a vu tout à l'heure), puis la signature est effectuée avec ECDSA. Si un seul bit du certificat est modifié, la signature ne correspondra plus.

Empreintes (Fingerprints) :
Les empreintes sont les résumés cryptographiques du certificat. La SHA-256 est :
7C:44:42:22:6C:CD:74:C5:FB:FA:41:3A:A8:E7:ED:6D:A7:9F:F6:49:59:10:D7:DA:D0:EA:41:6C:D1:C1:AD:39
La SHA-1 est aussi donnée :
20:88:EB:6B:B8:5D:D4:16:E8:6E:13:E8:8D:FE:F0:41:E3:84:74:90
Comme on l'a vu c'est ce qui permet d'identifier de manière unique le certificat.

(La plupart des informations viennent du site ssl.com)

Ensuite on nous demande des informations sur l'autorité de certification.

Une autorité de certification, ou CA, c’est tout simplement l’entité qui dit valide un certificat. C’est elle qui vérifie l’identité d’un site, d’une organisation ou d’un utilisateur, puis qui délivre un certificat. Sans elle, personne ne saurait si la clé publique appartient vraiment à la bonne personne ou au bon site.
Dans la PKI c'est cette autorité qui gère le système de confiance.

En ce qui concerne la chaîne de certification, le certificat que j’ai récupéré pour ddnet.org n’est que le certificat final, celui du site lui-même. En remontant la chaîne de vérification, on passe par le certificat intermédiaire, puis on arrive au certificat racine, qui est totalement fiable. C’est ce certificat racine qui garantit à 100% que ddnet.org est authentique et que la clé publique du site correspond bien au domaine.  

Dans notre cas la chaîne de vérification peut se trouver dans le même endroit on a récuperé les informations. Sur ddnet.org on voit l'émetteur qui est WE1 qui a lui même comme émetteur GTS Root R4. C'est lui le certificat racine.

Quand un certificat est révoqué, ça veut dire qu’il n’est plus fiable. Même si la date de validité n’est pas dépassée, il ne faut plus faire confiance à ce certificat. Pour le vérifier on a deux outils qui sont CRL et OCSP. CRL est une liste venant de l'autorité de certification qui contient tous les certificats révoqués.L'OCSP est plus simple d'utilisation car on n'a pas besoin de vérifier tous les certificats et on peut "interroger" le CRL pour notre certificat spécifique.

On peut maintenant voir les extensions annexes qu'on a pu voir auparavant comme Subject Alternative Name qui permet de ne pas refaire des certificats pour les sous-domaines.

On key usage qui dans notre cas est Digital Signature ce qui veut dire que la clé sert à signer les échanges. Dans le même style on a Extended Key Usage qui a comme valeur:Server Authentication. Cela nous dit que le certificat est utilisé pour authentifier un site web(comme prévu!).

Un certificat auto-signé est un certificat qui se signe lui-même. Ce qui veut dire que l’émetteur et le sujet sont identiques, et donc  qu'il n’y a pas d’autorité de certification pour garantir son authenticité. C'est donc une application qui n'est vraiment pas appliqué à internet mais uniquement avec des gens de confiances.


Exercice4:

4.1) Un bloc Bitcoin contient d’abord un en-tête où on trouve quelques infos techniques comme la version, le hash du bloc d’avant, la racine de Merkle, l’heure indiquée par le mineur, la difficulté et le nonce. Après cet en-tête, on a simplement toutes les transactions du bloc, en commençant par la coinbase qui sert à payer le mineur.

4.2) En général, la taille d’un bloc tourne autour de 1,3 à 2 Mo. La valeure moyenne affiché sur les sites donnés dans le sujet est environ 300B mais apparament ça serait seulement la taille du header. Il y'a bien une limite de taille.

4.3) Un bloc contient en moyenne entre 2 500 transactions. Le nombre exact dépendrai de la taille des transactions en en permettant plus ou moins.

4.4) L’en-tête d’un bloc contient plusieurs champs techniques qui servent à identifier le bloc et à vérifier qu’il est valide. On y trouve : la version du bloc, le hash du bloc précédent, la racine de Merkle qui résume toutes les transactions, l’horodatage indiqué par le mineur, le champ “bits” qui représente la difficulté actuelle, et enfin le nonce, qui est la valeur que les mineurs modifient pour tenter de produire un hash conforme aux règles du réseau.

4.5) Le champ « Previous Block Hash » sert simplement à relier chaque bloc au bloc qui vient juste avant lui. Grâce à ça, tous les blocs s’enchaînent les uns aux autres, ce qui forme la blockchain. Si un seul hash précédent changeait, tous les blocs suivants deviendraient invalides. Ce champ garantit l’intégrité et l’ordre de la chaîne.

4.6) Le nonce est un nombre que les mineurs modifient en boucle quand ils essaient de trouver un hash de bloc qui respecte la difficulté du réseau. Comme le hash dépend de ce nonce, ils le changent à chaque essai afin de produire un nouveau hash. Une fois qu'un nonce compatible est trouvé, le mineur peut proposer un bloc au réseau. le nonce est sur 32 bits.

4.7) Pour créer un nouveau bloc, le mineur commence par rassembler les transactions en attente. Il prépare ensuite l’en-tête du bloc avec le hash du bloc précédent, la racine de Merkle, la date et la difficulté. Il teste ensuite différentes valeurs de nonce jusqu’à trouver un hash qui correspond aux règles du réseau. Une fois trouvé, le bloc est envoyé au réseau et ajouté à la blockchain après validation. Concrètement il doit modifier chaque bit du nonce puis hacher avec SHA-256 jusqu'à ce que le résultat soit valide.

4.8) Le minage, c’est le processus où les mineurs essaient plein de combinaisons pour trouver un hash valide. Il sert à sécuriser la blockchain et à valider les transactions. C’est aussi le moyen par lequel de nouveaux bitcoins sont créés grâce à la récompense du bloc.

4.9) La difficulté indique à quel point il est difficile de trouver un hash qui respecte les règles. Elle s’adapte automatiquement tous les 2016 blocs pour que les nouveaux blocs sortent en moyenne toutes les 10 minutes. Si les mineurs trouvent les blocs trop vite, elle augmente. S’ils mettent trop de temps, elle baisse.

4.10) Je n'ai pas trouvé d'information fiable ni de moyen de calculer le nombre de 0 initiaux. Selon certain site nous aurions entre 18 et 20 0 initiaux.

4.11) La première récompense était de 50 BTC par bloc sachant que la valeur d'un BTC était de quelque centimes

4.12) Le premier bloc, le bloc « genesis » (bloc #0), est particulier : il est le tout premier bloc de la chaîne, il ne référence aucun bloc précédent (puisqu’il n’y en a pas).
De plus, la récompense de ce bloc est considérée comme non dépensable, ce qui rend le bloc “hors-norme” comparé aux blocs suivants. 

4.13) Le message contenu dans le bloc génésis est:
"The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"

4.14) Après ce premier halving, la récompense par bloc est passée de 50 BTC à 25 BTC.

4.16) Un halving se produit tous les 210 000 blocs selon le protocole de Bitcoin. 

4.17) Puisqu’en moyenne un bloc est créé toutes les 10 minutes, 210 000 blocs représentent 1460 jours. Donc, un halving a lieu en moyenne tous les 1460 jours

4.18) Jusqu’à maintenant, il y a déjà eu quatre halving. 

4.19) La récompense actuelle par bloc est de 3.125 BTC. 

4.20/21) Si on part du principe qu'un bloc se complète en 10 minutes pile, on 525 960 minutes en 1 ans donc 52 596 blocs/an. Connaissant la production par ans, ils nout faut savoir le nombre maximum de bitcoin possible pour savoir à quelle date. 
Sachant que à chaque halving(tout les 210 000 blocs), on divise la récompense par 2 et qu'on commence à 50 BTC, nous avons une suite géométrique de raison 1/2. Cette converge vers 21 millions qui est donc une valeur assymptotique. Connaissant cette limite il faut donc 48 000 jours. La limite sera donc atteinte en 2140.

4.22) Le temps moyen ciblé entre deux blocs dans Bitcoin est d’environ 10 minutes.

4.23) C'est à ça que sert la difficulté. Lorsque que le trafic sera très grand, la difficulté sera aggrandie et inversement pour "garantir" un temps moyen de 10 minutes.

4.24) La difficulté est réajustée tous les 2016 blocs, soit environ tous les 14 jours (2016 × 10 minutes = 20 160 minutes ≈ 14 jours).

4.25) Si la puissance de calcul du réseau double, les blocs seront trouvés théoriquement deux fois plus vite donc 5 min. En revanche au prochain ajustement de la difficulté la moyenne sera ramené à 10 minutes pas bloc comme convenu.

4.26)Ajouter un zéro supplémentaire dans le hash cible correspond à diviser la cible par 16.Comme le hash est aléatoire, il faudrait donc 16 fois plus de puissance de calcul pour trouver un bloc valide avec ce zéro supplémentaire.

4.27) Il faut attendre plusieurs confirmations pour être sûr qu’une transaction est définitive, car la blockchain peut subir de petits forks temporaires. Plus il y a de confirmations, plus il devient improbable qu’un bloc contenant la transaction soit réécrit. De manière un peu injuste, on peut trouver une solution qui ne sera jamais validée.

4.28) Pour une transaction importante, il est généralement recommandé d’attendre 6 confirmations, ce qui correspond à environ 1 heure sur Bitcoin.(https://bitcoin.org/fr/vous-devez-savoir?)

4.29) Une attaque des 51 % se produit lorsqu’un mineur contrôle plus de la moitié de la puissance de calcul du réseau. Dans ce cas, il peut créer une chaîne plus longue que celle du reste du réseau et la faire accepter comme valide. Concrètement, l’attaquant peut miner en secret une chaîne alternative dans laquelle il n’inclut pas certaines de ses propres transactions, par exemple un paiement qu’il a déjà effectué. Pendant ce temps, le reste du réseau continue à accepter la chaîne publique. Si l’attaquant parvient ensuite à publier une chaîne plus longue (donc avec plus de preuve de travail), le réseau l’adopte automatiquement. Les blocs précédents sont alors abandonnés. C'est l'implication d'avoir ce monopole à savoir réécrire l'historique récent. C'est donc primordial que la puissance de calcul du réseau soit répartie entre de nombreux mineurs pour rentre ce type d'attaque très couteuses donc très difficile.

4.30) La fonction de hachage est SHA-256 qui comme vu plus haut dans le TP est très populaire.

4.31) Un hash est SHA-256 est donc de 32 octet soit 256 bits.

4.32) C'est l'entête qui est utilisé comme preuve de travail et non pas l'intégralité des transactions ce qui semble logique.

4.33) Lorsqu'on observe plusieurs hashs de blocs on peut noter qu'ils sont en hexadécimal. Ils font tous la même taille de 64 caractères hexadécimaux.

4.34) La preuve de travail consiste simplement à trouver un hash du bloc qui respecte une contrainte imposée par le réseau donc modifier le nonce dans l'en-tête puis haché jusqu'à obtrenir un hash suffisamment petit comme vu précedement. Grâce à cet effort de calcul, la blockchain est sécurisé et empêche les attaques à moins d'avoir le scénaro du 51%.

4.35) Un bloc est valable mathématiquement si le hash de son en-tête est inférieur ou égal à une valeur cible appelée target. C'est cette valeur que la difficulté impacte comme on a pu le voir. Très rapidement plus la difficulté est grande, plus la target est petite et plus il est compliqué de trouvé un bon hash. Si on devait donner une formule ça serait comme ceci: SHA256(header) < Target.

4.36) Le nombre moyen de hash dépend de la difficulté. On a deja 2^32 qui est le nombre moyen de nonce à tester pour une difficulté de 1. Le vrai nombre est donc 2^32 * difficulté. Nayant pu trouvé la difficulté actuelle je ne peux pas faire ce calcul mais l'idée est la.

Exercice pratique:

J'ai choisi de prendre le bloc 927737 qui a comme hash 00000000000000000000d2ab9b5ba7e4de666a38da3a24e6ee2d50554ac81ffa sachant que le hash précedent est ceci 00000000000000000001b2037f2ce876da458e318962869f9c21ea47d4d159b3. Comme prévu ils sont très différent du à la fonction SHA-256 sauf les 0 au début qui témoigne de l'impact de la difficulté. Ensuite ce bloc à comme Timestamp 2025-12-13 16:48:51 et a 3834 transactions. Il a une taille de 1.57 MB pour une difficulté de 148195306640204.7 avec comme nonce 0x26cb429c. On prend vraiment conscience de la puissance de calcul nécessaire pour trouver toute les combinaisons avec de tel nombre. Enfin la ré compense totale du mineur est de 3,167 BTC avec comme pool de minage F2Pool.

4.37) La structure en chaîne de blocs garantit l’immutabilité des transactions grâce à l’utilisation de hash cryptographiques et au lien entre les blocs. Chaque bloc contient le hash du bloc précédent, ce qui fait que si quelqu’un voulait modifier une transaction passée, il faudrait recalculer tous les hashs des blocs suivants, ce qui demande une puissance de calcul astronomique. Comme le réseau adopte toujours la chaîne ayant la plus grande preuve de travail, une modification locale est pratiquement impossible, ce qui rend l’historique des transactions quasi permanent et fiable à moins d'avoir une puissance de calcul démesuré ou que peut de personne soit présente sur le trafic.

4.38) Bitcoin est un système décentralisé parce qu’il n’y a pas d’autorité centrale qui contrôle les transactions ou émet la monnaie. Le réseau fonctionne grâce à des nœuds distribués qui vérifient et relaient les transactions, et des mineurs qui ajoutent de nouveaux blocs via la preuve de travail. Chacun peut rejoindre le réseau et participer à la validation, ce qui rend le système résistant à la censure et aux attaques, puisque le contrôle n’est pas concentré entre les mains d’un acteur unique. Comme analogie on pourrait penser à une immense projet open-source.

4.39) En prenant des blocs de 1 MB et un bloc toutes les 10 minutes, Bitcoin peut traiter environ 7 transactions par seconde, ce qui est très faible comparé à des systèmes comme Visa qui peuvent atteindre plusieurs milliers de transactions par seconde. Cette lenteur ne limite pas la sécurité du réseau, mais elle restreint la scalabilité, ce qui explique pourquoi des solutions comme le Lightning Network sont nécessaires pour accélérer les paiements sans compromettre la décentralisation.

4.40) La preuve de travail consomme énormément d’électricité parce que les mineurs doivent effectuer des milliards de calculs pour trouver un bloc valide. Cette consommation a un impact environnemental significatif, surtout si elle dépend de sources non renouvelables. 
Pour réduire cette empreinte, des alternatives comme le Proof of Stake  sont proposées. Dans un système Proof of Stake, les blocs ne sont pas créés en résolvant des calculs complexes comme dans la preuve de travail, mais par un processus de sélection basé sur la quantité de cryptomonnaie détenue par chaque participant, appelé validator. Plus un validateur possède de crypto, plus il a de chances d’être choisi pour créer le bloc suivant. On a donc une économie d'énergie massive car il n'ya plus besoin de calculer des milliards de hashes qui ne servent théoriquement.

4.41) Sur les six derniers mois, le hashrate total du réseau Bitcoin a généralement augmenté, ce qui reflète l’arrivée de nouveaux mineurs ou l’amélioration des équipements. Une augmentation du hashrate rend le réseau plus sûr, car il devient plus difficile pour un attaquant de prendre le contrôle de la chaîne.







