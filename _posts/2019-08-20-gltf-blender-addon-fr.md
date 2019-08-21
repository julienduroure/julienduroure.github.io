---
layout: post
title:  "Blender and glTF2.0"
permalink: /fr/:year/:month/blender-et-gltf/
lang: fr
ref: gltf_blender
tags: [Development]
img: 20180610_gltf.png
comments: true
---

Bonjour à tous,

Voilà presque un an maintenant que j'ai posté sur ce site un [premier message concernant le format glTF2.0][1]. Les choses ont bien évoluées depuis, et je vais donc, dans ce second article, parler de l'année qui vient de s'écouler, et des perspectives pour le futur.

# glTF

Peut être que quelques précisions s'imposent pour ceux qui ne connaissent pas ce que c'est...  

glTF est une spécification libre de format de fichier servant au transfert de données 3D. Pour ceux qui souhaitent avoir des détails précis, je peux vous renvoyer vers le [site official de glTF][2], ainsi que vers la [spécification du format][3].  

En quelques mots, glTF permet le transfert de :

* Objets, avec liens de parenté
* Maillage
* ShapeKeys (Morphing)
* Rigging & Skinning
* Animation:
  * d'objets
  * de rig
  * de shapekeys
* de Matériaux PBR

# Intégration de Blender

Les choses ont bien changé depuis l'année dernière. Après quelques jours à développer mon addon d'import de fichier glTF dans Blender pour le compte d'Airbus Defence & Space (principalement la hiérarchie d'objets et le maillage), j'ai poursuivi le développement de manière bénévole pour en faire un addon le plus complet possible.
Durant le printemps 2018, j'ai été contacté par [Khronos][4], le consortium à l'origine du format glTF. Ils m'ont alors proposé d'unir mes travaux et les travaux réalisés sur l'export depuis Blender vers glTF (travaux réalisés par la société UX3D). Depuis juillet 2018, donc, je continue mes travaux sur le github de l'[importeur / exporteur glTF pour Blender][5].
Peu de temps après la [Blender Conference 2018][6], où j'ai pu discuter avec l'équipe de développement, cet addon a été intégré directement à Blender, et activé par défaut. Depuis novembre 2018, le développement, qui a toujours lieu sur github, est répliqué sur le dépot de Blender.
Depuis, je continue à maintenir sur mon temps libre la partie _import_ de l'addon. La partie _export_ étant, dans un premier temps toujours maintenu par UX3D. A l'heure actuelle, UX3D ayant terminé son contrat avec Khronos, ils ne participent plus au développement de l'addon. Ce qui fait de moi le contributeur le plus actif, pour l'import et pour l'export.

# D'un point de vue utilisateur

Pour préparer ma [conférence au GrafikLabor][7], je me suis placé en temps qu'utilisateur, et j'ai pu constaté que beaucoup de choses ne fonctionnaient pas (encore). Le socle du code est en place, mais de nombreux détails restent à mettre en place. Le cas de figure le plus courant (rig complexe, plusieurs animations différentes dans le NLA), ne fonctionne tout simplement pas.

Parmi les choses qui ne fonctionnent pas correctement, ou de manière incomplète, au moment du GrafikLabor, et sur lesquels j'ai prévu de travailler par la suite, on peut trouver:
* L'animation de certains index uniquement (l'axe X uniquement, par exemple)
* Les rigs complexes, c'est à dire os avec contraintes
* L'export de plusieurs animations différentes
* L'animation des shapekeys via drivers

Il s'agit bien sûr d'une liste non exhaustive, mais il s'agit pour moi du strict minimum pour avoir un exporteur opérationnel (d'un point de vue rig/anim).

# 0 A.D.

J'ai eu l'occasion de rencontrer plusieurs membres actifs du jeu [0 A.D.][8], et on a même eu l'occasion de se faire une lan-party, lors du GrafikLabor.
Actuellement, le jeu utilise le format Collada pour exporter les assets depuis Blender vers leur moteur de jeu. Après discussion, l'équipe sera prête, à moyen terme, à changer leur pipeline pour utiliser glTF à la place de Collada, ce qui est une évolution logique, Collada étant un format dont la norme n'est plus suivi par KhronosGroup, les efforts étant maintenant portés sur glTF. Je me suis donc porté volontaire pour les accompagner dans cette démarche, pour tout ce qui concerne la norme glTF elle-même, ainsi que pour le maintien de l'exporter Blender.

# Khanagat

J'ai également rencontré lors du GrafikLabor une partie de l'équipe de [Khanagat][9], qui compte aussi regarder du côté du glTF pour leur jeu.

# Blender 2.80

Il y a quelques semaines, la version 2.80 de Blender est sortie. Elle contient donc l'importer/exporter glTF actif par défaut. C'est une étape importante, mais ce n'est pas un aboutissement : beaucoup de travail reste à faire sur l'addon.

# Et après ?

Le travail va continuer. En plus de la gestion des bugs, je compte travailler plus particulièrement sur l'export d'animation, qui manquent d'options et de maturité. Dans un deuxième temps, il faudra faire un gros travail sur les performances. Toutes les personnes volontaires sont bien sûr bienvenues :)


[1]: http://julienduroure.com/fr/2018/06/blender-gltf-importer/
[2]: https://www.khronos.org/gltf/
[3]: https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md
[4]: https://www.khronos.org
[5]: https://github.com/KhronosGroup/glTF-Blender-IO
[6]: https://www.blender.org/conference/2018/
[7]: https://afgral.org/grafiklabor-2019
[8]: https://play0ad.com/
[9]: https://khaganat.net/
