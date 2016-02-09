//Ugly collaboration jq with native js
main_blocks = {}
$(document).ready(function() {
    b = detect.parse(navigator.userAgent);
    console.log(b.browser.name);
    var loader_icon = $(".loader_icon");
    loader_icon.css("display", "none");

    var photos_container = $(".photos-container");
    photos_container.css("display", "block");


    var ratio = 1 / 1;
    var $box = $('.photo-preview');

    var loader_icon = $(".loader_icon");
    loader_icon.css("display", "none");

    var galleries_cont = $(".galleries-holder");
    galleries_cont.css("display", "block");

    var resizingRelativeHeight = function(box, ratio){
        box.height(box.width() * ratio);
    };

    $(window).resize(function() {
            resizingRelativeHeight($box,ratio);
    });
    
    //Native js
    var img = document.getElementsByTagName("img");
    for (var i=0; i<img.length; i++){
        img[i].addEventListener("contextmenu", returnFalseFunction);
    }

    addFullOpenOnclick();

    //Main blocks
    header = document.getElementsByClassName("header")[0];
    main_blocks = {photos : document.getElementsByClassName("photo-preview"),
                    photos_container : document.getElementsByClassName("photos-container"),
                    full_photo_container : document.getElementsByClassName("full-image-holder")[0],
                    photo_holder : document.getElementsByClassName('full-image-holder__photo-holder')[0],
                    holder_close_button: document.getElementsByClassName('full-image-holder__close')[0],
                    holder_next_button: document.getElementsByClassName('full-image-holder__next-photo')[0],
                    holder_prev_button: document.getElementsByClassName('full-image-holder__prev-photo')[0],
                    holder_photo_info: document.getElementsByClassName('full-image-holder__photo-info')[0],
                    holder_photo_info_name: document.getElementsByClassName('full-image-holder__name')[0],
                    holder_photo_info_descr: document.getElementsByClassName('full-image-holder__descr')[0]}
    image_number = -1;


});


//Additional function that make possible nice binding listener on block
function onClickBound(e) {
    openFullImage.call(this, e || windown.event);
}

//Function add event listener (open full res) on all preview images
var addFullOpenOnclick = function (){
    var photos = $(".photo-preview");

    //Hadle onclick event on each photo. event call openFullImage eventually
    photos.each(function (index){
        _this = this;

        if (this.addEventListener){
            this.addEventListener("click", onClickBound, false);
        }
        else if (cell1.attachEvent){
            this.attachEvent("onclick", onClickBound);
        }
    });
}

//Function delete onclick listener on all images
var removeFullOpenOnclick = function(){
    var photos = $(".photo-preview");
    photos.each(function(){
        this.removeEventListener('click', onClickBound);
    });
}


var returnFalseFunction = function(){
    return false;
};

var get_image = function(url) {
    var holder = $(".full-image-holder");
    holder.css("display", "block");
    holder.html("");
    holder.append("<img src='" + url + "' width='500px' onclick='close_image_modal()' >");

};



//Js native
var openFullImage = function(){
    removeFullOpenOnclick();
    _this = this;
    header.style.position = "fixed";

    for (var i=0; i<main_blocks.photos.length; i++){
        main_blocks.photos[i].className += " photo-preview--slideshow";
    }

    //Listener that wait for end of fadeout animation of preview
    setTimeout(openFullImageLayer, 800);
    setTimeout(postHolderAnimation, 800);


    function openFullImageLayer(event){

        //No display photo-preview while open full image
        for (var i=0;i<main_blocks.photos.length;i++){main_blocks.photos[i].style.display="none"};
        main_blocks.full_photo_container.style.visibility = "visible";
        main_blocks.full_photo_container.className += " full-image-holder--opening";
    }

    //Function that will called after ending of FullPhotoLayer animation
    function postHolderAnimation(event){


        //Input full img
        pasteFullImage(_this);

        main_blocks.holder_close_button.className += " full-image-holder__close--ready";
        main_blocks.holder_next_button.className += " full-image-holder__next-photo--ready";
        main_blocks.holder_prev_button.className += " full-image-holder__prev-photo--ready";
        main_blocks.holder_photo_info.className += " full-image-holder__photo-info--ready";

        //Find index of current photo almost all on page
        for (var i=0; i<main_blocks.photos.length; i++){
            if (main_blocks.photos[i]==_this){
                image_number = i;
            }
        }
        console.log(image_number);
        if (main_blocks.holder_close_button.addEventListener){
            main_blocks.holder_close_button.addEventListener("click", closeFullImageOnCLick, false);
            main_blocks.holder_next_button.addEventListener("click", nextPhotoOnClick, false);
            main_blocks.holder_prev_button.addEventListener("click", prevPhotoOnClick, false);
        }
        else if (cell1.attachEvent){
            //TODO: Добавить
            //this.attachEvent("onclick", onClickBound);
        }

    }
    

}

var closeFullPhotoImg = function(){
    var full_photo = document.getElementsByClassName("full-photo")[0];
    if (full_photo){
        
        setTimeout(returnFalseFunction, 1000);
        main_blocks.full_photo_container.removeChild(full_photo);
    }
}

var pasteFullImage = function(preview_photo){
    //Enter src from image to background-img of photo-holder
    main_blocks.photo_holder.style.backgroundImage = 'url(' + preview_photo.dataset.image +')';
    pasteFullImageInfo(preview_photo);
}

var pasteFullImageInfo = function(preview_photo){
    main_blocks.holder_photo_info_name.innerHTML = preview_photo.dataset.name; 
    main_blocks.holder_photo_info_descr.innerHTML = preview_photo.dataset.descr; 
}

var closeFullImageOnCLick = function(){
    //Remove listener from button close
    main_blocks.holder_close_button.removeEventListener("click", closeFullImageOnCLick);

    //Make full_photo_container to start position
    main_blocks.full_photo_container.style.visibility = "";
    main_blocks.full_photo_container.className = " full-image-holder";
    main_blocks.photo_holder.style.backgroundImage = '';
    //Delete full_photo
    closeFullPhotoImg();

    //Resize photoblocks
    //very bad
    var ratio = 1;
    var box = document.getElementsByClassName('photo-preview');
    console.log(box);
    for (var i=0; i<box.length;i++){
        box[i].style.height = '';
        console.log(box[i].offsetHeight);
    }
    
   
    //Remove button from window
    main_blocks.holder_close_button.className = " full-image-holder__close";
    main_blocks.holder_next_button.className = " full-image-holder__next-photo";
    main_blocks.holder_prev_button.className = " full-image-holder__prev-photo";
    main_blocks.holder_photo_info.className = " full-image-holder__photo-info";
    //Display preview
    for (var i=0;i<main_blocks.photos.length;i++){main_blocks.photos[i].style.display=""};
    setTimeout(function(){
         for (var i=0; i<main_blocks.photos.length; i++){
            main_blocks.photos[i].className = " photo-preview";
        }
    }, 20);
    addFullOpenOnclick();  
}


var nextPhotoOnClick = function(){
    console.log(image_number);
    if (main_blocks.photos[image_number+1]){
       closeFullPhotoImg();
       var next_photo = main_blocks.photos[image_number+1];
       pasteFullImage(next_photo);
       image_number += 1; 
    };
}

var prevPhotoOnClick = function(){
    console.log(image_number);
    if (main_blocks.photos[image_number-1]){
       closeFullPhotoImg();
       var next_photo = main_blocks.photos[image_number-1];
       pasteFullImage(next_photo);
       image_number -= 1; 
    }
}