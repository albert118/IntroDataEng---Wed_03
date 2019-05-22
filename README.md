# Introduction to Data Engineer, Group: Wed_03
## UTS Project - Assessment 2, Machine Learning / Stochastic Optimization (30%)

### Problem Statement:
*Utilise the PBIL algorithm (essentially a basic genetic algorithm in this case) to stochasticlly optimise the concentrator - terminal problem.*

### Background Reading
* Differences between Epoch, Batch and Mini-Batch: https://stats.stackexchange.com/questions/117919/what-are-the-differences-between-epoch-batch-and-minibatch
* Population Based Incremental Learning heuristics, algorithmic definition and further resources: http://www.cleveralgorithms.com/nature-inspired/probabilistic/pbil.html
* Original paper introducing PBIL: https://www.ri.cmu.edu/pub_files/pub1/baluja_shumeet_1994_2/baluja_shumeet_1994_2.pdf


### IntroData Assesment Explanation of PBIL ('simply')
PBIL is a simple stochastic/genetic algorithm for optimizing a configuration.

* A description of the solution space by means of a "binary string"
* A probability vector that is the same length as the "binary string, where each location indicates the likelihood of that binary digit in the solution string being `TRUE` or `FALSE`.
* A means of calculating a "Cost" from that "binary string", in this case using the given Cost Table

The algorithm proceeds as follows:
#### Step 1: Creating an epoch of sample solutions
Create a number of sample solutions based on the probability vector (solution set). This is called an epoch and could have any number of solutions, perhaps 100 (i.e. this is an arbitrary choice...).
* Each sample solution a "binary strings".
** Say the Nth element of the Probability Vector is 0.5, then the Nth element of the binary string would be equally likely to be a "1" or "0"
* Say the Nth element of the Probability Vector is 0.667, then the Nth element of the binary string would be a "1" on 66% of the trials
* Say the Nth element of the Probability Vector is 1, then the Nth element of the binary string would always be a "1"
* Say the Nth element of the Probability Vector is 0.0, then the Nth element of the binary string would never be a "1"
* And so on for all the elements of the binary string
Check that all the solutions found do not abrogate the constraints (e.g. max number of terminal connections to a concentrator is 3)
#### Step 2: Working out the costs
Now that you have an epoch of sample solutions, which are just "binary strings", you have to calculate the Cost of each solution.
Use your cost table, with each sample solution to calculate the Cost of that particular solution.
#### Step 3: Ranking the epoch
Based on the costs calculated above, find the minimum one
* You could do this by ranking them.
* Now take the minimum one and use it in the next step
#### Step 4: Updating the Probability Vector
You now have a "binary string" that represents the best solution of your epoch of possible solutions, use it to modify the Probability Vector so that the next epoch you create will be more similar to this best (fittest) solution found in Step 3.
* So, if element N was a "1" then the corresponding Nth element of the Probability Vector needs to be adjusted by a small amount so that in the next epoch, the Nth elements of the sample solutions are more likely to be a "1", and so on for all the elements
#### Step 5: Go back and do it again
* Return to Step 1: and create another epoch of solutions
* Proceed through Steps 2, 3 and 4 as before
**Inspect your Probability Vector.** It should start to look more like a string of "1s" and "0s" each time you go around the process.
When the Probability Vector has finally settled (converged) as a string of "1s" and "0s", you know you have a solution (*hopefully a globally minimised cost and not just a local one!*).
This is then the same as a sample solution, and you can use it to work back and show your configuration. 
**Voila!!**
