// If two given numbers represent your birth month and day in either order, log
// "How did you know?", else log "Just another day...."

var birthMonth = 5
var birthDay = 7

function Birthday(a,b){
    if ((a == birthMonth && b == birthDay) || (b == birthMonth && a == birthDay)){
        console.log("How did you know?");
    }else{
        console.log("Just another day....")
    }
}
