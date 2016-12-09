// You are passed an array containing strings. Working within that same array,
// replace each string with a number--the length of the string at previous array
// index--and return the array.



function previousLength(arr){
    arr2 = [0]
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i].length
        arr2.push(arr[i])
    }
    console.log(arr2)
}

previousLength(["dog", "bird", "mouse", "donkey"])
