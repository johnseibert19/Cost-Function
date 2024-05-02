# Cost-Function
This is an expansion of research done by [Max Norfolk](https://mnorfolk03.github.io/) in 2020 to include the gamut of primitive recursive (PR) functions.
[You can view Max's work by clicking this sentence.](https://scholar.rose-hulman.edu/cgi/viewcontent.cgi?article=1478&context=rhumj)

The cost a postive integer *m* for *m > 1* is defined as the minimum of C<sub>S</sub>(a)+C<sub>S</sub>(b) such that *a* and *b* are positive integers and *m = a * b* for a primitive recursive function * &in; S. Regardless of *S*, C<sub>S</sub>(0) = 1 and C<sub>S</sub>(1) = 1. This function is similar to Kolmogorov complexity, however it is computable. 

UPDATE (5/2/2024): I have figured out what the "subtract" business going on in Max's code is doing. The newly added function, pred(x), achieves a similar effect as the approach taken in his code involves going through the indices in descending order while establishing changes for subsequent indices. Mine doesn't use an iterator, while his does. The result, when taking out the operational costs in the definition, is the same.
