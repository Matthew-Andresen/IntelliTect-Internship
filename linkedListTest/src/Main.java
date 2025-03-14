public class Main {
    public static void main(String[] args) {
// Create a NDHLinkedList instance
        NDHLinkedList list = new NDHLinkedList();
// Test isEmpty() - should return true initially
        System.out.println("Is the list empty? " + list.isEmpty());
// Test addFirst() - adding to the first position
        list.addFirst(10);
        list.addFirst(20);
        System.out.println("After adding 10 and 20 to the front: " +
                list.toString());
// Test addLast() - adding to the last position
        list.addLast(30);
        System.out.println("After adding 30 to the end: " + list.toString());
// Test removeFirst() - removing the first node
        list.removeFirst();
        System.out.println("After removing the first element: " + list.toString());
// Test removeLast() - removing the last node
        list.removeLast();
        System.out.println("After removing the last element: " + list.toString());
// Test search() - searching for an element in the list
        try {
            int position = list.search(10);
            System.out.println("Found 10 at position: " + position);
        } catch (IllegalStateException e) {
            System.out.println("Error: " + e.getMessage());
        }
// Test removeAtIndex() - removing node at a specific index
        try {
            list.removeAtIndex(0);
            System.out.println("After removing node at index 0: " +
                    list.toString());
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
// Test addAtIndex() - adding a node at a specific index
        list.addAtIndex(0, 15);
        System.out.println("After adding 15 at index 0: " + list.toString());
// Test isEmpty() - should return false now that list is not empty
        System.out.println("Is the list empty? " + list.isEmpty());
// Test toString() - print the current list
        System.out.println("Current list: " + list.toString());
// Edge case - test removing from an empty list
        list.removeFirst();
        list.removeLast();
        System.out.println("After removing all elements: " + list.toString());
// Edge case - searching in an empty list
        try {
            list.search(10);
        } catch (IllegalStateException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}