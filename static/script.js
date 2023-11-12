/*Slider function [It is recommended to place a function in a separate JS file, such as "functions.js"]*/
function myCoolSlider() {
    $('.slider').slick({
        
        arrows:false,
        dots: false,
        infinite: true,
        
        speed: 600,
 
     
        autoplay: true,
        autoplaySpeed: 4000,

    }

   );
}
/*End of Slider function*/



$(document).ready(function() {


/*Calling the function [It is recommended to call a function in a separate JS file, such as "scripts.js"]*/
myCoolSlider();
AOS.init();
/*.................End of call*/


});