const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

const toggleBob = function(){
    const isVisible = bobGif.getAttribute("data-visible") ==="true";
    if(isVisible){
        bobGif.style.display = "none";
        bobGif.setAttribute("data-visible","false");
    }else{
        bobGif.style.display = "block";
        bobGif.setAttribute("data-visible","true");
    }
};
