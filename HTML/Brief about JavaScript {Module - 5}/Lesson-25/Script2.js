function Myfunction(){
    var greeting;
    var time = new Date().getHours();
    
    if(time < 10){
        greeting = "GOOD MORNING";
    }

    else if (time < 20) {
        greeting = "GOOD AFTERNOON";
    }
    
    else{
        greeting = "GOOD EVENING";
    }
document.getElementById("Hour").innerHTML = "The current is " + time;
document.getElementById("greet").innerHTML = "Greetings :" + greeting;
}
