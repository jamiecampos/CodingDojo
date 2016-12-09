// Create a function that takes an array of numbers. The function should print
// the lowest value in the array and return the highest value in the array.

function lowHigh(arr){
    for (var i = 0; i < arr.length; i++){
        var min = arr[0]
        var max = arr[0]
        if(arr[i] > max){
            max = arr[i]
        }
        else if(arr[i] <= min){
            min = arr[i]
        }
    }
    console.log(min)
    return max
}

lowHigh([1,2,3])
