// Given an array, move all values forward by one index, dropping the first and
// leaving a '0 value at the end.'

function moveUp(arr){
    for(i = 0; i < arr.length - 1; i++){
        arr[i] = arr[i + 1]
    }
    arr[arr.length-1] = 0
    console.log(arr)
}

moveUp([4,5,2,8])
