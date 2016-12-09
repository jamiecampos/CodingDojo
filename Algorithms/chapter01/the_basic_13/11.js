// Square each value in a given array, returning that same array with changed values.

function square(arr){
    for(i = 0; i < arr.length; i++){
        arr[i] = arr[i]*arr[i]
    }
    console.log(arr)
}

square([4,5,2,8])
