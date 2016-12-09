// Mr. Cerise teaches high school math. Write a function that assigns and
// prints a letter grade, given an integer representing a score from 0 to 100.
// Those getting a 90+ get an 'A', 80-89 earn 'B', 70-79 is a 'C', 60-69 should
// get a 'D', and lower than 60 receive an 'F'. For example, given 88, you
// should log "Score: 88. Grade: B". Given the score 61, log the string "Score:
// 61. Grade: D".

function letterGrades(grade){
    if(grade > 89){
        console.log("Score: " + grade + ". Grade: A.")
    }else if(grade > 79){
        console.log("Score: " + grade + ". Grade: B.")
    }else if(grade > 69){
        console.log("Score: " + grade + ". Grade: C.")
    }else if(grade > 59){
        console.log("Score: " + grade + ". Grade: D.")
    }else{
        console.log("Score: " + grade + ". Grade: F.")
    }
}

letterGrades(100)
