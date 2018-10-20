/**
 * Iden Craven
 * CPSC 331
 */

public class SLLBubbleSort {
    public static <T extends Comparable<? super T>> void BubbleSort(SLL<T> list) {
        if (list.getLength() > 1) {
            for (int i = 0; i < list.getLength(); i++) {
                SLLNode<T> curr = list.head;
                SLLNode<T> next = list.head.next;
                while (next != null) {
                    if (curr.info.compareTo(next.info) > 0) {
                        T temp = curr.info;
                        curr.info = next.info;
                        next.info = temp;
                    }
                    curr = next;
                    next = next.next;
                }
            }
        }
    }
}
