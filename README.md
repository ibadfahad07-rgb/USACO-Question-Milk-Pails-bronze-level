## usaco-bronze-milk-pails

Link : https://usaco.org/index.php?page=viewproblem2&cpid=1116

## Problem Statment :

Farmer John has received an order for exactly M units of milk (1≤M≤1,000) that he needs to fill right away. Unfortunately, his fancy milking machine has just become broken, and all he has are three milk pails of integer sizes X, Y, and M (1≤X<Y<M). All three pails are initially empty. Using these three pails, he can perform any number of the following two types of operations:

- He can fill the smallest pail (of size X) completely to the top with X units of milk and pour it into the size-M pail, as long as this will not cause the size-M pail to overflow.

- He can fill the medium-sized pail (of size Y) completely to the top with Y units of milk and pour it into the size-M pail, as long as this will not cause the size-M pail to overflow.

Although FJ realizes he may not be able to completely fill the size-M pail, please help him determine the maximum amount of milk he can possibly add to this pail.

**INPUT FORMAT (file pails.in):**

The first, and only line of input, contains X, Y, and M, separated by spaces.

**OUTPUT FORMAT (file pails.out):**

Output the maximum amount of milk FJ can possibly add to the size-M pail.

**SAMPLE INPUT:**
17 25 77

**SAMPLE OUTPUT:**
76

In this example, FJ fills the pail of size 17 three times and the pail of size 25 once, accumulating a total of 76 units of milk.

Problem credits: Brian Dean

## Algorithm :

1. Set best = 0.
2. For i = 0 to M/X (number of times the X pail is poured in):
3. For j = 0 to M/Y (number of times the Y pail is poured in):
4. Compute total = i*X + j*Y.
5. If total ≤ M and total > best, set best = total.
6. Print best.

## Explanation

Since FJ can only pour whole X-sized or whole Y-sized pails into the big pail, the final amount of milk in the size-M pail always comes down to some combination of "i full pails of X" plus "j full pails of Y." Because M is small (at most 1,000), we don't need anything clever here — we can just try every reasonable number of X-pours and every reasonable number of Y-pours, add them up, and see which combination gets us closest to M without going over. We start i and j at 0 and stop once i*X or j*Y alone would already exceed M, since going further would just waste pours. For every valid combination we check whether it fits under M, and if it's the best one we've seen so far, we save it. By the time we've checked every combination, we're guaranteed to have found the highest amount of milk FJ can add without overflowing.
