---
layout: post
title:  Rigging - Dependency cycle detected
lang: en
ref: dependency-cycle-detected
tags: [Rigging, Tuto]
permalink: /en/:year/:month/dependency-cycle-detected/
img: None_100.png
---

Hi all,  
Today, some more technical than artistic subject :)

![][1]

## Starting point

In the past few months, I started to create a new human rig, based on some mixed properties of several common human rigs. Features of this rig were not the purpose of this post (and will be detailed in another one in the future).

Fact is that my first version of the rig was totally buggy. Features were here, but some strange behaviour appears in some cases.

Some gifs are quite heavy, be patient :)

![][2]

![][3]

Please note that model used  for this rig is © 2012 by Nathan Vegdahl and The Blender Foundation, and is licensed under CC BY 3.0, and can be downloaded from Blender Cloud.


As you can see in first gif, there are some jiggles where moving some bones.

In second gif, we can see that reset default transformations of all bones of the rig need more than one iteration to be performed.


## What's wrong with this rig ?

Easiest way to find what's wrong is to look at blender console. And there :

![][4]

Some errors detected (specially when switching between pose and edit mode on armature).


## Dependency graph and dependency cycle

Ok, now, it's time to understand what's really behind these words. Dependency graph is a way to store relations between "objects" in blender. 2 "objects" (this can be objects/materials/textures/bones) are linked if some data of second object need some data from first object to be displayed (location, color, or any other data). Object 2 is linked to object 1. Dependency graph is the global graph that represent links between all data in Blender.

Here is an example that you can find in wiki.blender.org, dependency graph page :

![][5]

In this example, graph goes from "Tube" to "Scene". A dependency cycle is created when a node B is dependant of a node A, but node A is also dependent of node B (with any intermediate nodes). In example bellow, a cycle is created if "Tube" is dependant of "Plane" (because "Plane" is already dependent of "Tube".


## Some rigging examples

In following examples, I'm going to show you some dependency cycles on rigging,at bone level. Bones can be linked in 2 different ways :

*  By constraints
*  By parenting


### Example 1

In this example, ([.blend][6]), copy location is used to constraint 3 bones.

![][7]  
![][8]  
![][9]  

Result : None of bones can move !


### Example 2

In this example ([.blend][10]) , not only constraints are use to link bones, but parenting is also used. (parenting, but not connected)

![][11]  
![][12]  
![][13]  

Result when trying to move Bone.001 (on top) :

![][14]

Some weird transforms. Reset default values don't work, except if you enter into edit mode.


### Example 3

 This example ([.blend][15]) is quite similar to example 2, but using IK constraint instead of Stretch to.

Note that IK constraint seems to be applied only for 1 bone (in yellow), but all chain of this bone is constraint by IK.

![][16]  
![][17]  
![][18]  

Same result when trying to move the IK target :

![][19]  

### Example 4

 This example ([.blend][20]) is different from others, because it links bones & objects.

![][21]  
![][22]  
![][23]  

As you can see, Blender dependency graph stays at object level. That means that Armature is showed as 1 object, and another dependency graph is used inside Armature to evaluate relation between bones.

Result : Some jiggles.

![][24]  

A complete refactor of dependency graph is currently in progress, during gooseberry project. With this new version of dependency graph, granularity of "object" in main dependency graph will be go down to bones. This means that this case won't be a dependency cycle anymore, and will be represented like that :

![][25]  

### Example 5

This last example ([.blend][26]) shows some limitation of dependency cycle detection.

![][27]  
![][28]  
![][29]  

Manipulating this rig don't show us weird result, except when trying to reset default values.

![][299]  

## Debugging my rig

After these quite simple examples, back to my buggy rig ! I develop a script to be able to visualize dependency graph of my armature, using [Graphviz][30]. Here is the first picture I generate. Parenting are displayed in black, constraints on location on red, rotation on blue, and scale on green.

![][31]

First thing I can see is that in up left corner, MCH-ST and spine.def bones are quite physically separated from other part of bones. Regarding spine.def, I can see that this deformation bone is used, by constraints, to set data to other bones. This is a big mistake in my rig.


Using [this code][32], I tried to visualise the cycle in my rig (in red)

![][333]

Because I moved my bones to specific layers, my rig is quite well organized. Each bone chains are in separated layers, that's why I modified my script to group bones into layers.

![][33]

Based on all these informations, I thought about my rig features, and how to simplify my rig to reach same features, avoiding dependency cycles.


And I won :)

My new rig is now up, without dependency cycle, without any jiggles.

Here is a dependency graph of the armature :

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
