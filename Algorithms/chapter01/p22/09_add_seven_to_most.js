// Build a function that accepts array. Return a new array with all values
// except first, adding 7 to each. Do not alter the original array.

function addSeven(arr){
    arr2 = []
        for(var i = 1; i < arr.length; i++){
                arr2.push(arr[i] + 7)
        }
        console.log(arr2)
}

addSeven([1,2,3,4,5,6,7])
