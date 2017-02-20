---
layout: post
title:  "KeyingSet : Whole Character"
permalink: /fr/:year/:month/utiliser-keyingset-whole-character/
lang: fr
ref: keyingset_whole_character
tags: [Tuto, Rigging]
img: 20170220_Whole_Character.png
no_rss: false
comments: true
---

Bonjour à tous,  
Dans cet article, je vais vous présenter l'option "_Whole Character_" des _KeyingSets_.  

Quand on anime un personnage riggé (et encore plus lors de la phase de blocking), il peut être intéressant d'ajouter des _Keyframes_ sur l'ensemble des os du perso. Mais ... cela nous intéresse uniquement pour les os (et leurs propriétés) qui sont animable par l'animateur. Sinon, on va se retrouver avec des _f-curves_ inutiles.  

C'est là qu'intervient l'option _Whole Character_. Plutôt que de construire un _KeyingSet_ spécifique, on peut donc utiliser cette option. Une astuce (non documentée dans la [doc officielle][1]), permet justement d'éviter de créer des clés d'animation sur les os non souhaités. Cela se passe au niveau du nom de l'os.  
Tous les os commençant par :  

*	DEF  
*	GEO  
*	MCH  
*	ORG  
*	COR  
*	VIS  

ne seront pas pris en compte. Tous les autres os le seront (même s'ils sont masqués ou sur un calque non affiché). A noter que les transformations _lockées_ ne sont pas prises en compte non plus. Pour les propriétés des os, par défault, toutes les propriétés sont prises en comptes.  
On peut retrouver cette liste (et donc éventuellement trouver le fichier à modifier pour compléter/modifier la liste), directement dans le code source, en allant voir le [commit suivant][2].  

Je vous propose de regarder tout ça en vidéo :  
{% include youtube.html id='FSfSpEnbVvQ' %}



[1]: https://www.blender.org/manual/animation/keyframes/keying_sets.html
[2]: https://developer.blender.org/rB1439ebb6b1091c0bc976480ec1751966395b2755
