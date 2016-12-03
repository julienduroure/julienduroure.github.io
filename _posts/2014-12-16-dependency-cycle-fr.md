---
layout: post
title:  Rigging - Cycle de dépendance
lang: fr
ref: dependency-cycle-detected
tags: [Rigging, Tuto]
permalink: /en/:year/:month/detection-cycle-de-dependance/
img: 20141216_dep.png
comments: true
---

Bonjour à tous,  
Aujourd'hui, un article plus technique que artistique :)

![][1]

## Point de départ

Durant les derniers mois, j'ai commencé à créer un Rig de bipède, basé sur les propriétés de plusieurs rigs "habituels". Ces propriétés ne sont pas le sujet de cet article.  

Le fait est que la première version de ce rig était complètement buggé. Les fonctionnalités du rig sont bien là, mais il y avait des comportements bizarres dans certains cas.

_Cetains gif sont assez lourd, soyez patient :)_

![][2]

![][3]

A noter que le modèle utilisé pour ce rig est © 2012 Nathan Vegdahl and The Blender Foundation, sous license CC BY 3.0, et est téléchargeable sur le Blender Cloud.

Comme on peut le voir sur le premier gif, il y a quelques secousses quand on bouge certains os.

Sur le deuxième gif, on peut voir que lorsqu'on réinitialise les transformations de tous les os, on doit réaliser cette opération plusieurs fois pour que cela soir réellement fait.

## Qu'est ce qui ne va pas avec ce rig ?

La façon la plus simple de trouver ce qui ne va pas est d'afficher la console :  

![][4]

Il y a des erreurs détectées (particulièrement quand on bascule du mode _Edit_ au mode _Pose_)

## Graphe de dépendance et cycles

Il est temps de comprendre ce qui se cache réellement derrière ces mots. Un graphe de dépendance est un manière de stoquer l'ensemble des relations entre les "objets" dans Blender. 2 "objets" (il peut s'agit d'objets, de matériaux, de textures, d'os, etc...) sont liés si certains paramètres du 2ème objet dépendent du premier objet (par leur position, couleur, ou autre données). L'objet 2 est donc lié à l'objet 1. Le graphe de dépendance est un graphe global qui représente tous les liens entre l'ensemble des données dans Blender.

Voici un exemple de ce qu'on peut voir sur le site wiki.blender.org, sur la page _Dependency graph_:  

![][5]

Dans cet exemple, le graphe va du tube à la scène. Un cycle de dépendance est créé quand un noeud B est dépendant d'un noeud A, mais que le noeud A est aussi dépendant du noeud B (avec potentiellement des noeuds intermédiaires). Dans l'exemple, un cycle serait créé si le tube est dépendant du plan (parce que le plan est déjà dépendant du tube).

## Quelques exemples concernant le Rigging

Dans les exemples suivcant, je vais montrer quelques cycles de dépendances, au niveau des os d'un rig. Les os peuvent être liés de deux manières différentes :  

*  Par contraintes
*  Par parentage

### Exemple 1

Dans cet exemple, ([.blend][6]), 3 os sont liés par des contraintes _Copy Location_.

![][7]  
![][8]  
![][9]  

Resultat : Aucun des os ne peut bouger !


### Exemple 2

Dans cet exemple ([.blend][10]) , non seulement les contraintes _Copy Location_ sont utilisées, mais aussi le parentage (parentage sans être connectés).

![][11]  
![][12]  
![][13]  

Resultat, quand on essaie de bouger l'os _Bone.001_ (en haut) :

![][14]

Il y a des mouvements étranges. Remettre les valeurs par défaut ne fonctionne pas, sauf si on passe en mode _Edit_.


### Example 3

Cet exemple ([.blend][15]) est assez similaire à l'exemple 2, mais utilise une contrainte _IK_ au lieu de _Stretch To_.

A noter que la contrainte _IK_ ne s'applique pas seulement à un os (en jaune), mais c'est toute la chaine qui est contrainte.

![][16]  
![][17]  
![][18]  

Même résultat quant on essaie de bouger la cible de la contrainte _IK_.
Same result when trying to move the IK target :

![][19]  

### Exemple 4

Cet exemple ([.blend][20]) est différent des autres, puisqu'il lie des os et des objets.

![][21]  
![][22]  
![][23]  

Comme on peut le voir, le graphe de dépendance reste au niveau objet. Ce qui signifie que l'armature est vu comme un seul objet, et qu'un autre graphe de dépendance, à l'intérieur de l'armature, est utilisé pour évaluer les relations entre les os.

Resultat : Ca vibre.

