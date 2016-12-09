// Return the given array, after setting any negative values to zero.

function zero(arr){
    for(i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0
        }
    }
    console.log(arr)
}

zero([34,-6,23,4,1,-9,-44])
