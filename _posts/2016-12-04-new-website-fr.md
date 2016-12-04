---
layout: post
title:  "Nouveau site"
permalink: /en/:year/:month/nouveau-site/
lang: fr
ref: new-website
tags: [Website]
img: 20161204_newsite.png
comments: true
---

Voici une nouvelle version de mon site !  
Cette année, j'ai eu pas mal de soucis de piratage avec la version précédente ([Wordpress][1]) de mon site...

J'ai donc décidé de le migrer sous [Jekyll][2] : plus de problèmes, que du contenu statique !  
C'est également plus facile pour moi de maintenir le site et d'écrire de nouveaux articles.  
J'espère que vous l'aimez :)

Niveau contenu, pas de grand changement (pour le moment) avec le "vieux" site :  

*  [Une description rapide de mes compétences / centre d'intérêt][3] (Rigging, Animation, Développement, Formation)
*  [Un blog avec des articles autour de la 3D, et de Blender évidemment][4]
*  Un lien vers [BleRiFa][5], un site qui rassemble les développements d'addons que je réalise
*  Comment [me contacter][6] si vous souhaitez travailler avec moi

# Quoi de neuf ?

*  Un nouveau lien pour le [flux RSS][7], pensez à mettre à jour ;-)  
*  Souscrivez à la _Newsletter_, (en bas de cet article), ne ratez plus aucune info
*  Dans le [blog][4], les articles provenant de [BleRiFa][5] apparaissent aussi

A bientôt !

[1]: http://fr.wordpress.org
[2]: https://jekyllrb.com
[3]: {{ site.baseurl }}{{ site.data.trad["service_url"][page.lang] }}
[4]: {{ site.baseurl }}{{ site.data.trad["blog_url"][page.lang] }}
[5]: http://BleRiFa.com/fr/
[6]: {{ site.baseurl }}/fr/about/
[7]: {{ site.baseurl }}/feed_fr.xml
