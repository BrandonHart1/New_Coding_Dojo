// isPalindrome(str) -> input is a single string (str). function returns true if
// the input is a palindrome and false otherwise.
// a palindrome is a word or phrase that is the same forwards or backwards
// for this example, capitalization and other punctuation matter
// "racecar" is a palindrome
// "raCecar" is not (a capital C is not the same as a lowercase c)
// "race car" is not (the space doesn't match up with the E on the opposite side)

function isPalindrome(str) {
	for (var i = 0; i < str.length/2; i++) {
		if (str[i] == str[str.length - 1 - i]) {
			continue;
		}
	else {
		return false;
	}
	}
	
	return True
}

// what are our test cases?




// longestPalindrome(str) -> input is a string
// output is the longest palindrome contained within that string
// if you find multiple palindromes of the same length, return the first one
// that you find
// "ehjgkkgeh" -> "gkkg"
// "ehjg kkgeh" -> "kk"
// "qwertttreqwerewy" -> "ertttre"
// "qwerttttttreqwerewy" -> "erttttttre"
// "abacabd" -> "bacab"
// "abacaed" -> "aba"
// "abcde" -> "a" (every character is effectively its own palindrome)
// "a" -> "a" (lol)
// "I like to drive the racecar extremely fast" -> "e racecar e"
// "racecar" -> "racecar" (no need to use the previous function if you don't want to)


function longestPalindrome(str) {
	for (var i = 0; i < str.length/2; i++) {
		
	}

}