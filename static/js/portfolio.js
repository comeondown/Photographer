$(document).ready(function() {
    
    var ratio = 1 / 1.25;
    var $box = $('.gallery-cover');

	var loader_icon = $(".loader_icon");
    loader_icon.css("display", "none");

    var galleries_cont = $(".galleries-holder");
    galleries_cont.css("display", "block");

    // animated fadeInUp
    if ($(document).width() >= 640){
        $box.height($box.width() * ratio);
    }

    $(window).resize(function() {
        if ($(document).width() > 623){
            console.log($(document).width());
            $box.height($box.width() * ratio);
        }
        else {
            $box.height('200px');   
        }
    });

    

});



