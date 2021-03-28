


// document.getElementById("home").addEventListener("click", nextSection);

// function nextSection() {
//     document.getElementById("page-home").style.display = "none";
// }

var canvas = document.getElementById('field');
canvas.width = document.getElementsByClassName("home")[0].clientWidth;
canvas.height = window.innerHeight;
var ctx = canvas.getContext('2d');
ctx.globalCompositeOperation = 'destination-over';
var x = 100, y = 100;

function Snow() {
    this.x = Math.round(Math.random() * (canvas.width + window.innerWidth - document.getElementsByClassName("home")[0].clientWidth));
    this.y = Math.round(Math.random() * canvas.height);
    this.r = Math.round(Math.random() * 5);
    this.a = Math.random() * 3 + 0.5;
    this.o = Math.random() * 1 + 0.1;
}

Snow.prototype.update = function () {
    ctx.beginPath();
    ctx.globalAlpha = this.o;
    ctx.fillStyle = 'white';
    ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2, false);
    ctx.fill();
    ctx.closePath();


    if (this.x > canvas.width || this.x < 0) {
        this.x = Math.round(Math.random() * canvas.width);
        this.y = 0;
    }

    this.y -= this.a;
    if (this.y < 0) {
        this.y = canvas.height;
        this.x = Math.round(Math.random() * canvas.width);
    }
}


var totalSnows = 80;
var snows = [];

function drawSnows() {
    for (var i = 0; i < totalSnows; i++) {
        snows[i].update();
    }
}

function effect() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawSnows();
}

// typejs


//hidden section
document.getElementById("about-me").addEventListener("click", nextSection1);
document.getElementById("home").addEventListener("click", nextSection2);
document.getElementById("contact").addEventListener("click", nextSection3);
document.getElementById("resume").addEventListener("click", nextSection4);
document.getElementById("portfolio").addEventListener("click", nextSection5);



function nextSection1() {
    document.getElementById("page-about-me").style.display = "block";
    document.getElementById("page-home").style.display = "none";
    document.getElementById("page-contact").style.display = "none";
    document.getElementById("page-resume").style.display = "none";
    document.getElementById("page-portfolio").style.display = "none";

}

function nextSection2() {
    document.getElementById("page-about-me").style.display = "none";
    document.getElementById("page-home").style.display = "block";
    document.getElementById("page-contact").style.display = "none";
    document.getElementById("page-resume").style.display = "none";
    document.getElementById("page-portfolio").style.display = "none";
}

function nextSection3() {
    document.getElementById("page-about-me").style.display = "none";
    document.getElementById("page-home").style.display = "none";
    document.getElementById("page-contact").style.display = "block";
    document.getElementById("page-resume").style.display = "none";
    document.getElementById("page-portfolio").style.display = "none";
}

function nextSection4() {
    document.getElementById("page-about-me").style.display = "none";
    document.getElementById("page-home").style.display = "none";
    document.getElementById("page-contact").style.display = "none";
    document.getElementById("page-resume").style.display = "block";
    document.getElementById("page-portfolio").style.display = "none";
}

function nextSection5() {
    document.getElementById("page-about-me").style.display = "none";
    document.getElementById("page-home").style.display = "none";
    document.getElementById("page-contact").style.display = "none";
    document.getElementById("page-resume").style.display = "none";
    document.getElementById("page-portfolio").style.display = "block";
}



//set scrollbar visible when srolling
var scrolling = false;
var styleElement = document.createElement("style");


window.onscroll = function(e) {
    scrolling = true;
}

//animation progress-bar
// var bodyRect = document.

// onload
window.onload = function () {
    for (var i = 0; i < totalSnows; i++) {
        snows.push(new Snow());
    }
    setInterval(effect, 40);
    setInterval(() => {
        if(scrolling){
            styleElement.appendChild(document.createTextNode("::-webkit-scrollbar-thumb {background: black;}"));
            document.getElementsByTagName("head")[0].appendChild(styleElement);
            scrolling = false;
        }
        else{
            styleElement.appendChild(document.createTextNode("::-webkit-scrollbar-thumb {background: transparent;}"));
            document.getElementsByTagName("head")[0].appendChild(styleElement);
        }
    }, 100);
}

$(document).ready(function () {
    $('.owl-clients').owlCarousel({
        margin: 10,
        loop: true,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 2
            },
            500: {
                items: 3
            },
            700: {
                items: 4
            },
            1000: {
                items: 6
            }
        }
    });
});
$(document).ready(function () {
    $('.owl-testimonials').owlCarousel({
        margin: 40,
        loop: true,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            1000: {
                items: 2
            }
        }
    });
});

//set button portpoloio
var btns = document.getElementsByClassName("btn");

for(var i = 0; i < btns.length; i++)
{
    btns[i].addEventListener("click", function(){
        var current = document.getElementsByClassName("active-port");
        current[0].className = current[0].className.replace(" active-port", "");
        this.className += " active-port";
    });
};

// filter portfolio

function filter(status) {
    var x = document.getElementsByClassName("product");
    if(status == "all") status = "product";
    for(i = 0; i < x.length; i++)
    {
        arr1 = x[i].className.split(" ");
        if(arr1.indexOf("show") > -1) arr1.splice(arr1.indexOf('show'), 1);
        x[i].className = arr1.join(" ");

        if(arr1.indexOf(status) > -1)  x[i].className += " show";
    }
}