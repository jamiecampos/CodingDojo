// Create a function that accepts a number as an input. Return a new array that
// counts down by one, from the number (as array's 'zero'th element) down to 0
// (as the last element. How long is this array?)

var array = []

function countdown(number){
    var y = 0
    for(var x = number; x >= 0; x -= 1){
        array[y] = x
        y += 1
    }
    return array
}

console.log(countdown(8))
