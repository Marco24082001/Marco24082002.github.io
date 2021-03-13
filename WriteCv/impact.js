// document.getElementById("home").addEventListener("click", nextSection);

// function nextSection() {
//     document.getElementById("page-home").style.display = "none";
// }

var canvas = document.getElementById('field');
        canvas.width = document.getElementsByClassName("home")[0].clientWidth;
        canvas.height = window.innerHeight;
        var ctx = canvas.getContext('2d');
        ctx.globalCompositeOperation='destination-over';
        var x = 100, y = 100;

        function Snow(){
            this.x = Math.round(Math.random() * (canvas.width + window.innerWidth - document.getElementsByClassName("home")[0].clientWidth));
            this.y = Math.round(Math.random() * canvas.height);
            this.r = Math.round(Math.random() * 5);
            this.a = Math.random() * 3 + 0.5;
            this.o = Math.random() * 1 + 0.1; 
        }

        Snow.prototype.update = function(){
            ctx.beginPath();
            ctx.globalAlpha = this.o;
            ctx.fillStyle = 'white';
            ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2, false);
            ctx.fill();
            ctx.closePath();
            
            
            if(this.x > canvas.width || this.x < 0){
                this.x = Math.round(Math.random() * canvas.width);
                this.y = 0; 
            }

            this.y -= this.a;
            if(this.y < 0) {
                this.y = canvas.height;
                this.x =Math.round(Math.random() * canvas.width);
            }
        }


        var totalSnows = 80;
        var snows = [];

        function drawSnows(){
            for(var i = 0; i < totalSnows; i++) {
                snows[i].update();
            }
        }

        function merryXmas(){
            ctx.clearRect(0,0,canvas.width,canvas.height);
            drawSnows();
        }

        window.onload = function(){
            for(var i = 0; i< totalSnows; i++){
                snows.push(new Snow());
            }
            setInterval(merryXmas, 40);
        }