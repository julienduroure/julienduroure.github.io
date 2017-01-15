Reveal.addEventListener( 'videoloop', function() {
	var vid = document.getElementById("anim");
	vid.loop = true;
	vid.play();
}, false );

function ral(val) {
	document.getElementById('foot').playbackRate = val;
}

function pencil(val) {
	if (val == 'on') {
		src = 'img/CdL2016/foot_on.ogv' ;
	} else
	{
		src = 'img/CdL2016/foot.ogv' ;
	}
	document.getElementById('foot').pause() ;
	document.getElementById('footid').setAttribute('src', src) ;
	document.getElementById('foot').load() ;
	document.getElementById('foot').play() ;
}
