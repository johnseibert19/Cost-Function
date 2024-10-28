# Cost-Function
This is an expansion of research done by [Max Norfolk](https://mnorfolk03.github.io/) in 2020 to include the gamut of primitive recursive (PR) functions.
[You can view Max's work by clicking this sentence.](https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1478&context=rhumj)

The cost a postive integer *m* for *m > 1* is defined as the minimum of C<sub>S</sub>(a)+C<sub>S</sub>(b) such that *a* and *b* are positive integers and *m = a * b* for a primitive recursive function * &in; S. Regardless of *S*, C<sub>S</sub>(0) = 1 and C<sub>S</sub>(1) = 1. This function is similar to Kolmogorov complexity, however it is computable. 

<strike>UPDATE (5/15/2024): The function C({+, *, -}) in Norfolk's code holds experimentally to a version I wrote to check to see if pred(x) is logically equivalent. Experimentally, it holds for the first 2000 integers, likely indicating it holds for all Z.</strike>

<strike>UPDATE (6/19-21/2024): I have now checked for all Z up to 2 billion using a C program by Janis Iraids. It is likely true pred/successor are the only needed operations, which impacts A091333. A005245 fails, as shown in a 2008 C program by Martin Fuller. You can view it on OEIS.</strike> The same author showed that the conjecture does NOT hold in the same article! Way to not read the literature there!

UPDATE (6/7/2024): It has been brought to my attention this is actually called the Mahler-Popken complexity, which is A005245 on OEIS. Articles dating back to the 80s are cited on Kurt Mahler and Jan Popken's problem from 1953. This celebrated work has gone through many optimizations from the likes of Selfridge, Coppersmith, Fuller, et. al.

UPDATE (10/28/2024): I am hoping to do a runtime analysis on the naive implementations already done as well as the newly-optimized versions.
