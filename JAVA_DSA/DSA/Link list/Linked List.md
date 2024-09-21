```java
public class LL {  
    private Node head;  
    private Node tail;  
    private int size;  
    private Node next;  
  
    public LL() {  
        this.size = 0;  
    }  
  
    private class Node {  
        private int val;  
        private Node next;  
  
        public Node(int val) {  
            this.val = val;  
        }  
  
        public Node(int val, Node next) {  
  
            this.val = val;  
            this.next = next;  
        }  
    }  
  
    public void add(int val) {  
        Node node = new Node(val);  
        node.next = head;  
        head = node;  
  
        if (tail == null) {  
            tail = head;  
        }  
        size += 1;  
    }  
  
    public void display() {  
        Node temp = head;  
        while (temp != null) {  
            System.out.print(temp.val + " -> ");  
            temp = temp.next;  
        }  
        System.out.println("null");  
    }  
  
    public void addLast(int val) {  
        if (tail == null) {  
            add(val);  
            return;  
        }  
        Node node = new Node(val);  
        tail.next = node;  
        tail = node;  
        size++;  
  
    }  
  
    public void insertbefore(int idx, int val) {  
        if (idx == 0) {  
            add(val);  
            return;  
        }  
        if (idx == size) {  
            addLast(val);  
            return;  
        }  
  
        Node temp = head;  
        for (int i = 1; i < idx; i++) {  
            temp = temp.next;  
        }  
  
        Node node = new Node(val, temp.next); // this is a constructor which declared above  
        temp.next = node;  
  
        size++;  
         
    }  
//    Delete from 1St nod  
  
    public int delFirst() {  
        int val = head.val;  
        head = head.next;  
  
        if (head.next == null) {  
            head = null;  
            tail = null;  
            size--;  
        }  
        return val;  
    }  
//    Get a node idx  
    public  Node get(int index){  
        Node node = head;  
  
        for (int i = 0; i < index; i++) {  
            node = node.next;  
  
        }  
        return node;  
    }  
  
    public int deleteLast() {  
        if (size <= 1) {  
            return delFirst();  
        }  
  
        Node secondLast = get(size - 2);  
        int val = tail.val;  
        tail = secondLast;  
        tail.next = null;  
        size--;  
        return val;  
    }  
    public int delanyIdx(int idx){  
        if (idx == 0) {  
            return delFirst();  
        }  
        if (idx == size - 1) {  
            return deleteLast();  
        }  
        Node prev = get(idx - 1);  
        int val = prev.val;  
        prev.next = prev.next.next;  
        return val;  
    }  
  
  
  
    public static void main(String[] args) {  
        LL list = new LL();  
  
        list.add(1);  
        list.addLast(2);  
  
        list.addLast(3);  
        list.display();  
        list.delanyIdx(1);  
  
     list.insertbefore(2, 4);  
  
  
          list.display();  
//        System.out.println(list.delFirst());  
//        System.out.println(list.deleteLast());  
    }  
}
```

# Leetcode q's

## Cycle detecction

```<>
/**

 * Definition for singly-linked list.

 * class ListNode {

 *     int val;

 *     ListNode next;

 *     ListNode(int x) {

 *         val = x;

 *         next = null;

 *     }

 * }

 */

public class Solution {

    public boolean hasCycle(ListNode head) {

        ListNode fast = head;

        ListNode sec = head;

  

        while(fast!=null && fast.next!=null){

            fast = fast.next.next; // fast move 2 steps

            s = s.next; //slow move 1 step

  

            if(fast == s){

                return true;

            }

        }

        return false;

    }

}
```


##Length of cycle 

