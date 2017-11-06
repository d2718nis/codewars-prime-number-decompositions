Prime number decompositions
==========
Solution for the [codewars](https://www.codewars.com) challenge.
* Task description: https://www.codewars.com/kata/prime-number-decompositions/python


The Task
----------
### Get All Prime Factors

You have to code a function `get_all_prime_factors` which takes an integer as a parameter and returns a list containing its prime decomposition by ascending factors. If a factor appears multiple times in the decomposition it should appear as many time in the list.

### Get Unique Prime Factors With Count
You should also write `get_unique_prime_factors_with_count`, a function which will return a list containing two lists: one with prime numbers appearing in the decomposition and the other containing their respective power.

### Get Unique Prime Factors With Products

You should also write `get_unique_prime_factors_with_products` which returns a list containing the prime factors to their respective powers.

### Examples
`get_all_prime_factors(100)  # [2,2,5,5]`
`get_unique_prime_factors_with_count(100)  # [[2,5],[2,2]]`
`get_unique_prime_factors_with_products(100)  # [4,25]`

### Notes
#### Not Valid Cases
All three functions in these cases should return `[]`, `[[],[]]` and `[]` respectively:
 - `n` is not a number
 - `n` not an integer
 - `n` is negative or 0

#### Edge Cases
If `n=0`, functions should return `[]`, `[[],[]]` and `[]` respectively.
If `n=1`, functions should return `[1]`, `[[1],[1]]`, `[1]` respectively.
If `n=2`, functions should return `[2]`, `[[2],[1]]`, `[2]` respectively.

The result for `n=2` is normal. The result for `n=1` is arbitrary and has been chosen to return a useful result. The result for `n=0` is also arbitrary but cannot be chosen to be both useful and intuitive. (`[[0],[0]]` would be meaningful but won't work for general use of decomposition, `[[0],[1]]` would work but is not intuitive.)


Running Tests
----------
Tests are located in the `tests` directory. To run Prime decomposition related tests use `python -m unittest tests.test_prime`


Authors
----------
* **Denis Z.** &#8212; *Initial work* &#8212; [d2718nis](https://github.com/d2718nis)

See also the list of [contributors](https://github.com/d2718nis/codewars-give-me-a-diamond/contributors) who participated in this project.


Acknowledgments
----------
* [Wikipedia: Prime Factor](https://en.wikipedia.org/wiki/Prime_factor) &#8212; the prime numbers that divide that integer exactly
