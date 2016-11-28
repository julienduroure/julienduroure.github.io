---
layout: post
title:  Utiliser l'outil "Propagate"
lang: fr
ref: using_propagate
tags: [Tuto, Animation]
permalink: /:year/:month/utiliser-l-outil-propagate/
img: 20150826_using_propagate.png
comments: true
---

Bonjour à tous,  
Dans un précédent article concernant les [nouveautés des versions 2.74 & 2.75][1], j'ai évoqué une amélioration de l'outil _Propagate_.

J'ai eu depuis plusieurs demandes de clarification à propos de cet outil.

![][2]

L'outil s'utilise principalement lors des phases de _blocking_. Il permet, dans certains conditions, de modifier en masse des images clés.

Prenons l'exemple d'un cycle de marche pour expliquer son fonctionnement. On remarque plusieurs phases dans l'animation du pied :

* Le _contact_, où le pied est posé au sol, et il existe plusieurs images clés identiques consécutives.
* Le _passing_, où le pied est en l'air, et avance jusqu'à sa position de contact suivant (le pas suivant)

![][3]

## Propagate Pose

Lors des phases de _blocking_, il est souvent nécessaire de réajuster les positions des différents os. Prenons ici l'exemple du pied : L'animateur décide que sa position au niveau du contact n'est pas idéale, il faut donc la modifier. Pour une meilleure visibilité des courbes, je règle, pour les besoins de cette démo, les courbes en mode Bézier, bien qu'étant en phase de _blocking_.

On se positionne donc sur la première image clé du contact (au moment du contact avec le sol), et on déplace le pied, dans la vue 3D, jusqu'à obtenir la position corrigée. Pour éviter tout glissement du pied entre cette image clé et les suivantes, il faut également ré-ajuster toutes les images clés du contact.

Au lieu de copier/coller l'image clé corrigée sur les suivantes (les 5 autres images clés où le pied est au contact du sol), nous allons utiliser l'outil _propagate_.

Avant de sauvegarder la nouvelle image clé (à l'aide de la touche _I_), on utilise _Propage_ (à l'aide du raccourci _Alt + P_) dans la vue 3D, ou bien dans le menu _Pose_, toujours dans la vue 3D.

![][4]

Comme on peut le voir dans le _graph editor_, les images clés correspondant au contact du sol ont été modifiées, et c'est maintenant la nouvelle position du pied qui est enregistré. Voici le détail de ce qui a été réalisé par l'outil :

* L'outil calcule quelles sont les images clés suivantes qui ont exactement la même position que l'image courante enregistrée (donc avant la modification que l'on vient de faire). Dans notre cas, l'image courante est la 1ère au contact du sol (trait vert vertical). Les 5 images clés suivantes sont identiques à l'image courante.
* Sur l'image courante, l'outil enregistre la nouvelle position du pied.
* Sur les images clés qui ont été sélectionnées à l'étape 1, l'outil enregistre également la nouvelle image clé, donc la nouvelle position du pied.
* L'outil s'arrête dès que l'image clé suivante (l'image clé suivant la parte d'appui) n'est plus identique à la précédente.

_NB_ : Il est important, pour que l'outil fonctionne, qu'il n'y ait pas d'enregistrement automatique des images clés.

![][5]

Sinon, dès qu'on déplace le pied sur l'image clé du contact avec le sol, la nouvelle position est enregistrée, et l'image clé suivante est considérée comme différente, et l'outil ne s'applique donc pas.

_NB2_ : Pour tester si 2 images clés sont identiques, l'outil prend en compte l'ensemble des canaux de l'os (position, rotation, mise à l'échelle), et non pas uniquement ceux affichés dans le _Graph Editor_. Dans notre exemple, on voit que la position Y du pied est bien identique. Mais puisque l'outil s'est appliqué l'ensemble des images clés correspondant au contact avec le sol, c'est que la rotation, la mise à l'échelle, et la position X et Z du pied sont également identiques.

## Last Keyframe

Voyons maintenant un autre cas où cet outil est utile. Toujours dans le cadre d'un cycle de marche, mais cette fois-ci au niveau de la hanche. On a ici un mouvement cyclique. On a donc la première image clé qui est identique à la dernière image clé de l'action.

Imaginons maintenant qu'il faille modifier la rotation de la hanche sur la première image clé.

La solution "à la main" :

* On corrige la rotation, puis on insère une image clé pour corriger la première image clé. Avec le modificateur _Cyclic_ sur la courbe, on remarque un décallage au niveau de la jointure de chaque cycle.

![][6]

* Il faut donc copier/coller la nouvelle image clé sur la dernière du cycle.

On peut réaliser ces opérations plus rapidement grâce à _Propagate to Last Keyframe_: On change la rotation de la hanche, on enregistre la nouvelle image clé, et on applique l'outil.

On voit que la dernière image clé est modifiée automatiquement sans avoir besoin de se déplacer jusqu'à celle-ci.

![][7]

_NB_ : cette fois-ci, il faut bien enregistrer l'image clé avant d'appliquer l'outil

## To next Keyframe

Cette fois-ci, le comportement est un peu différent puisqu'il permet de modifier uniquement l'image clé suivante. L'outil réagit différemment si une image clé existe sur l'image, ou non.

* Si une image clé existe, alors la nouvelle position est enregistrée, et c'est tout. Cela revient au même que de faire _Insert Keyframe_ (raccourci _I_). Donc aucun intérêt :)
* Si aucun image clé n'existe sur l'image courante, alors la pose courante est enregistrée sur la prochaine image clé existante.

## On selected keyframe

Il s'agit, pour cette option, de copier automatiquement la position courante vers un certain nombre d'images préalablement sélectionnées.

Par exemple, avant modification :

![][8]

Puis je déplace le pied, et j'active l'outil avec l'option _On selected keyframe_

![][9]

Là encore, on remarque que l'image courante n'est pas modifiée, il faut en plus enregistrer l'image avec _I_.


## On selected markers

Cela fonctionne comme pour _On selected Keyframes_, mais prend en compte les marqueurs sélectionnés, au lieu des images clés sélectionnées.

![][10]

## Conclusion

Voici pour ce tour d'horizon de l'outil _Propagate._ Comme vous avez pu le remarquer, il n'est pas forcement facile de le prendre en main. Je trouve que les différentes options sont assez différentes les uns des autres, et surtout, ne réagissent pas de la même manière sur l'enregistrement de l'image courante ( On ne doit pas enregistrer l'image courante avant _Propagate Pose_, qui s'en occupe, mais il faut le faire pour les autres options).

[1]: {{ site.baseurl }}/fr/2015/07/2-74-2-75-les-nouveautes-rigging-animation/
[2]: {{ site.baseurl }}/assets/imgs/post/2015/09/menu.png
[3]: {{ site.baseurl }}/assets/imgs/post/2015/09/movment_FR.png
[4]: {{ site.baseurl }}/assets/imgs/post/2015/09/propagate_pose.png
[5]: {{ site.baseurl }}/assets/imgs/post/2015/09/auto_insert.png
[6]: {{ site.baseurl }}/assets/imgs/post/2015/09/hips_KO.png
[7]: {{ site.baseurl }}/assets/imgs/post/2015/09/last_kekyframe.png
[8]: {{ site.baseurl }}/assets/imgs/post/2015/09/selected_before.png
[9]: {{ site.baseurl }}/assets/imgs/post/2015/09/on_selected_after.png
[10]: {{ site.baseurl }}/assets/imgs/post/2015/09/selected_markers.png