![][24]  

Une refonte complète du graphe de dépendance est en cours, pendant le projet _Goosberry_. Avec la nouvelle version du graphe de dépendance, la granularité des noeuds du graphe de dépendance principal sera descendu jusqu'au niveau des os. Ce qui signifie que cet exemple ne sera plus un cycle de dépendance, et pourrra être représenté comme cela :

![][25]  

### Exemple 5

Ce dernier exemple ([.blend][26]) montre les limitation de la détection des cycles de dépendance.

![][27]  
![][28]  
![][29]  

Manipuler ce rig ne montre pas de comportement incohérent, sauf quand on essaie de réinitialiser les valeurs.

![][299]  

## Debugger mon rig

Après ces exemples assez simples, retournons à mon rig buggé ! J'ai développé un script capable de visualiser les graphes de dépendances de mes armature, utilisant [Graphviz][30]. Voici une première image que j'ai généré. Les liens de parenté sont en noir, les contraintes de position en rouge, de rotation en bleue, de mise à l'échelle en vert.

![][31]

La première que l'on peut voir, en haut à gauche, est que les os _MCH-ST_ et _spine.def_ sont assez séparés des autres os. En regardant les os _spine.def_, on voit que ces os de déformation sont utilisés, via des contraintes, pour modifier la valeur d'autres os. C'est une grosse erreur dans mon rig.


En utilisant [ce code][32], j'ai essayé de visualiser les cycles de dépendance dans mon rig (en rouge).

![][333]

Puisque j'ai mis mon os dans des calques spécifiques, mon rig est relativement bien organisé. Chaque chaine se trouve dans un calque différent, j'ai donc modifié mon script pour regrouper les os dans les calques.

![][33]

A partir de ces informations, j'ai réfléchi aux fonctionnalité de mon rig, et comment le simplifier tout en gardant les même fonctionnalités, en évitant les cycles de dépendance.

Et j'ai gagné :)

Mon nouveau rig est fonctionnel, sans cycle de dépendance, sans comportement bizarre.

Voici le nouveau graphe de l'armature :

![][34]


[1]: {{ site.baseurl }}/assets/imgs/post/2014/12/rigging.png
[2]: {{ site.baseurl }}/assets/imgs/post/2014/12/jiggle.gif
[3]: {{ site.baseurl }}/assets/imgs/post/2014/12/reset.gif
[4]: {{ site.baseurl }}/assets/imgs/post/2014/12/dep_cycle.png
[5]: https://wiki.blender.org/uploads/6/61/Dev_depsgraph_example_screen.png
[6]: https://drive.google.com/open?id=0B-mpivl1jPpuSURRZXNURTR4SzQ
[7]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep1.png
[8]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep_console.png
[9]: {{ site.baseurl }}/assets/imgs/post/2014/12/dc1.png
[10]: https://drive.google.com/open?id=0B-mpivl1jPpuTUh2M0xzTEd6X0k
[11]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep2.png
[12]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep2_console.png
[13]: {{ site.baseurl }}/assets/imgs/post/2014/12/dc2.png
[14]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep2.gif
[15]: https://drive.google.com/open?id=0B-mpivl1jPpuVVhoTEVOSHVHNU0
[16]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep3.png
[17]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep3_console.png
[18]: {{ site.baseurl }}/assets/imgs/post/2014/12/dc3.png
[19]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep3.gif
[20]: https://drive.google.com/open?id=0B-mpivl1jPpuaGF5OFdJT2JjT00
[21]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep4.png
[22]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep4_console.png
[23]: {{ site.baseurl }}/assets/imgs/post/2014/12/dc4.png
[24]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep4.gif
[25]: {{ site.baseurl }}/assets/imgs/post/2014/12/dc4_2.png
[26]: https://drive.google.com/open?id=0B-mpivl1jPpuaWJxYTJ3NV9nQ3M
[27]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep5.png
[28]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep5_console.png
[29]: {{ site.baseurl }}/assets/imgs/post/2014/12/dc5.png
[299]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycle_dep5.gif
[30]: http://www.graphviz.org/
[31]: {{ site.baseurl }}/assets/imgs/post/2014/12/color.png
[32]: http://lists.research.att.com/pipermail/graphviz-interest/2007q3/003396.html
[33]: {{ site.baseurl }}/assets/imgs/post/2014/12/cycles.png
[333]: {{ site.baseurl }}/assets/imgs/post/2014/12/layers.png
[34]: {{ site.baseurl }}/assets/imgs/post/2014/12/nv.png
