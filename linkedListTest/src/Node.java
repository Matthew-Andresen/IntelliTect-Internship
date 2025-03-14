public class Node {
    int data;
    public Node next;

    public Node(int data, Node next){
        this.data = data;
        this.next = next;
    }

    public int getData(){
        return this.data;
    }

    @Override
    public String toString(){
        return "Node with data: " + data;
    }
}
