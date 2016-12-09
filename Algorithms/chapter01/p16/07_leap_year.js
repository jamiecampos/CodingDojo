// Write a function that determines whether a given year is a leap year. If a
// year is divisible by four, it is a leap year, unless it is divisible by 100.
// However, if it is divisible by 400, then it is.


function leapYear(num){
    if ((num % 4 == 0) && ((num % 100 != 0) || (num % 400 == 0))){
        console.log("The year " + num + " is a leap year.")
    }else{
        console.log("The year " + num + " is not a leap year.")
    }
}
