---
layout: post
title:  "KeyingSet : Whole Character"
permalink: /en/:year/:month/using-keyingset-whole-character/
lang: en
ref: keyingset_whole_character
tags: [Tuto, Rigging]
img: 20170220_Whole_Character.png
no_rss: false
comments: true
---

Hi all,  
In this post, I will present you _Whole Character_ option of _KeyingSet_.

When you animate a rigged character (and even more during blocking step), you need to insert keyframes on all character bones. But ... it is really needed only on bones (and corresponding properties) that are animable by animators. Otherwise you will get lots of unused _F-curves_.

Here is _Whole Character_ option usefull. Instead of creating a user specific _KeyingSet_, you can use this option. A tips that is not documented in [official documentation][1] is used to avoid creating keyframes on unneeded bones. (Based on bone name).  
All bone names started with :  

*	DEF  
*	GEO  
*	MCH  
*	ORG  
*	COR  
*	VIS  

are not taken into account. Other ones will be (even if they are hidden, or on a non displayed layer. Note that locked transformations will be not taken into account too. For bone properties, all properties are keyframed.  
You can find this list (and source file to modify if you want to add/modify) directly on source code, regarding this [commit][2].

Here is a (french) video explaining this :   
{% include youtube.html id='FSfSpEnbVvQ' %}



[1]: https://www.blender.org/manual/animation/keyframes/keying_sets.html
[2]: https://developer.blender.org/rB1439ebb6b1091c0bc976480ec1751966395b2755
