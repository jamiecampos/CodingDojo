// Create an array with all the odd integers between 1 and 255 (inclusive).


function createArr(){
    var arr = []
    for(i = 1; i < 256; i++){
        if(i % 2 ==1){
            arr.push(i)
        }
    }
    console.log(arr)
}

createArr()
