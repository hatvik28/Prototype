public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5};
        System.out.println(numbers[6]); // Accessing invalid index

        Object obj = null;
        System.out.println(obj.length()); // Possible NullPointerException

        while (true) { // Infinite loop
            // No increment for loop variable
        }

        printNumber(); // Method does not exist

        int unusedVar = 42; // Unused variable
        
        public int getValue() {
            // Missing return statement
        }
    }
}