```<>
/**

 * Definition for singly-linked list.

 * class ListNode {

 *     int val;

 *     ListNode next;

 *     ListNode(int x) {

 *         val = x;

 *         next = null;

 *     }

 * }

 */

public class Solution {

    public int countCycl(ListNode head) {

        ListNode fast = head;

        ListNode sec = head;

  

        while(fast!=null && fast.next!=null){

            fast = fast.next.next; // fast move 2 steps

            s = s.next; //slow move 1 step

  

            if(fast == s){

            ListNode temp=slow;

            int Length =0;

            do{

                temp=temp.next;

                length++;

            }while(temp!=s);

                return length;

            }

        }

        return 0;

    }

}
```

# Find from where the cycle starts

```<>
/**

 * Definition for singly-linked list.

 * class ListNode {

 *     int val;

 *     ListNode next;

 *     ListNode(int x) {

 *         val = x;

 *         next = null;

 *     }

 * }

 */

public class Solution {

  

    public int Len(ListNode head) {

        Node fast = head;

        Node s = head;

  

        while(fast!=null && fast.next!=null){

            fast = fast.next.next; // fast move 2 steps

            s = s.next; //slow move 1 step

  

            if(fast == s){

                ListNode temp=s;

                int length =0;

                do{

                    temp=temp.next;

                    length++;

                }while(temp!=s);

                return length;

  

            }

        }

        return 0;

    }

  

    public ListNode detectCycle(ListNode head) {

        int length = 0;

  

        Node fast = head;

        Node s = head;

  

        while (fast != null && fast.next != null) {

            fast = fast.next.next; // fast move 2 steps

            s = s.next; //slow move 1 step

  

            if (fast == s) {

                length = Len(s);

                break;

            }

            if (length==0){

                return null;

            }

  

            //move f by 1

  

            Node f = head;

            Node slow = head;

  

            // move slow pointer to the len of list

            while (length > 0) {

                slow = slow.next;

                length--;

            }

  

            //move both f and slow until they meet each other

            while (f != slow) {

                f = f.next;

                slow = slow.next;

            }

            return s;

  

        }

    }

}
```

## Find middle in a linked list

```<>
/**

 * Definition for singly-linked list.

 * public class ListNode {

 *     int val;

 *     ListNode next;

 *     ListNode() {}

 *     ListNode(int val) { this.val = val; }

 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }

 * }

 */

class Solution {

    public ListNode middleNode(ListNode head) {

        ListNode s = head;

        ListNode f = head;

  

        while(f !=null && f.next!=null){

            f=f.next.next;

            s=s.next;

        }

        return s;

    }

}
```

## Reverse of LinkedList

```<>
/**

 * Definition for singly-linked list.

 * public class ListNode {

 *     int val;

 *     ListNode next;

 *     ListNode() {}

 *     ListNode(int val) { this.val = val; }

 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }

 * }

 */

class Solution {

    public ListNode reverseList(ListNode head) {

  

        ListNode prev = null;

        ListNode Present = head;

        ListNode next = null;

  

        while(Present !=null){

           next = Present.next;

            Present.next = prev;

            prev = Present;

            Present = Present.next;

            Present = next;

        }

         return prev;

    }

}
```

## Reverse list b\w

```<>
/**

 * Definition for singly-linked list.

 * public class ListNode {

 *     int val;

 *     ListNode next;

 *     ListNode() {}

 *     ListNode(int val) { this.val = val; }

 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }

 * }

 */

class Solution {

    public ListNode reverseBetween(ListNode head, int left, int right) {

         if (left == right) {

            return head;

        }

  

        // skip the first left-1 nodes

        ListNode current = head;

        ListNode prev = null;

        for (int i = 0; current != null && i < left - 1; i++) {

            prev = current;

            current = current.next;

        }

  

        ListNode last = prev;

        ListNode newEnd = current;

  

        ListNode next = current.next;

        for (int i = 0; current != null && i < right - left + 1; i++) {

            current.next = prev;

            prev = current;

            current = next;

            if (next != null) {

                next = next.next;

            }

        }

  

        if (last != null) {

            last.next = prev;

        } else {

            head = prev;

        }

  

        newEnd.next = current;

        return head;

    }

}
```

