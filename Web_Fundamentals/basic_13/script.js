// // Print 1-255
// Print1To255()
// Print all the integers from 1 to 255. 

function print1To255() {
    for(i = 1; i <= 255; i++)
    console.log(i)
}
print1To255()


// ###########################################################
// 2. Print Odds 1-255
// PrintOdds1To255()
// Print all odd integers from 1 to 255. 

function printOdds1To255() {
    for (i = 1; i <= 255; i++) {
        if (i % 2 !=0) {
            console.log(i);
        }
    }
}
printOdds1To255();


// ###########################################################
// 3. Print Ints and Sum 0-255
// PrintIntsAndSum0To255()
// Print integers from 0 to 255, and with each integer print the sum so far. 

function printIntsAndSum0To255() {
    var number = 0
    for(var i = 0; i <= 255; i++) {
        number = number + i
        console.log(i)
        console.log(number)
    }
}

printIntsAndSum0To255();

// ###########################################################
// 4. Iterate and Print Array
// Iterate through a given array, printing each value. 
// PrintArrayVals(arr)
arr = [1, 2, 3, 4, 5, 6, 7];
for(var i = 0, i > arr.length; i++) {
    console.log(i)
}


// ###########################################################
// 5. Find and Print Max
// PrintMaxOfArray(arr)
// Given an array, find and print its largest element. 




// ###########################################################
// 6. Get and Print Average
// PrintAverageOfArray(arr)
// Analyze an array’s values and print the average. 



// ###########################################################
// 7. Array with Odds
// ReturnOddsArray1To255()
// Create an array with all the odd integers between 1 and 255 (inclusive).  



// ###########################################################
// 8. Square the Values
// SquareArrayVals(arr)
// Square each value in a given array, returning that same array with changed values. 



// ###########################################################
// 9. Greater than Y
// ReturnArrayCountGreaterThanY(arr, y)
// Given an array and a value Y, count and print the number of array values greater than Y. 



// ###########################################################
// 10. Zero Out Negative Numbers
// ZeroOutArrayNegativeVals(arr)
// Return the given array, after setting any negative values to zero. 



// ###########################################################
// 11. Max, Min, Average
// PrintMaxMinAverageArrayVals(arr)
// Given an array, print the max, min and average values for that array.



// ###########################################################
// 12. Shift Array Values
// ShiftArrayValsLeft(arr)
// Given an array, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the array.



// ###########################################################
// 13. Swap String For Array Negative Values
// SwapStringForArrayNegativeVals(arr)
// Given an array of numbers, replace any negative values with the string 'Dojo'.







