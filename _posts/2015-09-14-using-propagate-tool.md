---
layout: post
title:  Using "Propagate" tool
lang: en
ref: using_propagate
tags: [Tuto, Animation]
permalink: /:year/:month/using_propagate-tool/
img: 20150826_using_propagate.png
---

Hi there,  
In a previous post ([What's new in 2.74 & 2.75][1]) , I talked about _Propagate_ tool.

I had few questions from readers about this tool, so here are some details about it:

![][2]

This tool is usefull during blocking step of animation. We are able to modify many keyframes in only one step.

Here is an exemple about Walk Cycle. We can see 2 phases during animation of the foot:

* _contact_, where foot is on the ground. There are some adjacent identical keyframes.
* _passing_, where foot is moving forward, until it touches ground again.

![][3]

## Propagate Pose

During _blocking_, we have to tweak position of bones. About foot: Animator can decide to change position of the foot during contact. For a better visiblity during this example, I set curves in Bezier mode, even if this is a blocking stage.

We move current frame in order to have current frame on first keyframe with foot on ground, we adjust position of the foot until it seems to be OK. In order to avoid sliding, we have to correct any keyframes that are during contact.

Instead of copy/paste new keyframe on next 5 keyframes (where foot is on the ground), we are going to use _Propagate_ tool.

Before inserting keyframe on current frame (with keyboard _I_), we use shortcut Alt+P in 3D view, or in menu Pose (in 3D view too).

![][4]

As we can see on screenshot of _Graph Editor_, all keyframes of contact phase has been modified, and this is now the new foot position that is saved. Here is a detail steps of what the tool did:

* Tool compute all next keyframes to find what are keyframes with exactly same position than keyframe of current frame (so before I moved the foot). In this example, current frame is first frame of contact, and next 5 keyframes are identical.
* In current frame, the tool insert keyframe to save new position of the foot.
* On keyframes selected on step 1, the tool insert keyframes, so all these keyframe have new position.
* The tool stops when next keyframe is no more identical to previous one.

_NB_ : It is important that auto-keyframe is not enabled in order to use this tool.

![][5]

_NB_ :If auto-keyframing is enable, when we moved the foot, a new keyframe is inserted, and next keyframe is now different from current keyframe, so the tool don't apply._NB2_ : In order to test if 2 keyframes are identical, the tool take into account all channels, not only fcurve displayed on _Graph Editor._ In the example we can see that Y location are identical. Because the tool applied on next 5 keyframes, that means that rotation, scale, and X and Z location are identical too.

## Last Keyframe

Here is another example of using Propagate, with &#8220;Last Keyframe&#8221; option. : Walk cycle too, but on hips, we have a cyclic movment. The first keyframe is identical to last frame.

Imagine that we want to modify rotation of hips on first keyframe.

Here is how to process by hand:

* We modify the rotation, and insert keyframes, on first keyframe. With cyclic modifier on cruve, we can see a break into curve at junction between 2 cycles.

![][6]

* We need to copy/paste this new keyframe on last keyframe of cycle.

We can go faster, using _Propagate to Last Keyframe : We modify hips rotation on first keyframe, insert keyframes, and then apply the tool. We can see that last keyframe is modified without the need to go effectively on last keyframe._


![][7]

_NB_ : This time, we really need to insert keyframe before applying tool.

## To next Keyframe

With this option, tool is a quit bit different, because we can modify only next keyframe. Tool works differently if there is a already a keyframe on current frame.

* If there is aleady a keyframe, so new position is saved, and that's it. It's exactly the same that using _Insert Keyframes_ (with _I_).
* If there is no keyframe on current frame, so current pose is insert, but not in current frame, but in next available keyframe.

## On selected keyframe

With this option, current pose is automatically inserted on all selected keyframes.

For example, before modification :

![][8]

Then I moved the foot, and then I use _Propagate_, with option _On selected keyframe_.

![][9]

Note that on current frame, keyframe is not inserted ! We have to insert it with _I_ too.

## On selected markers

This is exactly same that On selected keyframe, but paste is done on selected markers instead of selected keyframes.

![][10]

## Conclusion

Here is a tour of this tool. As you can see, it not a really simple tool to use. I think that these different options are quite different from each others, and more important, that these option don't react same way regarding insert keyframe on current frame : We don't have to for Propagate Pose, but we need to for other options.

[1]: {{ site.baseurl }}/en/2015/07/2-74-2-75-rigging-animation-new-features/
[2]: {{ site.baseurl }}/assets/imgs/post/2015-09/menu.png
[3]: {{ site.baseurl }}/assets/imgs/post/2015-09/movment_EN.png
[4]: {{ site.baseurl }}/assets/imgs/post/2015-09/propagate_pose.png
[5]: {{ site.baseurl }}/assets/imgs/post/2015-09/auto_insert.png
[6]: {{ site.baseurl }}/assets/imgs/post/2015-09/hips_KO.png
[7]: {{ site.baseurl }}/assets/imgs/post/2015-09/last_kekyframe.png
[8]: {{ site.baseurl }}/assets/imgs/post/2015-09/selected_before.png
[9]: {{ site.baseurl }}/assets/imgs/post/2015-09/on_selected_after.png
[10]: {{ site.baseurl }}/assets/imgs/post/2015-09/selected_markers.png