```
/**

 * Definition for singly-linked list.

 * public class ListNode {

 *     int val;

 *     ListNode next;

 *     ListNode() {}

 *     ListNode(int val) { this.val = val; }

 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }

 * }

 */

class Solution {

    public ListNode reverseBetween(ListNode head, int left, int right) {

        if(left == right){

            return head;

        }

        ListNode curr = head;

        ListNode prev = null;

        for(i=0;i<left-1 && curr!=null;i++){

            prev = curr;

            curr = curr.next;

        }

        ListNode last = prev;

        ListNode n = curr;

        ListNode next = curr.next;

        for(i=0;i<right-left+1 && curr!=null;i++){

            next = curr.next;

            prev = curr;

  

            curr = curr.next;

  

            curr = next;

    }

  

    if(last!=null){

        last = last.next;

    }

    head = prev;

  
  

    }

}
```

```<>
public class LinkedRev {  
    static class Node{  
        Node head;  
        Node nextNode;  
        Node prev;  
        int data;  
        Node next;  
        public Node(int data){  
            this.data = data;  
        }  
}  
        public static Node listrevr(Node head) {  
            Node curr = head;  
            Node prev = null;  
            Node next;  
  
        while(curr != null){  
                //store next of curr node  
  
                next = curr.next;  
                //this will change dir <-  
                curr.next = prev;  
  
                //move pointer by 1  
                prev = curr;  
                curr = next;  
            }  
            return prev;  
        }  
  
        //Reversing kth group in a node  
        static int length(Node head){  
        Node curr = head;  
        int count = 0;  
        while(curr != null){  
            curr = curr.next;  
            count++;  
        }  
        return count;  
        }  
  
  
    static Node reversegroup(Node head, int k) {  
        Node curr = head;  
        Node nextNode = null;  
        Node prev = null;  
  
        // Count the number of nodes in the linked list  
        int N = length(head);  
        int groups = N / k;  // Total number of full groups  
  
        Node prevTail = null;  // The tail of the previous group  
        Node newHead = null;   // The new head of the reversed list  
  
        // Reverse each group        for (int i = 0; i < groups; i++) {  
            Node groupHead = curr;  // Head of the current group  
            Node groupPrev = null;  // Reversed group's previous node  
  
            // Reverse `k` nodes            for (int j = 0; j < k && curr != null; j++) {  
                nextNode = curr.next;  
                curr.next = groupPrev;  
                groupPrev = curr;  
                curr = nextNode;  
            }  
  
            // If this is the first group, update the new head  
            if (newHead == null) {  
                newHead = groupPrev;  
            }  
  
            // Connect the tail of the previous group to the head of the reversed group  
            if (prevTail != null) {  
                prevTail.next = groupPrev;  
            }  
  
            // The current group's head becomes the tail for the next group  
            prevTail = groupHead;  
        }  
  
        // Attach the remaining part of the list (if any) to the last group's tail  
        if (prevTail != null) {  
            prevTail.next = curr;  
        }  
  
        return newHead;  
    }  
  
  
  
    // Utility function to print the linked list  
    static void printList(Node head) {  
        Node curr = head;  
        while (curr != null) {  
            System.out.print(curr.data + " ");  
            curr = curr.next;  
        }  
        System.out.println();  
    }  
  
    public static void main(String[] args) {  
        // Creating the linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6  
        Node head = new Node(1);  
        head.next = new Node(2);  
        head.next.next = new Node(3);  
        head.next.next.next = new Node(4);  
        head.next.next.next.next = new Node(5);  
        head.next.next.next.next.next = new Node(6);  
        head.next.next.next.next.next.next = new Node(7);  
  
  
        System.out.print("Given Linked List: ");  
        printList(head);  
  
        // Reverse the linked list in groups of 3  
        head = reversegroup(head, 3);  
  
        System.out.print("Reversed in Groups of 3: ");  
        printList(head);  
    }  
  
  
}
```