// Given an array and a value Y, count and print the number of array values
// greater than Y.

function greaterThan(arr, Y){
    var total = 0
    for(i = 0; i < arr.length; i++){
        if(arr[i] > Y){
            console.log(arr[i])
            total +=1
        }
    }
    console.log(total + " greater than " + Y)
}

greaterThan([43,56,23,1,4356,657,345,243], 365)
