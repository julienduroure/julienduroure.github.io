---
layout: post
title:  Utiliser les fonctions "Clean Keyframes" et "Clean Channels"
lang: fr
ref: using_clean_keyframes_clean_channels
tags: [Tuto, Animation]
permalink: /fr/:year/:month/utiliser-les-fonctions-clean-keyframes-et-clean-channels/
redirect_from:
  - /2015/08/utiliser-les-fonctions-clean-keyframes-et-clean-channels/
img: 20150826_using_clean_keyframes_clean_channels.png
---

Bonjour à tous,  
Comme évoqué dans [cet article][99], la version 2.75a a vu apparaître, dans le dopesheet et le graph editor, une entrée "Clean Keyframes" dans le menu de suppression "X".

![][1]

J'aimerai revenir sur son fonctionnement à travers un exemple.

A partir du cube de la scène par défaut, j'enregistre les positions clés suivants :  

*  image 1 : LocRotScale, afin d'enregistrer la position, rotation, et mise à l'échelle ( I )
*  image 5 : Je déplace le cube sur l'axe Y, et j'enregistre la position à l'aide de Location ( I )
*  image 10 : Je déplace le cube, de nouveau sur l'axe Y, et j'enregistre la position.
*  image 15 : J'enregistre de nouveau la position, sans avoir déplacé le cube.
*  image 20 : Je déplace le cube sur l'axe Y, et j'enregistre la position
*  image 25 : J'enregistre la position, sans avoir déplacé le cube

Dans le Graph Editor, je peux donc voir les courbes suivantes :

![][2]

On observe nettement la courbe de position sur l'axe Y, en vert. Mais on peut également voir les courbes concernant la mise à l'échelle, à 1. On peut voir une seule image clé, sur l'image 1.

Les courbes de rotation sont aussi présentes, superposées aux courbes de position sur l'axe X et Z, ayant la valeur 0.

![][3]

Voyons maintenant le fonctionnement de l'outil Clean Keyframes (à utiliser, donc, à l'aide de la touche X dans le Graph Editor ou le Dopesheet. Voici les nouvelles courbes disponibles dans le Graph Editor. Il faut penser à sélectionner tout d'abord l'ensemble des points, à l'aide de la touche A, afin que l'outil s'applique sur l'ensemble de notre animation.

![][4]

On peut remarquer :

*  La clé, en image 25, sur l'axe Y, a été supprimée. En effet, elle n'était pas nécessaire pour définir le mouvement du cube sur cet axe, les 2 valeurs, en image 20 et 25, étaient identiques. On remarque que l'outil n'a pas supprimée l'une ou l'autre des clés en image 10 et 15, même si leurs valeurs étaient identiques, car cela aurait modifié l'interpolation de la courbe.

*  Les courbes de position sur les axes X et Z ont été complètement nettoyées, puisque seule une image clé est maintenant présente. Auparavant, l'ensemble des points avaient des valeurs identiques.

*  Il en est de même pour les trois courbes de mise à l'échelle.

On peut se demander pourquoi garder des courbes pour les 3 axes de mise à l'échelle, les 3 axes de rotation, et les 2 axes de position X et Z ? En effet, les courbes ne possèdent qu'une seule image clé, signifiant que les valeurs ne changent pas dans le temps (les courbes n'ayant pas de _modifier_, pour les puristes).

C'est justement l'objet de l'outil _Clean Channels_, qui fera sont apparition dans la version 2.76.

![][5]

Cet outil fonctionne exactement de la même manière que l'outil _Clean Keyframes_, mais supprime également toutes les courbes n'ayant qu’une seule image clé à l'issu de l'opération de nettoyage des images clés. Voici ce que cela donnera sur l'exemple du cube. On remarque qu'effectivement, sur la gauche de l'écran, que l'animation n'a plus qu'une seule courbe.

![][6]

Voyons maintenant l'impact que ces deux outils peuvent avoir sur une scène de production. Je vais utiliser pour cela une scène d'animation du Rig suivant, donc j'aurai l'occasion de vous reparler.

![][7]

L'animation est au stade de blocking primaire. La scène est longue de 385 images, soit 16 secondes environs.

![][8]

A l'aide du script dans les sources sont disponibles en fin d'article, je compte la totalité des courbes et images clés enregistrées pour le rig.

Puis j'applique les outils _Clean Keyframes_ et _Clean Channels_, afin de mesurer dans quelles mesures l'animation a été simplifiée.

![][9]

|                                    | Courbes      | Image clés |
|------------------------------------|:------------:|:----------:|
| Initial                            | 9223         | 543550     |
| Après "Clean Keyframes"            | 9223         | 11061      |
| Après "Clean Channels"             | 203          | 2041       |
{: class="pure-table pure-table-bordered"}

<br/>
On remarque qu'effectivement, la scène avait besoin d'un grand nettoyage !

> import bpy
>
> ob = bpy.context.active_object
>
> print("fcurves : " + str(len(ob.animation_data.action.fcurves)))
>
> keyframes = 0
>
> for fcurve in ob.animation_data.action.fcurves:
>
> keyframes = keyframes + len(fcurve.keyframe_points)
>
> print("keyframes : " + str(keyframes))

[1]: {{ site.baseurl }}/assets/imgs/post/2015-08/clean_keyframes.png
[2]: {{ site.baseurl }}/assets/imgs/post/2015-08/clean_before.png
[3]: {{ site.baseurl }}/assets/imgs/post/2015-08/clean_before_detail_fr.png
[4]: {{ site.baseurl }}/assets/imgs/post/2015-08/clean_after.png
[5]: {{ site.baseurl }}/assets/imgs/post/2015-08/clean_channels.png
[6]: {{ site.baseurl }}/assets/imgs/post/2015-08/clean_channels_after.png
[7]: {{ site.baseurl }}/assets/imgs/post/2015-08/rig_spider.png
[8]: {{ site.baseurl }}/assets/imgs/post/2015-08/before_.png
[9]: {{ site.baseurl }}/assets/imgs/post/2015-08/after_.png
[99]: {{ site.baseurl }}/fr/2015/07/2-74-2-75-les-nouveautes-rigging-animation/
