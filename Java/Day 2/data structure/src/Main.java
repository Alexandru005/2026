import java.util.*;

public class Main{
    public static void main(String[] args){
        System.out.println("Array");
        //Array
        int[] vector = new int[10];

        for (int i = 0; i < vector.length; i++){
            vector[i] = i + 1;
            System.out.print(vector[i] + " ");
        }

        System.out.println("\n\n2D Array");

        //2D Array
        int[][] matrice = new int[2][2];

        int valoare = 1;

        for(int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                matrice[i][j] = valoare;
                valoare++;
                System.out.print(matrice[i][j] + " ");
            }
        System.out.println();
        }

        System.out.println("\nList");

        //declarare
        List<String> listaCulori = new ArrayList<>();

        //Adaugare in lista
        listaCulori.add("albastru");
        listaCulori.add("rosu");

        //alte functii
        System.out.println(listaCulori);
        System.out.println(listaCulori.size()); // arata cate elemente are
        System.out.println(listaCulori.contains("albastru")); // verifica daca exista elementul
        System.out.println(listaCulori.contains("roz"));

        //parcurgere
        for(String color : listaCulori){
            System.out.println(color);
        }

        System.out.println("\nStack / Queue");

        //declarare stiva
        Stack<Integer> stack = new Stack<>();

        //adaugare elemente
        stack.push(12);
        stack.push(13);
        stack.push(14);
        stack.push(15);

        System.out.println(stack.size());
        System.out.println(stack.peek());
        System.out.println(stack.pop());
        System.out.println(stack.peek());
        System.out.println(stack.empty());

        //declarare coada
        Queue<Integer> coada = new LinkedList<>();
        coada.add(12);
        coada.add(3);


        System.out.println(coada);
        coada.poll();
        System.out.println(coada);

        System.out.println("\nLinked List");

        List<Integer> linkedList = new LinkedList<>();

        linkedList.add(12);
        linkedList.add(10);

        System.out.println(linkedList);
        linkedList.addFirst(1);
        System.out.println(linkedList);
        linkedList.add(2,4);
        System.out.println(linkedList);

        System.out.println("\nSet");

        Set<Integer> multime = new HashSet<>();

        multime.add(12);
        multime.add(1);
        multime.add(3);

        //parcurgere
        Iterator<Integer> iterator = multime.iterator();
        while(iterator.hasNext()){
            System.out.print(iterator.next() + " ");
        }

        System.out.println("\n\nMap");

        Map<String, Integer> persoane = new HashMap<>();
        persoane.put("Alex", 20);
        persoane.put("Andrei", 21);

        System.out.println(persoane);
        System.out.println(persoane.get("Alex"));
        System.out.println(persoane.keySet());
        System.out.println(persoane.entrySet());

        System.out.println("\nHash");

        Map<String, Integer> persoana = new HashMap<>();
        persoana.put("Alex", 23);




    }
}