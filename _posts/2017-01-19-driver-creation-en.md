---
layout: post
title:  "Drivers in version 2.78"
permalink: /en/:year/:month/drivers-in-version-2-78/
lang: en
ref: drivers_2_78
tags: [Tuto, Rigging]
img: 20170119_drivers.png
no_rss: false
comments: true
---

Hi all,  
In the post, I will describe new features about drivers in version 2.78.

### Driver creation with picker

![drivers]({{ site.baseurl }}/assets/imgs/post/2016/09/drivers.png)

Driver creation is now easilier that before:  

* You can use Ctrl+D on a property on which you want to create a driver.
* A pop-up is displayed to choose creation mode:  
	* __All from Target__ will add a driver on each component of property for example, location X, Y and Z). Reference for these drivers is a unique value, defined in next step.
  * __Single from Target__ will add a driver on only one component of property (for example, rotation Y).
  * __Match Indices__ will a driver on each component of property, based on each component of reference property (if reference has same length: position X, Y, Z on rotation X, Y, Z respectively, for example).
  *	__Manually Create Later__ works same way than _Add driver_ on Blender 2.77. A new driver is created for each component, but detail data must be filled in on _Graph Editor_.
  * __Manually Create Later (Single)__ works same way than _Add single driver_ on Blender 2.77. Driver data must be filled in on _Graph Editor_.

 _Transform Channel_ variables are created for each transformation properties. For all other type,  _Single Property_ are created.  
Radian/degree convertion for rotation are automatically added.

Here is a video (in French), where you can see how it works (after a short introduction about drivers):  
{% include youtube.html id='zBsW_QDd6ms' %}
<br/>
<br/>

### Keyframes for driver correction

Until version 2.77, when you add a _keyframe_ on a property where there is already a driver, this will add a new _F-curve_, that will be never used. We can see new _keyframes_ on _Timeline_, but are not used for animation ... That is quite strange.  
On version 2.78, new _Keyframes_ are added directly on _F-curve_ of driver. This is now more easy to create driver correction (but you need to mute this driver to add _keyframes_ on it).
Here is a (French) video to explain this new feature:  
{% include youtube.html id='GfFPue6RAec' %}
