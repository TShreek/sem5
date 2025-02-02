
class SharedBuffer {
    int[] buffer;
    int size;
    int in = 0, out = 0, count = 0;

    public SharedBuffer(int size) {
        this.size = size;
        buffer = new int[size];
    }

    public synchronized void produce(int item) {
        while (count == size) {
            try {
                wait(); // Wait if buffer is full
            } catch (InterruptedException e) {
                return;
            }
        }
        buffer[in] = item;
        in = (in + 1) % size;
        count++;
        System.out.println("Produced: " + item);
        notifyAll(); // Notify consumer
    }

    public synchronized void consume() {
        while (count == 0) {
            try {
                wait(); // Wait if buffer is empty
            } catch (InterruptedException e) {
                return;
            }
        }
        int item = buffer[out];
        out = (out + 1) % size;
        count--;
        System.out.println("Consumed: " + item);
        notifyAll(); // Notify producer
    }
}

class Producer implements Runnable {
    private SharedBuffer sb;
    private int max;

    public Producer(SharedBuffer sb, int max) {
        this.sb = sb;
        this.max = max;
    }

    @Override
    public void run() {
        for (int i = 0; i < max; i++) {
            sb.produce(i);
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                return;
            }
        }
    }
}

class Consumer implements Runnable {
    private SharedBuffer sb;

    public Consumer(SharedBuffer sb) {
        this.sb = sb;
    }

    @Override
    public void run() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                sb.consume();
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
            System.out.println("Consumer thread interrupted.");
        }
    }
}

public class p7 {
    public static void main(String[] args) {
        int bufSize = 5;
        int toProduce = 10;

        SharedBuffer sb = new SharedBuffer(bufSize);
        Thread producerThread = new Thread(new Producer(sb, toProduce));
        Thread consumerThread = new Thread(new Consumer(sb));

        producerThread.start();
        consumerThread.start();

        try {
            producerThread.join(); // Wait for producer to finish
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Interrupt consumer safely
        consumerThread.interrupt();
        System.out.println("Producer - Consumer threads exiting.");
    }
}
