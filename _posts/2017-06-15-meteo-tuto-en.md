---
layout: post
title:  "Weather animation tutorial"
permalink: /en/:year/:month/weather-anim-tuto/
lang: en
ref: meteo_tuto
tags: [Tuto, Animation]
img: 20170615-meteo.png
no_rss: false
comments: true
---

Hi all,  
In the following tutorial, I am going to create this animation from scratch:  

{% include html5video.html id="/2017/06/meteo.ogv" gif=true size="50%" %}

Last July (yes, one year ago ...), I perfomed a _master class_ at [Grafik Labor][1].  
Here is a tutorial version (in French) of what we did during it.  

Even with french audio, you will be able to understand. If not, here is a quick sumary of used tools (just below the video)  

<br/>
{% include youtube.html id='ZjG3Fz5fxS8' %}

<br/>
<br/>

*  Go to orthogal view, top view (_5_/_7_)  
*  Create a circle, duplicate with _Shilft+D_, using _Ctrl+R_ for repeating last operations Rename them :)  
*  Rotation of suns (left and right)  
    *  Create an empty at rotation center  
    *  Parent sun to empty (_Ctrl+P_)  
*  Sun rays :  
    *  keep object center at center of sun, so be sure to be in Edit Mode to move vertices  
    *  Duplicate with _alt+D_ (keeping only 1 mesh data), rotation 30°, and repeat with _Ctrl+R_  
*  Create Sun rays _shapekeys_ (for height, width, appearing and disappearing)  
* Cloud :  
    *  Create cloud with multiple circles, and join them into 1 object (_Ctrl+J_)  
    *  Move up cloud (to be above sun)  
* water drops :  
    *  Create a plan  
    *  Using local view (_/_)  
    *  In edit mode: Scale, and duplicate (_Shift+D_ then _Ctrl+R_)  
    *  In object mode (to modify local axis of object)  
    *  _Ctrl+Tab_ : selection by edge. Select an edge, then select similar to select all edges wanted  
    *  Change to pivot _"Individual origins"_  
    *  Scale 0 on Y axis to make edges horizontal  
    *  Go back to _"Median Point"_ pivot  
    *  Duplicate drops, and joint into only 1 object (_Ctrl+J_). Be sure to select correctly named object last, to be sure the resulting object will keep this name  
    *  Move drops between sun and cloud.(go to front view _1_, and wireframe _Z_ to see it correctly)  
* Do not parent rays to sun, but create a copy location constraint (for non rotating rays) :  
    *  Select sun, then a ray, _Ctrl+Shift+C_ to add copy location  
    *  Select all rays, with constrainted ray last, and Copy contraint to selected object  
*  Copy location of sun for cloud, use offset to be able to move the cloud  
*  Same process for water drops (copy location, enable offset)  
*  Animation of sun empty :  
    *  frame 0, rotation keyframe (_I_)  
    *  frame 10, change rotation, insert rotation keyframe  
    *  frame 20, reset rotation (_Alt+R), and insert keyframe  
*  Animation of cloudy sun empty:  
    *  frame 20, rotation keyframe  
    *  frame 30, change rotation, insert rotation keyframe  
    * frame 40, reset rotation, insert keyframe  
*  Change end of animation at frame 39 (for looping) (using _E_ on timeline)  
*  Using _Alt+A for play animation  
*  Open Graph Editor and DopeSheet  
*  On cloudy sun, move all keyframes 1 frame earlier ( _G -1_)  
*  Change end of animation (now on 38)  
*  Using _Home_ to zoom on Graph Editor  
*  Change handle type to free (V), then change curves  
*  Animation of rays:  
    *  Keyframe (I) at frame 0 and 10 for appearing (on height)  
    *  Keyframe at frame 10 and 20 for disappearing (on height and width)  
    *  Tweak curves (change handle type first (_V_)) for better result  
*  Animation of drops:  
    *  On frame 19, insert location keyframe  
    *  On frame 39, move drops using local axis (_G, Y, Y), insert location keyframe  
    *  Change interpolation to linear (T)  
*  Tweak Z position of sun to avoid mesh penetration  
*  Animation of render visibilty of cloud:  
    *  Render off, insert keyframe at frame 0  
    *  Render on, insert keyframe at frame 19  
    *  Can be done on View 3D visibility to see it  
*  Switch to Cycles render engine  
*  Use Emit shaders  
*  Create 1 material for central circles, 1 for sunny sun, 1 for cloudy sun  
*  Insert keyframes on color, set curves to _constant_ to avoid interpolations  
*  Use sun shader for rays  
*  For cloud, cloud on '4' to make a new material based on gray material, and change color  
*  Create a new material for drops  
*  Add a camera, use _0_ to go to camera view, and _G, Z, Z_ to get a correct location  
*  Have a first render :)  
*  Change sampling to 10 to go faster  
*  Using splots to compare different sampling (using _J_ to switch splots)  
*  Create a plan, scale, and create a new material (animated gray/blue, using _constant_ interpolation)  
*  Hide plan in view 3D, should be better for 3D view selection  
*  Animate sun material color, that I forgot to do earlier  
*  Create a new plan for drop hidding  
    *  Create plan  
    *  add constraint _Copy Location_, using offset, to follow the cloudy sun  
    *  Move up the static circle  
    *  Move cloudy sun up and drops down (need to delete Z curve)  
    *  Create a new material with _HoldOut_ shader  
    *  Set film to transparent  
* Compositing  
    *  Move background plan to another layer  
    *  Create a new render layer for background layer  
    *  On Node editor, duplicate render layer node  
    *  Switch the duplicated one to background render layer  
    *  Add alphaOver node, tweak socket if needed  
* Bug displayed is fixed in 2.78, don't worry ;-)  
* Render Animation :)  

[1]: http://julienduroure.com/en/2016/06/grafik-labor-rennes-on-july-2nd/
