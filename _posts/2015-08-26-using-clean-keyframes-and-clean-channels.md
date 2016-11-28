---
layout: post
title:  Using "Clean Keyframes" and "Clean Channels"
lang: en
ref: using_clean_keyframes_clean_channels
tags: [Tuto, Animation]
permalink: /en/:year/:month/using-clean-keyframes-clean-channels/
redirect_from:
  - /2015/08/using-clean-keyframes-and-clean-channels/
img: 20150826_using_clean_keyframes_clean_channels.png
comments: true
---

Hello,
As explains in [this article][99], a new tool _Clean Keyframes_, for _Dopesheet_ and _Graph Editor_, was added in X menu of 2.75a Blender version.

![][1]

Here is an example of use.

From default cube, I insert following keyframes :

* Image 1 : _LocRotScale_, to save location, rotation, and scale
* Image 5 : After moving on Y axe, I insert location using _Location_
* Image 10 : Moving cube on Y axe, and insert _Location_
* Image 15 : Insert _Location_, without moving cube
* Image 20 : Moving cube on Y axe, insert _Location_
* Image 25 : Insert _Location_, without moving cube

In the _Graph Editor_, we can see following curves :

![][2]

We can see Y Location on green. Scale curves, with value 1, are also visible, with only 1 keyframe, on frame 1. Rotation curves are also visible, at exactly same position than location on X and Z axes, with value 0.

![][3]

In order to use Clean Keyframes, we first select all keyframes on all curves. Clean Keyframes will be applied on entire animation.

![][4]

We can see :

* Keyframe, on frame 25 of Y axe location, was deleted. It was not useful to keep it, because value on frame 20 and 25 was identical. Tool didn't delete value on frame 10 and 15, because this would change interpolation.

* X and Z Location curve are now cleaned. Only 1 keyframe is remaining. Before cleaning, all keyframe values are identical.

* Scale curves are also clean, with only 1 keyframe on each curve.

* Why keep these curves with only 1 keyframe. These curves don't express animation (because these curves have not any _modifiers_) ? This is why a new tool will be added on version 2.76.[][5]This tool works quite same way than _Clean Keyframes_, but will delete curves with only 1 keyframe, after cleaning keyframes. We can see on next screenshot that all curves, except Y axe, are deleted.

![][6]

Here is another example, on a production file. The animation use the following rig (You will hear again about this rig in following months) :

![][7]

The shot is currently in rough blocking stage. 385 frames, about 16 seconds.

![][8]

Helped with a script (see end of post), we count how many curves and keyframes are present in animation, before cleaning, and after using these 2 tools.

![][9]

|                                    | Courbes      | Image clés |
|------------------------------------|:------------:|:----------:|
| Initial                            | 9223         | 543550     |
| After "Clean Keyframes"            | 9223         | 11061      |
| After "Clean Channels"             | 203          | 2041       |
{: class="pure-table pure-table-bordered"}

<br/>
As you can see, cleaning was really useful !

> import bpy
>
> ob = bpy.context.active_object
>
> print("fcurves : " + str(len(ob.animation_data.action.fcurves)))
>
> keyframes = 0
>
> for fcurve in ob.animation_data.action.fcurves:
>
> keyframes = keyframes + len(fcurve.keyframe_points)
>
> print("keyframes : " + str(keyframes))

[1]: {{ site.baseurl }}/assets/imgs/post/2015/08/clean_keyframes.png
[2]: {{ site.baseurl }}/assets/imgs/post/2015/08/clean_before.png
[3]: {{ site.baseurl }}/assets/imgs/post/2015/08/clean_before_detail_fr.png
[4]: {{ site.baseurl }}/assets/imgs/post/2015/08/clean_after.png
[5]: {{ site.baseurl }}/assets/imgs/post/2015/08/clean_channels.png
[6]: {{ site.baseurl }}/assets/imgs/post/2015/08/clean_channels_after.png
[7]: {{ site.baseurl }}/assets/imgs/post/2015/08/rig_spider.png
[8]: {{ site.baseurl }}/assets/imgs/post/2015/08/before_.png
[9]: {{ site.baseurl }}/assets/imgs/post/2015/08/after_.png
[99]: {{ site.baseurl }}/en/2015/07/2-74-2-75-rigging-animation-new-features/
