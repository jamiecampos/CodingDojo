// Kyle (smarter than Kenny) notes that the chance of one disaster is totally
// unrelated to the chance of another. Change whatHappensToday() function to
// create whatReallyHappensToday(). In this new function test for each disaster
// independently, instead of assuming exactly one disaster will happen. In other
// words, with this new function, all five might occur today--or not. Maybe
// Kenny will survive!

function whatReallyHappensToday(){
    if((Math.random() * (100 - 1) + 1) < 11){
        console.log("Kenny is lava'd today.")
    }if((Math.random() * (100 - 1) + 1) < 16){
        console.log("Kenny is washed to sea today.")
    }if((Math.random() * (100 - 1) + 1) < 21){
        console.log("Kenny is swallowed up by the ground today.")
    }if((Math.random() * (100 - 1) + 1) < 26){
        console.log("Kenny is buried in snow today.")
    }if((Math.random() * (100 - 1) + 1) < 31){
        console.log("Kenny is hit by a space rock today.")
    }
}

whatReallyHappensToday()
