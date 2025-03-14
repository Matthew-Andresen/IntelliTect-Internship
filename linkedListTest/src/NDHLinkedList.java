public class NDHLinkedList implements NDHLinkedListInterface{
    int size;
    Node head;

    public NDHLinkedList(){
        size = 0;
        head = null;
    }

    public NDHLinkedList(int[] data){
        for(int num : data){
            this.addLast(num);
        }
    }

//-Adding Methods---------------------------------------------------------------------------------------
    public void addFirst(int data){
        head = new Node(data, head);
        size ++;
    }

    public void addLast(int data){
        Node newNode = new Node(data, null);

        if(size == 0){
            head = newNode;
        }

        else{
            Node curr = head;

            while(curr.next != null){
                curr = curr.next;
            }

            curr.next = newNode;
        }

        size ++;
    }

    public void addAtIndex(int index, int data){
        if(index < 0){
            throw new IllegalArgumentException("Index out of bounds");
        }
        else if(index >= size){
            this.addLast(data);
        }
        else {
            Node newNode = new Node(data, null);
            int pos = 0;
            Node curr = head;

            while (pos < index - 1) {
                curr = curr.next;
                pos++;
            }

            newNode.next = curr.next;
            curr.next = newNode;
            size ++;
        }
    }

//-Removing Methods-------------------------------------------------------------------------------------
    public void removeFirst(){
        if(size == 0){
            throw new IllegalStateException("List is empty");
        }
        head = head.next;
        size --;
    }

    public void removeLast(){
        if(size == 0){
            throw new IllegalStateException("List is empty");
        }
        if(size > 1){
            Node curr = head;

            while(curr.next.next != null){
                curr = curr.next;
            }
            curr.next = null;
            size --;
        }
        else{
            head = null;
            size = 0;
        }
    }

    public void removeAtIndex(int index){
        if(index < 0 || index > size - 1){
            throw new IllegalArgumentException("Index out of bounds");
        }
        else if(index == size - 1){
            this.removeLast();
        }
        else{
            int pos = 0;
            Node curr = head;

            while(pos < index - 1){
                curr = curr.next;
                pos ++;
            }

            curr.next = curr.next.next;
            size --;
        }
    }

//-Util Methods---------------------------------------------------------------------------------------
    public Node getAtIndex(int index){
        if(index < 0 || index > size - 1){
            throw new IllegalArgumentException("Index out of bounds");
        }

        int pos = 0;
        Node curr = head;

        while(pos != index){
            curr = curr.next;
            pos ++;
        }
        return curr;
    }

    public int search(int data){
        if(head.getData() == data){
            return 0;
        }

        int pos = 0;
        Node curr = head;

        while(curr.next != null){
            if(curr.getData() == data){
                return pos;
            }
            curr = curr.next;
            pos ++;
        }

        return -1;
    }

    public boolean isEmpty(){
        return size == 0;
    }

    @Override
    public String toString(){
        if(!isEmpty()){
            Node curr = head;
            StringBuilder result = new StringBuilder("[" + curr.data);
            curr = curr.next;
            for(int i = 1; i < size; i++){
                result.append(", ").append(curr.getData());
                curr = curr.next;
            }

            return result + "]";
        }
        return "Empty List";
    }

    public int getSize(){
        return this.size;
    }

}
