
```java
public class LL {  
    private Node head;  
    private Node tail;  
    private int size;  
    private Node next;  
  
    public LL() {  
        this.size = 0;  
    }  
    private class Node{  
        private int val;  
        private Node next;  
  
    public Node(int val){  
        this.val = val;  
    }  
    public Node(int val, Node next){  
  
    this.val = val;  
    this.next = next;  
    }  
    }  
  
    public void  add(int val){  
        Node node = new Node(val);  
        node.next = head;  
        head = node;  
  
        if (tail == null) {  
            tail = head;  
        }  
        size += 1;  
    }  
    public void display(){  
        Node temp = head;  
        while (temp != null) {  
            System.out.print(temp.val + " -> ");  
            temp = temp.next;  
        }  
        System.out.println("null");  
    }  
    public void addLast(int val){  
        if (tail == null) {  
            add(val);  
            return;  
        }  
        Node node = new Node(val);  
        tail.next = node;  
        tail = node;  
        size++;  
  
    }  
    public void insertbefore(int idx,int val){  
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
  
        Node node = new Node(val, temp.next);  
        temp.next = node;  
  
        size++;  
    }  
//    Delete from 1St nod  
  
    public int delFirst(){  
        int val = head.val;  
        head = head.next;  
  
        if (head.next==null){  
            head=null;  
            tail=null;  
            size --;  
        }  
        return val;  
  
    }  
    public int delLast(){  
        int value = tail.val;  
        if (tail.next==null){  
            tail = null;  
              
        }  
    }  
  
  
    public static void main(String[] args) {  
        LL list = new LL();  
  
        list.add(1);  
        list.addLast(2);  
  
        list.addLast(3);  
  
        list.insertbefore(2, 4);  
  
  
        list.display();  
        System.out.println(list.delFirst());  
    }  
}
```