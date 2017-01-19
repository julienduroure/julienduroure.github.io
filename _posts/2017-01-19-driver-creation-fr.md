---
layout: post
title:  "Les drivers dans la version 2.78"
permalink: /fr/:year/:month/les-drivers-dans-la-version-2-78/
lang: fr
ref: drivers_2_78
tags: [Tuto, Rigging]
img: 20170119_drivers.png
no_rss: false
comments: true
---

Bonjour à tous,  
Dans cet article, je vais revenir sur les améliorations de la version 2.78 concernant les _drivers_.

### Création des drivers avec la pipette

![drivers]({{ site.baseurl }}/assets/imgs/post/2016/09/drivers.png)

La création des drivers est facilitée :  

* On peut maintenant utiliser Ctrl+D sur la propriété sur laquelle on souhaite rajouter un driver.
* Une pop-up nous permet de choisir le mode de création du _driver_ :
  * __All from Target__ rajoutera un driver sur toutes les composantes de la propriété (par exemple, position X, Y, et Z) en prenant pour référence une seule valeur, définie à la prochaine étape.
  * __Single from Target__ rajoutera un driver sur une seule composante de la propriété (par exemple, la rotation Y).
  * __Match Indices__ rajoutera un driver pour chaque composante de la propriété, en se basant sur chaque composante de la source (si celle-ci possède le même nombre de composantes (position X, Y, Z vers rotation X, Y, Z par exemple).
  * __Manually Create Later__ correspond à l'action _Add driver_ présente dans la version 2.77. Un driver est créé pour l'ensemble des composantes, mais les informations doivent être renseignées dans le _Graph Editor_ car elles ne sont pas initialisées.
  * __Manually Create Later (Single)__ correspond à l'action _Add single driver_ présente dans la version 2.77. Un driver est créé pour une seule composante, mais il faut ensuite renseigner les informations dans le _Graph Editor_, car elle ne sont pas renseignées automatiquement.

Des variables de type _Transform Channel_ sont créées pour toutes les propriétés de transformation. Les autres propriétés créent des variable de type _Single Property_.
On peut voir aussi qu'une convertion radian/degré est automatiquement ajoutée pour les rotations.

Voici une vidéo qui reprend tous ces modes de création (après une rapide introduction sur ce qu'est un driver):  
{% include youtube.html id='zBsW_QDd6ms' %}
<br/>
<br/>

### Keyframes pour la correction des drivers

Jusqu'à la version 2.77, lorsqu'on ajoute une _keyframe_ sur une propriété ayant un driver, cela rajoute une nouvelle _F-curves_, qui n'est jamais prise en compte. On voit donc de nouvelles _Keyframes_ dans la _Timeline_, mais elles n'ont aucun effet sur l'animation... Ce qui est assez perturbant.  
Dans la version 2.78, les nouvelles _Keyframes_ sont rajoutées directement dans la _F-curve_ du _driver_. Il est donc plus facile de créer des corrections sur ces _drivers_ (même s'il faut désactivé le _driver_ pour rajouter les _keyframes_).  
Tout ceci est expliqué dans la vidéo suivante :  
{% include youtube.html id='GfFPue6RAec' %}
