---
layout: post
title:  Outils de Rigging
lang: fr
ref: rigging_tools
tags: [Rigging]
permalink: /fr/:year/:month/outils-de-rigging/
redirect_from:
  - /fr/2015/03/outils-de-rigging/
img: 20150311_rigging_tools.png
---




Bonjour à tous,
Je travaille actuellement sur un court métrage en tant que Rigger & Animateur. Pendant la phase de rigging, j'ai développé quelques outils pour m'aider.

La plupart de ces outils sont encore en cours de développement, mais en voici quelques uns. Je les ai réunis dans un menu Pie. Ce menu lui même est un WIP, avec des noms temporaires.

### Visualisation des calques

Pour démarrer, une petite astuce ... car ce n'est pas un outil ! Entre l'_Outliner_ et le panneau des propriétés, je rajoute une nouvelle fenêtre (de type Propriétés également), que je positionne sur les calques de l'armature. Je masque le _header_ de cette fenêtre, et je la redimensionne pour visualiser uniquement les calques. De cette manière, je peux accéder rapidement aux calques des os, sans changer d'onglet si j'étais précédemment sur un autre onglet, comme celui des contraintes par exemple.

![][1]

### Affichage

J'ai ajouté au menu Pie un accès rapide à la plupart des modes d'affichage pour l'armature/les os :

![][2]

Et voici comment sont donc affichés les os :

![][3]

### Renommer les chaînes d'os

Renommer les os peut être long et fastidieux ! J'ai crée un script pour renommer automatiquement les os. Par exemple, lorsqu'il s'agit de renommer les os des doigts, au départ, tous les os sont nommés _Bone.XYZ_

![][4]

Il suffit de renommer un seul os, et utiliser un opérateur depuis le menu Pie.  
Par exemple, si on souhaite renommer les os en _finger_X.L_, avec _X_ égale à 0, 1, 2, 3 et 4, il faut renommer le premier os de la première chaine en _finger_.L_. Ensuite, il faut sélectionner tous les premiers os de chaque chaîne (chaque doigt), en prenant soin de sélectionner l'os déjà renommer en dernier.

![][5]

Tous les os sont ainsi renommés, en fonction de la chaîne à laquelle ils appartiennent, ainsi qu'en fonction de la position dans la chaîne :

![][6]

Le nom des chaînes est choisi en fonction de l'ordre alphabétique des os sélectionnés. Ici, dans notre exemple, l'os actif devient _finger_0.L_, Bonne.002 devient _finger_1.L_, etc... Si l'on souhaite réellement choisir l'ordre des chaînes, il faut, avant d'utiliser l'opérateur, renommer les premiers os de chaque chaîne dans l'ordre alphabétique.

### Sélection des os non parentés

Cet outil sélectionne automatiquement les os non parentés. Cela est utile pour tous les connecter à l'os racine (_root_). En utilisant cet outil, l'os racine sera lui aussi sélectionné. Il suffit de le dé-sélectionner et le re-sélectionner (pour le rendre actif), et de le parenter avec _Control+P_.

### Régler le nombre de segments pour les BBones

Concernant les BBones, régler un par un le nombre de segments peut être looonng ! Je peux maintenant les régler en une seule fois, en utilisant le nombre de segments indiqués dans les préférences de l'add-on.

![][7]

### Copier la mise à l'échelle de l'os _root_

Si on décoche "_inherit scale_" sur certains os, il est nécessaire d'ajouter une contrainte "_copy scale_" sur cet os, en copiant la mise à l'échelle de l'os racine, pour être capable de changer la taille globale du modèle en changeant la mise à l'échelle de l'os racine. Trouver ces os, et rajouter la contrainte (en premier dans la pile des contraintes), cela peut prendre du temps :)

J'ai créé un outil qui réalise cette action : l'outil sélectionne les outils impactés, rajoute la contrainte, et déplace cette contrainte au début de la pile.

### Miroir

Jusqu'à présent, pour réaliser un miroir de mon armature, je réalisais les étapes suivantes :

*  Duplication des os (les nouveaux os sont maintenant sélectionnés)
*  Changement des noms des nouveaux os en utilisant l'outil _flip names_
*  Inversion de la sélection (les anciens os sont maintenant sélectionnés)
*  Déplacement des os (mais je valide la transformation avant d'avoir réalisé le moindre déplacement). Cette étape est nécessaire pour recalculer la position des nouveaux os.

Ce process fonctionne dans certains cas. Mais pour les rigs un peu complexe, cela ne fonctionne pas. Cela mène à des grosses erreurs dans le rig, en ce qui concerne le parentage et les targets pour les contraintes.

![][8]

J'ai soumis un rapport de bug ([mirror bones][14]), mais qui a été refusé puisque ce process n'est au départ pas fait pour réaliser le miroir d'une armature. J'ai donc développé un outil qui réalise un miroir correct !

Mais ... cela est assez long. Pour réaliser un miroir d'un rig complexe, comme Charlie, qui peut être télécharger sur le site de [Puppeteer Lounge][9], cela fonctionne correctement, mais le process prend 1min05 ( pour 130 os). Assez long, mais toujours moins que de le faire à la main :)

J'ai donc décidé de l'implémenter directement dans Blender. J'ai écrit un patch : [Bone Mirror][10].

Actuellement, ce patch n'est pas encore accepté dans Blender. La même modification (130 os sur Charlie) est maintenant réalisé instantanément.

[Mise à jour du 19 mars] : Campbell a réalisé quelques corrections et ajustement sur mon patch, et vient de l'intégrer dans le code source. Cette nouvelle fonctionnalité sera donc disponible dans Blender 2.75


### Quelques bugs découverts ...

Pendant la phase de rigging du projet (qui n'est pas encore terminée), j'ai découvert et reporté quelques bugs sur [developer.blender.org][11]. Excepté le miroir (j'ai déjà écrit qu'il avait été refusé), les autres ont été corrigés, et sont disponible dans Blender 2.74 :

* [Bug quand on utilise "clear user transform" en mode "weight painting"][12]

* [Skinning : "set parent with automatic weights" ne prend pas en compte les groupes protégés des modifications][13]

### Conclusion

Il n’y a pas vraiment de conclusion, puisque ces outils ne sont pas encore stables, et peuvent (et seront) encore modifiés, en fonction de mon workflow.

Cet add-on n'est pas disponible au téléchargement, mais sera disponible dans les prochains mois.

Voici une vidéo, en français, à propos de ces différents outils :

{% include youtube.html id='bv66gdexbqg' %}


[1]: {{ site.baseurl }}/assets/imgs/post/2015/03/bone_layers.png
[2]: {{ site.baseurl }}/assets/imgs/post/2015/03/display_mode.png
[3]: {{ site.baseurl }}/assets/imgs/post/2015/03/display_example.png
[4]: {{ site.baseurl }}/assets/imgs/post/2015/03/rename1.png
[5]: {{ site.baseurl }}/assets/imgs/post/2015/03/rename2.png
[6]: {{ site.baseurl }}/assets/imgs/post/2015/03/rename3.png
[7]: {{ site.baseurl }}/assets/imgs/post/2015/03/segment.png
[8]: {{ site.baseurl }}/assets/imgs/post/2015/03/mirror1.png
[9]: http://www.puppeteerlounge.com/free-characters
[10]: https://developer.blender.org/D1147
[11]: http://developer.blender.org
[12]: https://developer.blender.org/T43776
[13]: https://developer.blender.org/T43814
[14]: https://developer.blender.org/T43760
