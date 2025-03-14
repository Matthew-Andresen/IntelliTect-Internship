public interface NDHLinkedListInterface{
    /*
        Appends a node to the beginning of the list
        @Param takes in an int as data to be put into the new node
        @Return void
     */
    void addFirst(int data);

    /*
        Appends a node to the end of the list
        @Param takes in an int as data to be put into the new node
        @Return void
     */
    void addLast(int data);
//-------------------------------------------------------------------------------------
    /*
        Removes the first node from the list
        @Return void
        @Throws IllegalStateException if list is empty
     */
    void removeFirst() throws IllegalStateException;

    /*
        Removes the last node from the list
        @Return void
        @Throws IllegalStateException if list is empty
     */
    void removeLast() throws IllegalStateException;
//-------------------------------------------------------------------------------------
    /*
        Prints the list as a string
        @Returns a string in the format [data, data, data,..., data]
        @Returns 'Empty List' if list isEmpty()
     */
    @Override
    String toString();

    /*
        Searches for the first instance of the data in the node
        @Param data to search for
        @Return int index where first occurrence of data is, -1 if data was not found
     */
    int search(int data);

//-------------------------------------------------------------------------------------
    /*
        Gets a node at a given index
        @Param int index to get
        @Return Node at index
        @Throws IllegalArgumentException if index is out of bounds
     */
    Node getAtIndex(int index) throws IllegalArgumentException;

    /*
        Adds a node at a given index
        @Param (int data to be added, int index to add at)
        @Return void
        @Throw IllegalArgumentException if index is out of bounds
     */
    void addAtIndex(int data, int index) throws IllegalArgumentException;

    /*
        Removes a node at given index and recouples the nodes together
        @Param int index to be removed
        @Return void
        @Throw IllegalArgumentException if index is out of bounds
     */
    void removeAtIndex(int index) throws IllegalArgumentException;

    /*
        Returns true if the list is empty, false if it is not.
     */
    boolean isEmpty();

}