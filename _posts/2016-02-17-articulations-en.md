---
layout: post
title:  Joint Study
permalink: /en/:year/:month/joint-study/
redirect_from:
  - /2016/02/joint-study/
lang: en
ref: articulations
tags: [Rigging, Skinning, Topology]
img: 20160217_articulations.png
---


Hi all,  
Today, we are going to address some topology stuff. Particularly about joint like elbow.

_Disclamer_ : This is not a tutorial, neither some good practice. Here is only some research/work I did. There is probably other ways to do, and probably some more efficient way ...

I tried many way of doing, in order to have some correct deformed joints, fold in only one way, about 150°, exactly like elbow.

{% include html5video.html id="/2016/02/joint.ogv" gif=true size="50%" %}

## Start situation

It's a cylinder, cut in half size, with 2 bones, and basic _Weight Paint_.

![][1]  

![][2]![][3]

As you can see, result is quit bad:

{% include html5video.html id="/2016/02/step1.ogv" gif=true size="20%" %}

## Volume Preservation

First step is to activate Volume Preservation on Armature modifier.

![][4]

Result quality increase a little bit, but is not good enough yet:

{% include html5video.html id="/2016/02/step2.ogv" gif=true size="20%" %}

## Topology change

Here I changed topology, in order to have a deformation limited to joint area. I added 2 _loopcuts_.

![][5]  

![][6]![][7]

Now, we have indeed a deformation only on joint area, a small volume loose. But we have some face intersection when angle is too high:

{% include html5video.html id="/2016/02/step3.ogv" gif=true size="20%" %}

## Change topology again

In order to avoid intersection, I changed topology again.

Main disadvantage is that now, joint can only be fold in one side. That is how elbow works ;-)

![][8]  

![][9]![][10]

We have still some intersection issues, but next step will partially fix them:

{% include html5video.html id="/2016/02/step4.ogv" gif=true size="20%" %}

## Adding SubSurf

I then added a SubSurf modifier:

![][11]

Now intersection are limited :

{% include html5video.html id="/2016/02/step5.ogv" gif=true size="20%" %}

## Adding Shape Keys

In order to decrease intersections, I added a Shape Key, that is activated by a driver based on joint rotation:

{% include html5video.html id="/2016/02/step6_shapekey.ogv" gif=true size="30%" %}

![][12]

This time, no more intersection. But joint is now "webbed":

{% include html5video.html id="/2016/02/step6.ogv" gif=true size="20%" %}

In order to avoid that, we can tweak value of driver of Shape Key. I am not going to perform this step right now, but I am going to test another modification.

## Moving Armature

Without any modification on _weight paint_, I then moved location of bones (in _Edit_ mode), to be closer to inside face of joint.

![][13]

Here is result (without _ShapeKey_ of previous step):

{% include html5video.html id="/2016/02/step7.ogv" gif=true size="20%" %}

## Mix this two steps

Based on two previous steps (bones closer to inside, and shapekeys), we now have:

{% include html5video.html id="/2016/02/step8.ogv" gif=true size="20%" %}

We have again webbed joint (more that previously). Now time to adjust the _driver_!

## Adjusting Driver.

Rotation range must be adjusted, or value must be decreased.

![][14]

Now result is quite correct :

{% include html5video.html id="/2016/02/step9.ogv" gif=true size="20%" %}

## Adding another shapekey

Inside face of joint is now correct, but outside part is so much rounded. Have a look on your elbow :)

I added another _ShapeKey_, in order to extrude elbow bone. I kept the first one, of course.

{% include html5video.html id="/2016/02/step10_shapekey.ogv" gif=true size="20%" %}

![][15]

Here is final result :

{% include html5video.html id="/2016/02/step10.ogv" gif=true size="20%" %}

## Conclusion

You know all tests I did :)
File with all steps can be downloaded here : [Joints][16]

As I said in introduction, there are only tests. I never used this on production.

[1]: {{ site.baseurl }}/assets/imgs/post/2016/02/step_1.png
[2]: {{ site.baseurl }}/assets/imgs/post/2016/02/step_1_weight1.png
[3]: {{ site.baseurl }}/assets/imgs/post/2016/02/step_1_weight2.png
[4]: {{ site.baseurl }}/assets/imgs/post/2016/02/step2.png
[5]: {{ site.baseurl }}/assets/imgs/post/2016/02/step3.png
[6]: {{ site.baseurl }}/assets/imgs/post/2016/02/step3_weight1.png
[7]: {{ site.baseurl }}/assets/imgs/post/2016/02/step3_weight2.png
[8]: {{ site.baseurl }}/assets/imgs/post/2016/02/step4.png
[9]: {{ site.baseurl }}/assets/imgs/post/2016/02/step4_weight1.png
[10]: {{ site.baseurl }}/assets/imgs/post/2016/02/step4_weight2.png
[11]: {{ site.baseurl }}/assets/imgs/post/2016/02/step5.png
[12]: {{ site.baseurl }}/assets/imgs/post/2016/02/step6.png
[13]: {{ site.baseurl }}/assets/imgs/post/2016/02/step7.png
[14]: {{ site.baseurl }}/assets/imgs/post/2016/02/step9.png
[15]: {{ site.baseurl }}/assets/imgs/post/2016/02/step10_shapekey.png
[16]: https://drive.google.com/file/d/0B-mpivl1jPpuVzVlN3dCMXY5WmM/view?usp=sharing
