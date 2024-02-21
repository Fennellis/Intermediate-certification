import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * Program
 */
public class Program {
    static PriorityQueue<Product> queue = new PriorityQueue<Product>();
    public static void main(String[] args){
        put("1 2 конструктор");
        put("2 2 робот");
        put("3 6 кукла");

        try(FileWriter writer = new FileWriter("log.txt", false))
        {
            for (int i = 0; i < 10; i++) {
                int result = get();
                if (result > 0){
                    writer.write(Integer.toString(result) + "\n");
                }
                else throw new RuntimeException();
            }
             
            writer.flush();
        }
        catch(IOException | RuntimeException ex){
             
            System.out.println(ex.getMessage());
        }

    }
    
    private static void put(String str){
        String[] temp = str.split(" ");
        if (temp.length != 3)
            return;
        try {
            int id = Integer.parseInt(temp[0]);
            int dropChance = Integer.parseInt(temp[1]);
            String name = temp[2];

            if (id <= 0 || dropChance <= 0)
                return;

            Product product = new Product(id, name, dropChance);
            if (!queue.contains(product))
                queue.add(product);
        } catch (Exception e) {
            System.out.println(e.toString());
            return;
        }
    }

    private static int get(){
        HashMap<Integer, Integer> map = new HashMap<>();
        int start = 0;
        int end = 0;
        for (Product product : queue) {
            end = start + product.getDropChance();
            map.put(product.getID(), end);
            start = end;
        }
        int random = (int)(Math.random() * (end + 1 - 0));
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (random <= entry.getValue())
                return entry.getKey();
        }
        return -1;
    }
}