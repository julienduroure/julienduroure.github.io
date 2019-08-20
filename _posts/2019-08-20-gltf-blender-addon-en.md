---
layout: post
title:  "Blender and glTF2.0"
permalink: /en/:year/:month/blender-and-gltf/
lang: en
ref: gltf_blender
tags: [Development]
img: 20180610_gltf.png
comments: true
---

Hello everyone,

It's almost a year now that I posted on this site a [first blogpost regarding the glTF2.0 format][1]. Things have changed a lot since then, so I'm going to talk in this second article about the past year and the prospects for the future.

# glTF

Maybe some clarification is needed for those who do not know what it is ...

glTF is a free file format specification for 3D data transfer. if you want more information, you can go to the [official website of glTF][2], as well as to the [format specification][3].

In a few words, glTF allows the transfer of:

* Objects, with tree parenting
* Mesh
* ShapeKeys (Morphing)
* Rigging & Skinning
* Animation of:
  * objects
  * rigs
  * shapekeys
* PBR Materials

# Blender integration

Things have changed a lot since last year. After a few days developing my glTF file import addon in Blender for Airbus Defense & Space (mainly object hierarchy and mesh), I continued the development on a volunteer basis to make it an addon as complete as possible.
During the spring of 2018, I was contacted by [Khronos][4], the consortium behind the glTF format. They then proposed me to join my effort work and the work carried out on the export since Blender towards glTF (work carried out by the company UX3D). Since July 2018, therefore, I continue my work on the github of [importer / exporter glTF for Blender][5].
Shortly after the [Blender Conference 2018][6], where I was able to chat with the development team, this addon was integrated directly into Blender, and enabled by default. Since November 2018, the development, which always takes place on github, is replicated on the git repository of Blender.
Since then, I continue to maintain in my spare time the _import_ part of the addon. The _export_ part being, in a first time, always maintained by UX3D. At the moment, UX3D having concluded its contract with Khronos, they no longer participate in the development of the addon. Which makes me the most active contributor, for import and for export.

# From a user point of view

To prepare my [GrafikLabor conference][7], I placed myself as a user, and I could see that many things were not working (yet). The base of the code is in place, but many details remain to be put in place. The most common scenario (complex rig, several different animations in the NLA), just does not work.

Among the things that do not work properly, or incompletely, at the time of the GrafikLabor, and on which I planned to work afterwards, we can find:
* Animation of some indexes only (X axis only, for example)
* Complex rigs, ie bones with constraints
* The export of several different animations
* The animation of shapekeys via drivers

This is of course a non-exhaustive list, but it is for me the bare minimum to have an operational exporter (from a rig / anim point of view).

# 0 A.D.

I had the opportunity to meet several active members of the game [0 AD][8], and we even had the opportunity to have a lan-party at the GrafikLabor.
Currently, the game uses the Collada format to export the assets from Blender to their game engine. After discussion, the team will be ready, in the medium term, to change their pipeline to use glTF instead of Collada, which is a logical evolution, Collada being a format whose standard is no longer followed by KhronosGroup, efforts are now focused on glTF. So I volunteered to support them in this process, for all that concerns the standard glTF itself, as well as for maintaining the export Blender.

# Khanagat

I also met at GrafikLabor part of the team of [Khanagat][9], which also intends to look for the glTF for their game.

# Blender 2.80

A few weeks ago, version 2.80 of Blender was released. It therefore contains the import / export glTF active by default. This is an important step, but it is not a culmination: a lot of work remains to be done on the addon.

# And after ?

The work will continue. In addition to bug management, I intend to work more specifically on animation export, which lack options and maturity. In a second time, it will take a lot of work on performance. All volunteers are of course welcome :)

[1]: http://julienduroure.com/en/2018/06/blender-gltf-importer/
[2]: https://www.khronos.org/gltf/
[3]: https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md
[4]: https://www.khronos.org
[5]: https://github.com/KhronosGroup/glTF-Blender-IO
[6]: https://www.blender.org/conference/2018/
[7]: https://afgral.org/grafiklabor-2019
[8]: https://play0ad.com/
[9]: https://khaganat.net/
