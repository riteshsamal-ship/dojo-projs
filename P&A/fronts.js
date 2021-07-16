class Node {
    constructor(value) {
        this.value = value;
        this.next = null
    }
}
class SLL {
    constructor() {
        this.head = null;
    }
    addFront(value) {
        
        var newNode = new Node(value);

        newNode.next = this.head;

        this.head = newNode;

        return this.head;
    }

    removeFront() {
 
        if(this.head) {
            this.head = this.head.next;
        }
        return this.head;
    }

    front() {
 
        if(this.head) {
            return this.head.value;
        }
        return null;
    }
}