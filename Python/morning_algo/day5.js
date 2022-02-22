// swapPairs(arr)
// consider every item in the array to be grouped into pairs, i.e.
// the array [3, 7, 2, 9, 1, 5] is made up of three pairs:
// 3 and 7 / 2 and 9 / 1 and 5
// swap each pair in the array in-place; for the above array, we want
// to end up with:
// [7, 3, 9, 2, 5, 1]
// if there's an odd item left over at the end, it's not part of a pair
// so we don't swap it

function swapPairs(arr) {
    for(var i = 0; i < arr.lenght - 1; i += 2){
        var temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        console.log(i);
    }
}

let test_one = [0, 1, 2, 3, 4, 5];
swapPairs(test_one);
console.log(test_one); // should display [1, 0, 3, 2, 5, 4]

let test_two = ['Aleks', 'Brittani', 'Charlie', 'Diana', 'Elon'];
swapPairs(test_two);
console.log(test_two); // should display ['Brittani', 'Aleks', 'Diana', 'Charlie', 'Elon']