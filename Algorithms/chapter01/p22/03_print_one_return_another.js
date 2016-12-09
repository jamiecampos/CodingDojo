// // Build a function that takes array of numbers. The function should print
// second-to-last value in the array, and return first odd value in the array.

function printReturn(arr){
    var odds = []
    for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 == 1){
            odds.push(arr[i])
        }
    }
    console.log(arr[arr.length - 2])
    return(odds[0])
}

printReturn([1,2,3,4,5])
