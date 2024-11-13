## What is heap ?

```
A heap is a complete binary tree data structure that satisfies the heap property: for every node, the value of its children is greater than or equal to its own value. Heaps are usually used to implement priority queues, where the smallest (or largest) element is always at the root of the tree.
```

> A heap is like a **binary**  tree where child >=  parent node
> It's a [complete](https://www.geeksforgeeks.org/complete-binary-tree/) binary tree

## 2 types of heap 

1. Max-heap : root > child
2. Min-heap : root < child

## Time complexity

> For insertion  = n(logn)
> For deletion = o(n logn)

## Heap insertion and deletion code

```java
import java.util.ArrayList;  
  
public class Heap {  
  
    private ArrayList<Integer> list;  
    public Heap() {  
        list = new ArrayList<>();  
    }  
  
    private void swap(int first,int last){  
    int  temp = list.get(first);  
    list.set(first,list.get(last));  
    list.set(last,temp);  
    }  
  
    int parent(int  index){  
        return (index - 1) / 2;  
    }  
  
    int left(int  index){  
        return 2 * index + 1;  
    }  
    int right(int  index){  
        return 2 * index + 2;  
    }  
  
    //INSERTION  
    public void insert(int value){  
    list.add(value);  
    uphead(list.size()-1);  
    }  
    private void uphead(int index){  
        if(index == 0){  
            return;  
        }  
        int parent = parent(index);  
        //COOMPARE THE CURRENT VAL WITH PARENT  
        if(list.get(index) < list.get(parent)){  
            swap(index, parent);  
            uphead(parent);  
        }  
    }  
    public int remove() throws Exception {  
        if (list.isEmpty()){  
            throw new Exception("Heap is empty");  
        }  
        int temp = list.get(0);  
        int last = list.remove(list.size()-1);  
        if(!list.isEmpty()){  
            list.set(0,last);  
            downhead(0);  
        }  
  
        return temp;  
    }  
  
    private void downhead(int index) {  
        int min = index;  
        int left = left(index);  
        int right = right(index);  
  
        if (left < list.size() && list.get(min) > list.get(left)){  
            min = left;  
        }  
        if (right < list.size() && list.get(min) > list.get(right)) {  
            min = right;  
        }  
        if (min != index) {  
            swap(min, index);  
            downhead(min);  
        }  
    }  
    public ArrayList<Integer> heapSort() throws Exception {  
        ArrayList<Integer> sortedData = new ArrayList<>();  
        while (!list.isEmpty()) {  
            sortedData.add(this.remove());  
        }  
        return sortedData;  
    }  
  
  
    public void main(String[] args) throws Exception {  
        Heap heap = new Heap();  
  
        heap.insert(10);  
        heap.insert(5);  
        heap.insert(30);  
        heap.insert(3);  
        heap.insert(7);  
        heap.remove();  
        System.out.println("Heap Sort: " + heap.heapSort());  // Outputs a sorted list  
    }  
}
```