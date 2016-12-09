// Kenny tries to stay safe, but somehow everyday something happens. If there is
// a 10% chance of volcano, 15% chance of tsunami, 20% chance of earthquake,
// 25% chance of blizzard, and 30% chance of meteor strike, write function
// whatHappensToday() to print the outcome.

function whatHappensToday(){
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

whatHappensToday()
