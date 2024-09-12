
```java
public class DLL {
    private Node head;
    private Node tail;
    private int size;
        public DLL(){
            this.size=0;
        }

    public class Node{
        private Node next;
        private Node prev;
        int val;
        public Node(int val){
            this.val = val;
        }
        public Node(int val, Node next,Node prev){
            this.val = val;
            this.next = next;
            this.prev = null;
        }
    }
    public void insert(int val){
        Node node = new Node(val);

        node.next=head;
        node.prev=null;
        if (head !=null){
            head.prev=node;
        }
        head = node;
        size++;

    }
    public void insertLast(int val){
            Node node = new Node(val);
            Node temp = head;
            node.next=null;
            if (head == null){ //check if head is null then head=node and it's prev to null and also next to null
                node.prev=null;
                head = node;
                return;
            }
            while (temp.next != null){
                temp = temp.next;
            }
            temp.next = node;
            node.prev=temp;
            size++;
    }
    public Node find(int val){
            Node node = head;
            while (node != null){
                if (node.val==val){
                    return node;
                }
                node = node.next;
            }
            return null;
    }
    public void addAt(int after,int val){
            Node node = new Node(val);
            Node prev = find(after);
            if (prev == null){
                insert(val);
            }
            node.next=prev.next;
            prev.next=node;
            node.prev=prev;

            if (node.next != null){
                node.next.prev=node;
            }
            size++;
    }
    public void display(){
            Node  node = head;
            while (node!=null){
                System.out.print(node.val+" ->");
                node = node.next;
            }
        System.out.print("null");
    }


    public static void main(String[] args) {
        DLL list = new DLL();
        list.insert(5);
        list.insert(6);
        list.insert(4);
        list.insertLast(7);
      list.addAt(6,77);
        list.display();
    }


}

```
