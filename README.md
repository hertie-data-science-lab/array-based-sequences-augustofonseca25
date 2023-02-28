# CaesarCipher

The Caesar cipher involves replacing each letter in a message with the letter that is a certain number of letters after it in the alphabet. So, in an English message, we might replace each A with D, each B with E, each C with F, and so on, if shifting by three characters. We continue this approach all the way up to W, which is replaced with Z. Then, we let the substitution pattern wrap around, so that we replace X with A, Y with B, and Z with C.


* Given that strings are immutable, we cannot directly edit an instance to encrypt it.
Instead, our goal will be to generate a new string. A convenient technique for performing string transformations is to create an equivalent list of characters, edit the
list, and then reassemble a (new) string based on the list. 
* The first step can be performed by sending the string as a parameter to the constructor of the list class. For
example, the expression list( bird ) produces the result [ b , i , r , d ]
* Conversely, we can use a list of characters to build a string by invoking the join
method on an empty string, with the list of characters as the parameter. For example, the call .join([ b , i , r , d ]) returns the string bird .

* If we were to number our letters like array indices, so that A is 0, B is 1, C is 2,
and so on, then we can write the Caesar cipher with a rotation of r as a simple
formula: Replace each letter i with the letter (i + r) mod 26, where mod is the
modulo operator, which returns the remainder after performing an integer division.
This operator is denoted with % in Python, and it is exactly the operator we need
to easily perform the wrap around at the end of the alphabet. For 26 mod 26 is
0, 27 mod 26 is 1, and 28 mod 26 is 2. The decryption algorithm for the Caesar
cipher is just the opposite—we replace each letter with the one r places before it,
with wrap around (that is, letter i is replaced by letter (i−r) mod 26).


Sample Test
```
cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(message)
print("Secret: ", coded)
answer = cipher.decrypt(coded)
print("Message: ", answer)
```

Sample Output:
```
Secret:  WKH HDJOH LV LQ SODB; PHHW DW MRH'V
Message:  THE EAGLE IS IN PLAY; MEET AT JOE'S
```
