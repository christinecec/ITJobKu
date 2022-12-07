window.onscroll = function() {scrollFunction()};
window.onresize = function() {scrollFunction()};

var elms = document.querySelectorAll("[id='nav-btn']");
let element = document.getElementById("scrollbar-track"),
    style = window.getComputedStyle(element),
    scroll_track_height = parseFloat(style.getPropertyValue('height'));
let ratio = scroll_track_height / document.documentElement.scrollHeight;
let scroll_height = window.innerHeight * ratio;
var scroll_top = document.documentElement.scrollTop * ratio;
document.getElementById("scrollbar-thumb").style.height = scroll_height + 'px';
document.getElementById("scrollbar-thumb").style.marginTop = scroll_top + 'px';

element.addEventListener("click", (e) => {
  let newPageScroll = (document.documentElement.scrollHeight * (e.clientY / window.innerHeight)) - (window.innerHeight / 2);
  window.scrollTo({
    top: newPageScroll,
    behavior: 'smooth'
  });
});

function scrollFunction() {
    let element = document.getElementById("scrollbar-track"),
        style = window.getComputedStyle(element),
        scroll_track_height = parseFloat(style.getPropertyValue('height'));
    let ratio = scroll_track_height / document.documentElement.scrollHeight
    let scroll_height = window.innerHeight * ratio;
    var scroll_top = document.documentElement.scrollTop * ratio;
    document.getElementById("scrollbar-thumb").style.height = scroll_height + 'px';
    document.getElementById("scrollbar-thumb").style.marginTop = scroll_top + 'px';
    
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("navbar").style.top = "0";
        for(var i = 0; i < elms.length; i++)
            elms[i].style.marginTop='10px';
        if (window.location.pathname != "/") {
            document.getElementById("nav-tes-btn").style.marginTop = "10px";
        }
        
    } else {
        document.getElementById("navbar").style.top = "-60px";
        for(var i = 0; i < elms.length; i++)
            elms[i].style.marginTop='20px';
        if (window.location.pathname != "/") {
            document.getElementById("nav-tes-btn").style.marginTop = "20px";
        }
        
    }
}


if (window.location.pathname == "/home.html") {
    document.querySelectorAll("[id='nav-btn']")[1].disabled = false;
    document.querySelectorAll("[id='nav-btn']")[2].disabled = false;
    document.querySelectorAll("[id='nav-btn']")[0].disabled = true;
}
else if (window.location.pathname == "/job") {
    document.querySelectorAll("[id='nav-btn']")[0].disabled = false;
    document.querySelectorAll("[id='nav-btn']")[2].disabled = false;
    document.querySelectorAll("[id='nav-btn']")[1].disabled = true;
}
else if (window.location.pathname == "/about.html") {
    document.querySelectorAll("[id='nav-btn']")[0].disabled = false;
    document.querySelectorAll("[id='nav-btn']")[1].disabled = false;
    document.querySelectorAll("[id='nav-btn']")[2].disabled = true;
}
else {
    document.querySelectorAll("[id='nav-btn']")[0].disabled = false;
    document.querySelectorAll("[id='nav-btn']")[1].disabled = false;
    document.querySelectorAll("[id='nav-btn']")[2].disabled = false;
}