---
layout: post
title:  "10 choses à vérifier sur un Rig"
permalink: /fr/:year/:month/10-choses-a-verifier-sur-un-rig/
lang: fr
ref: 10choses_verifier_rig
tags: [Tuto, Rigging]
img: 20170503_10things.png
no_rss: false
comments: true
---

Bonjour à tous,  
Cet article présente quelques vérifications à faire lorsque l'on se trouve devant un Rig.  

Dans un premier temps, j'avais imaginé publier cette liste pour présenter toutes les vérifications que je fais lorsque je me trouve devant un Rig que je ne connais pas, et que je veux savoir s'il tient la route. Il s'agit simplement de vérifications globales, aucune fonctionnalité du rig n'est testée, et cela peut donc s'appliquer à tous les rigs (ou presque).  

Puis je me rends compte que cette liste de vérification peut également me servir pour valider la qualité lorsque je termine la construction d'un rig. Je le publie donc aujourd'hui en temps que tel, et je me réserve le droit de compléter dans le futur avec d'autres vérifications qui me viendraient à l'esprit.

* Parentage / Contraintes
  * Os Racine
    * Dans une premier temps, il faut vérifier qu'il y a bien un os root. Indispensable pour pouvoir déplacer facilement un rig dans sa globalité.  
    ![][3]  
		<br/>

    * Mise à l'échelle
    Lorsqu'on modifie le _scale_ de l'os root, le modèle ne doit pas se déformer. Sinon, c'est qu'il y a un soucis de parentage et / ou de contraintes.  
    ![][4]  
		<br/>

  * Changement _Rest Position_ / _Pose Position_
    Lorsqu'on bascule d'un mode à l'autre, on ne doit voir aucun mouvement. Sinon, c'est qu'il y a un soucis sur les contraintes et/ou les _roll_.  
    ![][5]  
		<br/>

* Cycle de dépendance
  * Lors du passage de l'armature du mode _Edit_ au mode _Pose_, puis du mode _Pose_ au mode _Edit_, il faut vérifier qu'il n'y a pas d'erreur dans la console. En effet, on peut à ce moment là voir les problèmes de cycle de dépendance. Si vous ne savez pas ce qu'est un cycle de dépendance, vous pouvez lire un de mes vieux article sur le sujet des [cycles de dépendances][1].  
	![][6]  
	<br/>

* Nom des os
  * J'utilise l'insertion d'image clés avec l'option _Whole Character_, pour vérifier si le nommage des os est correct. S'il y a des os non accessibles par l'animateur qui ont une image clé, c'est que tout les os ne sont pas nommés correctement. Si vous ne voyez pas de quoi je veux parler, vous pouvez lire mon article récent sur le mode _[Whole Character][2]_.  
	![][7]  
	<br/>

  * Je réalise ensuite une pose, et j'utilise l'outil _Mirror Pose_, afin de vérifier que la convention gauche / droite est correcte. (regardez la position des mains qui n'est pas symétrique !)  
  	![][8]<br/>	![][9]  
		<br/>

* Roll
  * Axe local des os : On vérifie par exemple que les 2 pieds ont des axes locaux identiques.  
  ![][10]<br/>	![][11]  
	<br/>

* Transformations bloqués
  * Si certaines transformations ne sont pas disponibles pour certains os, je vérifie que je ne peux pas le modifier à la main, et que je ne peux pas mettre d'image clé dessus.  
	![][12]  
	<br/>

* Skinning
  * Evidemment, je joue avec le rig pour vérifier que les déformations sont correctes :)  
	![][13]  
	<br/>

  * Je déplace l'os root très loin de sa position de base (200 unités vers le haut par exemple), et je regarde ce que cela donne ... On se rend vite compte s'il y a un soucis de skinning :)  
	![][14]  
	<br/>

* Quelques extras
	*	Link : Je regarde si tout est en place pour pouvoir utiliser le rig dans un autre fichier par l'intermédiaire d'un _link_, par opposition au _append_. Je ne vais pas détailler en détail ici, mais j'y reviendrai dans un prochain article.  
	![][15]  
	<br/>

	*	En bonus, je regarde si le rig possède des bone groups, éventuellement avec des couleurs.  
	![][16]  
	<br/>

  * De même, en bonus, en activant l'addon Selection Set, je regarde s'il y a des entrées crées.  
	A noter que je développe actuellement un addon, [ExtraGroups][18], qui va beaucoup plus loin dans la gestion des os. Cet addon sera disponible avant l'été 2017.  
	![][17]  
	<br/>

La modélisation et le rig utilisé est copyright Blender Foundation, martyrisé par mes "soins" ;-)  

Voici une vidéo qui reprend tous ces éléments :  
{% include youtube.html id='TpzYlwJF_Hc' %}


[1]: {{ site.baseurl }}/fr/2014/12/detection-cycle-de-dependance/
[2]: {{ site.baseurl }}/fr/2017/02/utiliser-keyingset-whole-character/
[3]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/01_root.png
[4]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/02_scale.png
[5]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/03_rest_pose.png
[6]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/04_depcycle.png
[7]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/05_bone_names.png
[8]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/06_pose_1.png
[9]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/06_pose_2.png
[10]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/07_foot_1.png
[11]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/07_foot_2.png
[12]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/08_transformation.png
[13]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/09_pose.png
[14]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/10_skinning.png
[15]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/11_linking.png
[16]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/12_bone_groups.png
[17]: {{ site.baseurl }}/assets/{{ page.assets }}imgs/post/2017/05/13_selection_set.png
[18]: http://BleRiFa.com/fr/tools/ExtraGroups/
