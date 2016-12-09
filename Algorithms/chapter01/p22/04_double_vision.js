// Given array, create a function to return a new array where each value in the
// original has been doubled. Calling double ([1,2,3]) should return [2,4,6]
// without changing original.

function double(arr){
    arr2 = []
    for(var i = 0; i < arr.length; i++){
        arrVal = (arr[i] * 2)
        arr2.push(arrVal)
    }
    console.log(arr2)
}

double([1,2,3,4,5])
