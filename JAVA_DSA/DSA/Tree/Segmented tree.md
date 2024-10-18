
> A segment tree is a type of Binary Tree which works or used in range of data it follows o( log n ) complexity
> It is also a full binary tree in which every node except the leaf node has two child 


## Segment tree quering has three cases:

1. when node at startdx > qurery Startindx  or endidx >= qEndIdx  return node.data
2. if node startIdx > qEidx or endIdx < qsi return 0 {out of bound case}
3. Overlapping case: return node.left,qsi,qei + node.right,qsi,qei

