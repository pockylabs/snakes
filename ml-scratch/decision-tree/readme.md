# Decision Tree

## Approach
**Train Algorithm := Build the tree**

* Start at the top node and at each node select the best split based on the best information gain.
* Greedy search: Loop over all features and over all thresholds (all possible feature values).
* Save the best split feature and split threshold at each node.
* Build the tree recursively.
* Apply some stopping criteria to stop growing. <br> e,g. here: maximum depth, minimum samples at node, no more class distribution in node.
* When we have a leaf node, store the most common class label of this node

**Predict := Traverse Tree**
* Traverse the tree recursively
* At each node look at the best split feature of the test feature vector x and go left or right <br> depending on ```x[feature_idx] <=threshold```
* When we reach the lead node we return the stored most common class label