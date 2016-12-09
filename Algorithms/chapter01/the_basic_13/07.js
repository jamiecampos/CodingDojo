// Given an array of numbers, replace any negative values with the string "Dojo".

function dojo(arr){
    for(i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = "Dojo"
        }
    }
    console.log(arr)
}

dojo([34,-6,23,4,1,-9,-44])
