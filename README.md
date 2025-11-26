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




