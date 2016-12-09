// Given an array arr and a number num, multiply all values in arr by num, and
// return the changed array arr.

function scale(arr,num){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * num
    }
    console.log(arr)
}

scale([1,2,3,4,5], 5)
