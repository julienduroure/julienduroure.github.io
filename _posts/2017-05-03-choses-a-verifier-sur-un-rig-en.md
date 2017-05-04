---
layout: post
title:  "10 checks to perform on Rigs"
permalink: /en/:year/:month/10-checks-on-rigs/
lang: en
ref: 10choses_verifier_rig
tags: [Tuto, Rigging]
img: 20170503_10things.png
no_rss: false
comments: true
---

Hi there :)  
This post is about checks that need to be done on Rigs.  

In a first step, I planned to publish a list of checks to be done when I discover a new Rig, and I want to know the rig quality. This list is quite global, and can be applied on (almost) any rig.  
Then I realised that this list can be used as a check-list before deliver a rig. I'm publishing this list here, and I will eventually update it if I want / need.  

* Parent / Constraint
  * Root
    * First step : verify that there is a root bone. Essential to grab entire rig.  
    ![][3]  
		<br/>

    * Scaling  
    When scaling root bone, model should scale uniformally, without deforming some part of the mesh. Otherwise there is a problem of parent or constraint.  
    ![][4]  
		<br/>

  * Change _Rest Position_ / _Pose Position_  
    When switching from one to other, no mouvement should be noticed, except if there is some _roll_ or constraint error.  
    ![][5]  
		<br/>

* Dependency cycle
  * When you switch armature from _Edit Mode_ to _Pose Mode_, verify console error. If there are some dependency cycles, some errors will be displayed. If you don't know what is a dependency cycle, you can read an old post about [dependency cycle][1]  
  ![][6]  
	<br/>

* Bone naming
  * I am using keyingset _Whole Character_ to check bone naming. If some animator unused bone have a keyframe, some bones are not correctly named. If you don't know what I mean, please have a look on my post about _[Whole Character][2]_.  
  ![][7]  
	<br/>   

  * I pose the rig, and using _Mirror Pose_, I check that Right / Left convention is OK. (look at hand position this is not symmetrical in example)  
  ![][8]<br/>	![][9]  
  <br/>

* Roll
  * Bone Local axis : Check, for example, that both feet have identical local axis.  
  ![][10]<br/>	![][11]  
	<br/>

* Locked transformations
  * If some transformations are not available for some bones, I check that these transformations are locked (so no keyframe on it)  
  ![][12]  
  <br/>

* Skinning
  * Time to play with the rig to check deformations :)  
	![][13]  
	<br/>

  * Moving root bone far away of world center (200 units up for example), and see ... Quickly noticed any problems :)  
	![][14]  
	<br/>

* Extras
  * Link: I check that all is OK in order to using my rig in another file, using _link_ system. No details on it here, I will write another post about this particular point.  
  ![][15]  
	<br/>

	*	Bonus: I check if rig has bone groups, with color eventually.  
	![][16]  
	<br/>

  * Bonus again, activating addon _Selection Set_, I check if there is some entries.  
	Note that I am currently developping an addon, [ExtraGroups][18], that enhance Selection Sets. This addon will be available before summer 2017.  
	![][17]  
	<br/>

Model & Rig used is from Blender Foundation, destroyed by myself :)

Here is a (french) video about all these checks:  
{% include youtube.html id='TpzYlwJF_Hc' %}


[1]: {{ site.baseurl }}/en/2014/12/dependency-cycle-detected/
[2]: {{ site.baseurl }}/en/2017/02/using-keyingset-whole-character/
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
[18]: http://BleRiFa.com/en/tools/ExtraGroups/
