---
layout: post
title:  Rigging Workflow - Development
lang: en
ref: rigging_tools
tags: [Rigging]
permalink: /en/:year/:month/riggingworflow/
redirect_from:
  - /2015/03/riggingworflow/
img: 20150311_rigging_tools.png
comments: true
---


Hi all,
I am currently working on an animated short as rigger and animator. During rigging part of the project, I developed some tools to help me.

Most of these tools are still WIP, but here is some of them. I joined them into a pie menu. This pie is a WIP too, with temporary names.

### Layers display

This one is not a tool ... This is a quick tips to help me. Between _outliner_ and _properties_, I added a new window (type _properties_), on armature layer tab. I hide header of the window, and resize to only display layers. By this way, I can access quickly to bone layers, without changing tab if I previously was on bone tab or constraint tab :

![][1]

### Display mode

I added in my pie menu a quick access to most of display mode for armature/bones :

![][2]

Here are how bones are displayed :

![][3]

### Bone Chain Rename

Renaming bones can take a long time ! I use a script to rename automatically bones. Here is an example about finger. Bones are all named Bone.XYZ

![][4]

You only have to rename 1 bone, and use operator from pie menu. For example, if you want to rename bones to _finger_X.L_, with X equals 0,1,2,3, and 4, you have to rename first bone of first chain to _finger_.L_. Then select all chain roots, with renamed bone last.

![][5]

All bones are renamed, regarding chain and position of the bone.

![][6]

Chain named are choose with alphabetic order of old bone named. Here, active bone will become _finger_0.L_, Bone.002 will become _finger\_1.L_, etc... If we really want to choose order of chains, you can rename only chain roots alphabetically.

### Select non parented bones

This tool select automatically all non parented bones. This is useful to connect all bones to a root bone. Using this tools, root bone will be selected too. You only have to de-select it, and re-select it (to make it active bone), and parent with Control+P

### Set segment

If you want to use curved bones, setting all deform bone with segments number can take a loooong time. I can now set all bones in only 1 time, using number of segment that can be found in user preferences of the add-on.

![][7]

### Set scale from root

If you unchecked "_inherit scale_" on some bones, we need to add a copy scale on that bone (copying root bone), to be able to change global size of the rig by scaling root bone. Finding impacted bones, and adding the constraint (and move the constraint on top of stack) can be looong too :)

I wrote a tool that perform this action for me : automatic selection of impacted bones, adding constraint, and move constraint on top of constraint stack)

### Mirror

Until now, I used to mirror my armature following these steps :

*  Duplicate bones (so new bones are selected)
*  Flip names of new bones
*  invert selection (so old bones are now selected)
*  Translate bones (but validate without translation). This step is needed to redraw new bones mirrored.

This process works, most of the time. But for any complex rigs, it fails. It can leads to big errors in rigs, for parenting, and for constraint targets.

![][8]

I submitted a bug report ([mirror bones][14]), but it was refused because duplicating the chain, and then flip names can not leads to a correct bone naming and mirroring.

I developed a tool that perform a correct mirror of bones. Mirroring is now easy !

But ... it's quite low ! I mirrored a complex rig, Charlie, than can be downloaded from Puppeteer Lounge. Mirroring is working correctly, but take about 1min05s to perform (130 bones). Quite long, but faster than doing it by hands :)

I decided to implement it directly in blender. I wrote a patch : [Bone mirror][10].

Currently, this patch is not accepted into Blender yet. Same mirroring than previously (130 bones on Charlie) is done instantly.

_[updated March 19th] : Campbell made some fixes/improvements, and just committed the patch ! This new feature will be available on Blender 2.75_

### Bug detection

During rigging part of project (that is not finished yet), I detected some bugs that I reported on [developer.blender.org][11]. Except mirroring (I already wrote about this one :) ), other ones are now fixed, and available on Blender 2.74 :

* [Bug with clear user transform when paint weight painting is active][12]

* [Skinning : set parent with automatic weights doesn't take into account locked vertex groups][13]

### Conclusion

There is not really a conclusion, because all these tools are not stable, and can change, following my workflow.

This add-on is currently not available to download, and will be available in next months.

Here is a video, in French, about all these tools :

{% include youtube.html id='bv66gdexbqg' %}

[1]: {{ site.baseurl }}/assets/imgs/post/2015/03/bone_layers.png
[2]: {{ site.baseurl }}/assets/imgs/post/2015/03/display_mode.png
[3]: {{ site.baseurl }}/assets/imgs/post/2015/03/display_example.png
[4]: {{ site.baseurl }}/assets/imgs/post/2015/03/rename1.png
[5]: {{ site.baseurl }}/assets/imgs/post/2015/03/rename2.png
[6]: {{ site.baseurl }}/assets/imgs/post/2015/03/rename3.png
[7]: {{ site.baseurl }}/assets/imgs/post/2015/03/segment.png
[8]: {{ site.baseurl }}/assets/imgs/post/2015/03/mirror1.png
[9]: http://www.puppeteerlounge.com/free-characters
[10]: https://developer.blender.org/D1147
[11]: http://developer.blender.org
[12]: https://developer.blender.org/T43776
[13]: https://developer.blender.org/T43814
[14]: https://developer.blender.org/T43760
