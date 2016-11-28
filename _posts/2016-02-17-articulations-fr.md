---
layout: post
title:  Articulations
permalink: /fr/:year/:month/articulations/
redirect_from:
  - /2016/02/articulations
lang: fr
ref: articulations
tags: [Rigging, Skinning, Topology]
img: 20160217_articulations.png
comments: true
---


Bonjour à tous,  
Aujourd'hui, je vais aborder un sujet que je n'ai encore jamais traité : la topologie. Et plus particulièrement celle qui concerne les articulations, du coude par exemple.

_Disclamer_ : Ceci n'est pas un tutoriel, ni une liste de bonnes pratiques. Il s'agit uniquement de quelques travaux/recherche que j'ai effectué. Il existe sans doute d'autres manières de faire, peut être (sous doute) plus efficace que ce que je vais montrer/proposer ici.

Ceci étant dit, voilà de quoi il s'agit : J'ai suivi plusieurs pistes, afin d'obtenir une articulation cohérente d'un cylindre. Celui-ci peut se plier dans un seul sens, jusqu'à 150° environ. Il peut donc s’apparenter à un coude.

{% include html5video.html id="/2016/02/joint.ogv" gif=true size="50%" %}

## Situation de base

Il s'agit d'un simple cylindre coupé à mi-hauteur, avec 2 os, et un _Weight Paint_ basique.

![][1]  

![][2]![][3]

On peut le voir, le résultat est ... médiocre.

{% include html5video.html id="/2016/02/step1.ogv" gif=true size="20%" %}

## Préservation du volume

La 1ère chose à faire est de cocher Volume Preservation dans le modificateur Armature.

![][4]

Le résultat s'améliore légèrement, même si on est encore loin du compte :

{% include html5video.html id="/2016/02/step2.ogv" gif=true size="20%" %}

## Changer la topologie

Dans l'étape suivante, j'ai modifié le maillage du cylindre, afin d'avoir une déformation qui se limite à la zone de pliure, en rajoutant simplement 2 _loopcuts_.

![][5]  

![][6]![][7]

Maintenant, on a effectivement une déformation qui se limite à la zone qui nous intéresse, une perte de volume beaucoup moins importante. Mais on se retrouve avec des intersections de face lorsque l'angle est important :

{% include html5video.html id="/2016/02/step3.ogv" gif=true size="20%" %}

## Modifier encore la topologie

J'ai ensuite modifié la topologie, afin d'éviter les intersections.

Le principal inconvénient est que maintenant, l'articulation est optimisé pour se plier dans un seul sens. Ce qui est le cas du coude.

![][8]  

![][9]![][10]

On a encore des problèmes d'intersections, mais l'étape suivante va corriger en partie ce souci :

{% include html5video.html id="/2016/02/step4.ogv" gif=true size="20%" %}

## Ajout du SubSurf

J'ai ensuite ajouté un modificateur SubSurf sur la maillage.

![][11]

On commence ici à avoir des intersections limitées :

{% include html5video.html id="/2016/02/step5.ogv" gif=true size="20%" %}

## Ajout de Shape Keys

Pour limiter l'intersection, j'ai ensuite rajouté une _shape key_, qui sera activé par un driver selon la rotation de l'articulation :

{% include html5video.html id="/2016/02/step6_shapekey.ogv" gif=true size="30%" %}

![][12]

Cette fois-ci, on n'a plus d'intersections. Par contre, l'articulation se retrouve "palmée" :

{% include html5video.html id="/2016/02/step6.ogv" gif=true size="20%" %}

Pour éviter ce phénomène "palmé", on peut jouer sur la valeur drivé du shapekey. Je ne vais pas le faire de suite, mais testé d'abord une autre modification.

## Déplacer l'armature

Sans modifier le _weight paint_, j'ai ensuite déplacé la position des os (en mode _Edit_, donc) pour les rapprocher de l'intérieur de l'articulation.

![][13]

Voilà ce que ça donne (sans le _shapekey_ de l'étape précédente) :

{% include html5video.html id="/2016/02/step7.ogv" gif=true size="20%" %}

## Mix des deux méthodes

A partir, des deux méthodes précédentes (avoir les os rapprochés de l'intérieur de l'articulation, et shapekey), on obtient de résultat suivant :

{% include html5video.html id="/2016/02/step8.ogv" gif=true size="20%" %}

On retrouve l'articulation palmée, même accentuée par rapport à tout à l'heure. Il est donc temps de régler correctement le _driver_.

## Ajuster le driver

Comme dit au dessus, il faut ajuster la plage de rotation de l'articulation qui influence le driver, ou bien diminuer la valeur du driver.

![][14]

On a maintenant un résultat acceptable :

{% include html5video.html id="/2016/02/step9.ogv" gif=true size="20%" %}

## Ajouter un autre _shapekey_

Niveau intérieur de l'articulation, on a maintenant une pliure convenable, mais côté extérieur, on a quelque chose de beaucoup trop arrondi. Regardez votre coude, vous verrez :)

Je vais donc rajouter un deuxième _shapekey_, afin de faire ressortir l'os du coude. On conserve bien entendu le premier.

{% include html5video.html id="/2016/02/step10_shapekey.ogv" gif=true size="20%" %}

![][15]

Voici le résultat final :

{% include html5video.html id="/2016/02/step10.ogv" gif=true size="20%" %}

## Conclusion

Voici donc mes différents tests. Le fichier complet est disponible en téléchargement ici : [Articulations][16]

Comme dit plus haut, ceci est uniquement un test. Je n'ai jamais appliqué cette technique en production.

[1]: {{ site.baseurl }}/assets/imgs/post/2016/02/step_1.png
[2]: {{ site.baseurl }}/assets/imgs/post/2016/02/step_1_weight1.png
[3]: {{ site.baseurl }}/assets/imgs/post/2016/02/step_1_weight2.png
[4]: {{ site.baseurl }}/assets/imgs/post/2016/02/step2.png
[5]: {{ site.baseurl }}/assets/imgs/post/2016/02/step3.png
[6]: {{ site.baseurl }}/assets/imgs/post/2016/02/step3_weight1.png
[7]: {{ site.baseurl }}/assets/imgs/post/2016/02/step3_weight2.png
[8]: {{ site.baseurl }}/assets/imgs/post/2016/02/step4.png
[9]: {{ site.baseurl }}/assets/imgs/post/2016/02/step4_weight1.png
[10]: {{ site.baseurl }}/assets/imgs/post/2016/02/step4_weight2.png
[11]: {{ site.baseurl }}/assets/imgs/post/2016/02/step5.png
[12]: {{ site.baseurl }}/assets/imgs/post/2016/02/step6.png
[13]: {{ site.baseurl }}/assets/imgs/post/2016/02/step7.png
[14]: {{ site.baseurl }}/assets/imgs/post/2016/02/step9.png
[15]: {{ site.baseurl }}/assets/imgs/post/2016/02/step10_shapekey.png
[16]: https://drive.google.com/file/d/0B-mpivl1jPpuVzVlN3dCMXY5WmM/view?usp=sharing
