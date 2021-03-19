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

var textAnimation = document.getElementById("text-1");
var text2 = " UI/UX Designer";
var text3 = " Freelancer" ;

function ctrA() {
    var temp = textAnimation.textContent;
    textAnimation.innerHTML = text2;
    text2 = text3;
    text3 = temp;
}

window.onload = function () {
    for (var i = 0; i < totalSnows; i++) {
        snows.push(new Snow());
    }
    setTimeout(() => {  ctrA();
                        setInterval(ctrA, 2400);},1200); 
    setInterval(effect, 40);
}


//hidden section
document.getElementById("about-me").addEventListener("click", nextSection1);
document.getElementById("home").addEventListener("click", nextSection2);
document.getElementById("contact").addEventListener("click", nextSection3);
document.getElementById("resume").addEventListener("click", nextSection4);


function nextSection1() {
    document.getElementById("page-about-me").style.display = "block";
    document.getElementById("page-home").style.display = "none";
    document.getElementById("page-contact").style.display = "none";
    document.getElementById("page-resume").style.display = "none";
}

function nextSection2() {
    document.getElementById("page-about-me").style.display = "none";
    document.getElementById("page-home").style.display = "block";
    document.getElementById("page-contact").style.display = "none";
    document.getElementById("page-resume").style.display = "none";
}

function nextSection3() {
    document.getElementById("page-about-me").style.display = "none";
    document.getElementById("page-home").style.display = "none";
    document.getElementById("page-contact").style.display = "block";
    document.getElementById("page-resume").style.display = "none";
}

function nextSection4() {
    document.getElementById("page-about-me").style.display = "none";
    document.getElementById("page-home").style.display = "none";
    document.getElementById("page-contact").style.display = "none";
    document.getElementById("page-resume").style.display = "block";
}

//set scrollbar visible when srolling
var scrolling = false;
var styleElement = document.createElement("style");


window.onscroll = function(e) {
    scrolling = true;
}

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

