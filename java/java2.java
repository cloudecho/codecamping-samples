import java.util.stream.IntStream;

class Test {
    public static void main(String[] args) {
        // System.out.print("hello");
        int sum = IntStream.rangeClosed(
                1,
                100).sum();
        System.out.println("1+2+...+100 = " + sum);
    }
}