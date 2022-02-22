// bookIndex(input) -> input is an array of integers, in order
// those integers represent pages in a book where a certain term is found
// output is a string representing a listing of those pages in a book's index
// an input of: [58, 104, 105, 106, 192, 194, 195, 196]
// leads to an output of: "58, 104-106, 192, 194-196"
// input: [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18]
// output: "1-5, 8-12, 15, 17-18"

// suggestion: break this into two parts, or maybe even two
// functions - get your array of integers and turn it into an array
// of strings, then turn that array of strings into a single string
// [58, 104, 105, 106, 192, 194, 195, 196]
// ["58", "104-106", "192", "194-196"]
// "58, 104-106, 192, 194-196"
// also a suggestion: remember that you can modify your for loop iterator
// during your loop! you can add to or subtract from i at any point
// also also: remember that loops can go within loops - while in for,
// for in for, while in while, etc.

function bookIndex(input) {
    temp = []

    for(var i=0; i < input.length; i++){
        if ((input[i]+1)==input[i+1]){

        }else{
            temp.push(String(input[i]))
        }
        
    }
    return temp
    // for loop
    // check the value at i + 1 
    // if next value is not there, put in as a string
    // is the next value one higher than the current value (if statement)
    //      if no, push into the string
    //      if yes,
}

console.log(bookIndex([2,4,5,7,12,18, 35, 47]))

function buildString(input) {

}

// function bookIndex(input) {
//     // do some stuff here
//     return (buildString(array_of_strings));
// }

// function buildString(input) {
//     // turns input into a string to return
// }

console.log(bookIndex([1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 17, 18]));
// returns "1-5, 8-12, 15, 17-18"
console.log(bookIndex([1,2,3,4,16,18,21,22,23,24])) // returns "1-4, 16, 17, 21-24"
console.log(bookIndex([332, 476])) // returns "332, 476"
console.log(bookIndex([7, 8, 9, 10, 11])) // returns "7-11"
console.log(bookIndex([2, 7, 8, 9, 10, 11])) // returns "2, 7-11"
console.log(bookIndex([7, 8, 9, 10, 11, 23])) // returns "7-11, 23"

// ------------------------------------------------------------------------------------------