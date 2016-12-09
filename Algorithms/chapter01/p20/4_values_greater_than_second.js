// For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return
// how many values this is.

function greaterThan(arr){
    var total = 0
    for(var i = 0; i < arr.length; i +=1){
        if(arr[i] > arr[1]){
            console.log(arr[i])
            total += 1
        }
    }
    return "Value greater than 2nd value " + total + " times."
}

console.log(greaterThan([1,3,5,7,9,13]))
