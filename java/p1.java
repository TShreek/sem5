// Shared buffer class
class Buffer {
    private int[] buffer; // Array to hold the buffer's items
    private int count = 0; // Number of items currently in the buffer
    private int size; // Maximum capacity of the buffer
    private int in = 0; // Index for inserting items into the buffer (write index)
    private int out = 0; // Index for removing items from the buffer (read index)

    // Constructor to initialize the buffer with a given size
    public Buffer(int size) {
        this.size = size; // Set the maximum buffer size
        this.buffer = new int[size]; // Initialize the buffer array
    }

    // Produce an item and add it to the buffer
    public synchronized void produce(int item) {
        // Wait if the buffer is full
        while (count == size) {
            try {
                wait(); // Wait for space in the buffer
            } catch (InterruptedException e) {
                return; // Exit gracefully if interrupted
            }
        }
        buffer[in] = item; // Add the item at the current write index
        in = (in + 1) % size; // Move to the next index, circularly
        count++; // Increase the count of items in the buffer
        System.out.println("Producer produced: " + item); // Output the produced item
        notifyAll(); // Notify all waiting threads that an item was produced
    }

    // Consume an item from the buffer
    public synchronized int consume() {
        // Wait if the buffer is empty
        while (count == 0) {
            try {
                wait(); // Wait for items to consume
            } catch (InterruptedException e) {
                return -1; // Exit gracefully if interrupted
            }
        }
        int item = buffer[out]; // Get the item from the current read index
        out = (out + 1) % size; // Move to the next index, circularly
        count--; // Decrease the count of items in the buffer
        System.out.println("Consumer consumed: " + item); // Output the consumed item
        notifyAll(); // Notify all waiting threads that an item was consumed
        return item; // Return the consumed item
    }
}

// Producer class - Produces items and adds them to the buffer
class Producer implements Runnable {
    private Buffer buffer; // Shared buffer object
    private int maxItems; // Maximum number of items the producer will produce

    // Constructor to initialize the producer with a buffer and max items to produce
    public Producer(Buffer buffer, int maxItems) {
        this.buffer = buffer; // Set the buffer
        this.maxItems = maxItems; // Set the maximum number of items to produce
    }

    // Run method, executed when the thread starts
    @Override
    public void run() {
        // Produce items and add them to the buffer
        for (int i = 1; i <= maxItems; i++) {
            buffer.produce(i); // Call produce method to add item to the buffer
            try {
                Thread.sleep(500); // Simulate production time by sleeping for 500 ms
            } catch (InterruptedException e) {
                return; // Exit gracefully if interrupted
            }
        }
    }
}

// Consumer class - Consumes items from the buffer
class Consumer implements Runnable {
    private Buffer buffer; // Shared buffer object

    // Constructor to initialize the consumer with a buffer
    public Consumer(Buffer buffer) {
        this.buffer = buffer; // Set the buffer
    }

    // Run method, executed when the thread starts
    @Override
    public void run() {
        // Continuously consume items until interrupted
        while (true) {
            int item = buffer.consume(); // Call consume method to get an item from the buffer
            if (item == -1) break; // Exit if interrupted (item is -1)
            try {
                Thread.sleep(1000); // Simulate consumption time by sleeping for 1000 ms
            } catch (InterruptedException e) {
                return; // Exit gracefully if interrupted
            }
        }
    }
}

// Main class - Coordinates the producer and consumer threads
public class p1 {
    public static void main(String[] args) {
        int bufferSize = 5; // Maximum capacity of the buffer
        int maxItemsToProduce = 10; // Number of items to produce

        // Create a shared buffer with the specified size
        Buffer buffer = new Buffer(bufferSize);

        // Create the producer and consumer threads
        Thread producerThread = new Thread(new Producer(buffer, maxItemsToProduce)); // Create producer thread
        Thread consumerThread = new Thread(new Consumer(buffer)); // Create consumer thread

        // Start the producer and consumer threads
        producerThread.start(); 
        consumerThread.start(); 

        // Wait for the producer thread to finish producing all items
        try {
            producerThread.join(); // Ensure the main thread waits for the producer to finish
        } catch (InterruptedException e) {
            // Handle any interruptions gracefully
        }

        // Stop the consumer thread gracefully by interrupting it
        consumerThread.interrupt(); 
        System.out.println("Producer-Consumer process completed."); // Output completion message
    }
}
