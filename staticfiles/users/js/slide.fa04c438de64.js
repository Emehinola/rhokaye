// javascript to create a slide show in the browser

var images = ["static/users/images/sch_comp.png", "static/users/images/bck2.png", "static/users/images/bck7.png"];
var img_index = 0;

// fuction for the next button
function next() {
    slider = document.getElementById("image");
    if (img_index >= images.length - 1) {
        slider.src = images[img_index];
        slider.style.flex = "right"
        img_index = 0;
    } else {
        img_index++;

        slider.src = images[img_index];
        slider.style.flex = "right";
    }

}

// function for the previous button
function prev() {
    slider = document.getElementsByClassName("image");
    if (img_index <= 0) {
        img_index = images.length;
    }
    img_index--;
    slider.src = images[img_index];
    slider.style.flex = "right"
}

setInterval(function() { next() }, 3000)