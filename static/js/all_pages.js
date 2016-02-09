var body = document.getElementsByTagName("BODY")[0];
var header = document.getElementsByClassName("header")[0];
if (body.scrollTop == 0){
	header.className +=  " header--on-top";
}
else{
	header.className = "header"
}
window.onscroll = function() {
	console.log(header);
	if (body.scrollTop == 0){
		header.className +=  " header--on-top";
	}
	else{
		header.className = "header"
	}
}

var menuButtonOnclickOpen = function(){
		sliderMenu.className = "header-navslider header-navslider--open";
		console.log('open');
		headerMenuButton.removeEventListener("click", menuButtonOnclickOpen);
		if (headerMenuButton.addEventListener){
			headerMenuButton.addEventListener("click", menuButtonOnclickClose, false);
		};
}

var menuButtonOnclickClose = function(){
		
		sliderMenu.className = "header-navslider";
		console.log('close');
		headerMenuButton.removeEventListener("click", menuButtonOnclickClose);
		if (headerMenuButton.addEventListener){
			headerMenuButton.addEventListener("click", menuButtonOnclickOpen, false);
		};
}

window.onload = function (){
	headerMenuButton = document.getElementsByClassName('navigation__menu-icon')[0];
	sliderMenu = document.getElementsByClassName('header-navslider')[0];
	console.log(headerMenuButton);
	if (headerMenuButton.addEventListener){
		headerMenuButton.addEventListener("click", menuButtonOnclickOpen, false);
	};
}

window.onresize = function(){
	if (document.documentElement.clientWidth > 640 && sliderMenu.className !== "header-navslider"){
		headerMenuButton.removeEventListener("click", menuButtonOnclickClose);
		sliderMenu.className = "header-navslider";
		if (headerMenuButton.addEventListener){
			headerMenuButton.addEventListener("click", menuButtonOnclickOpen, false);
		};
	}
}