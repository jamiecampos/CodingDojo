// Given array, write a function that reverses values in-place. Example:
// reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3].

function reverse(arr){
    arr2 = []
    for(var i = arr.length-1; i >= 0; i--){
        arr2.push(arr[i])
    }
    console.log(arr2)
}

reverse([3,1,6,4,2])
