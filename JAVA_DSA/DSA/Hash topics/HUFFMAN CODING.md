
```java
import java.util.*;  
  
public class Huffman {  
    private HashMap<Character, String> encoder = new HashMap<>();  
    private HashMap<String, Character> decoder = new HashMap<>();  
  
    private class Node implements Comparable<Node> {  
        Character data;  
        int cost; // Frequency  
        Node left, right;  
  
        public Node(Character data, int cost) {  
            this.data = data;  
            this.cost = cost;  
            this.left = this.right = null;  
        }  
  
        // Compare based on cost (frequency)  
        @Override  
        public int compareTo(Node other) {  
            return this.cost - other.cost;  
        }  
    }  
  
    public Huffman(String feeder) throws Exception{  
        // Create a frequency map table  
        HashMap<Character, Integer> freqMap = new HashMap<>();  
        for (int i = 0; i < feeder.length(); i++) {  
            char cc = feeder.charAt(i);  
            if(freqMap.containsKey(cc)) {  
                int ov = freqMap.get(cc);  
                ov += 1;  
                freqMap.put(cc, ov);  
            } else {  
                freqMap.put(cc, 1);  
            }  
        }  
  
        // Create a priority queue (min-heap)  
        PriorityQueue<Node> minHeap = new PriorityQueue<>();  
        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {  
            Node node = new Node(entry.getKey(), entry.getValue());  
            minHeap.add(node);  
        }  
  
        // Build the Huffman tree  
        while (minHeap.size() > 1) {  
            Node first = minHeap.poll(); //REMOVES MIN COST  
            Node second = minHeap.poll(); //REMOVE MINIMUM COST  
            Node parent = new Node(null, first.cost + second.cost);  
            parent.left = first;  
            parent.right = second;  
            minHeap.add(parent); //AGAIN ADD TO MINHEAP  
        }  
  
        // Get the root of the Huffman tree  
        Node root = minHeap.poll();  
  
        // Generate encoder and decoder maps  
        buildEncoderDecoder(root, "");  
    }  
  
    private void buildEncoderDecoder(Node node, String path) {  
        if (node == null) {  
            return;  
        }  
  
        if (node.data != null) {  
            // Leaf node: map character to its binary representation  
            encoder.put(node.data, path);  
            decoder.put(path, node.data);  
        }  
  
        // Recurse for left and right children  
        buildEncoderDecoder(node.left, path + "0");  
        buildEncoderDecoder(node.right, path + "1");  
    }  
  
    public String encode(String source) {  
        StringBuilder encoded = new StringBuilder();  
        for (int i = 0; i < source.length(); i++) {  
            char cc = source.charAt(i);  
            encoded.append(encoder.get(cc));  
        }  
        return encoded.toString();  
    }  
  
    public String decode(String encoded) {  
        StringBuilder decoded = new StringBuilder();  
        String key = "";  
        for (int i = 0; i < encoded.length(); i++) {  
            key += encoded.charAt(i);  
            if (decoder.containsKey(key)) {  
                decoded.append(decoder.get(key));  
                key = "";  
            }  
        }  
        return decoded.toString();  
    }  
  
    public static void main(String[] args) {  
        try {  
            String feeder = "abbccda";  
            Huffman huffman = new Huffman(feeder);  
  
            String encoded = huffman.encode(feeder);  
            System.out.println("Encoded: " + encoded);  
  
            String decoded = huffman.decode(encoded);  
            System.out.println("Decoded: " + decoded);  
        } catch (Exception e) {  
            e.printStackTrace();  
        }  
    }  
}
```