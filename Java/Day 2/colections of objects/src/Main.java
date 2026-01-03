import java.util.*;

abstract class Valoare{
    abstract public List<Valoare> contine(long valoare);
}

class ValoareNumerica extends Valoare{
    private long val;

    public ValoareNumerica(long val){
        this.val = val;
    }

    public long getVal(){
        return this.val;
    }

    public boolean equals(Object o){
        if(o instanceof ValoareNumerica){
            ValoareNumerica obj = (ValoareNumerica)o;
            return obj.getVal() == this.val;
        }
        return false;
    }

    public int hashCode() {
        return Objects.hash(val);
    }

    public String toString(){
        String rez = "";
        rez += this.val;

        return rez;
    }

    public List<Valoare> contine(long val){
        List<Valoare> lista = new LinkedList<>();
        ValoareNumerica tmp = new ValoareNumerica(val);

        if(tmp.equals(this))
            lista.add(this);

        return lista;
    }
}

class PerecheDeValori extends Valoare{
    private Valoare val1;
    private Valoare val2;

    public PerecheDeValori(Valoare val1, Valoare val2){
        this.val1 = val1;
        this.val2 = val2;
    }

    public Valoare getVal1(){
        return this.val1;
    }

    public Valoare getVal2(){
        return this.val2;
    }

    public boolean equals(Object o){
        if(o instanceof PerecheDeValori){
            PerecheDeValori obj = (PerecheDeValori)o;
            return (obj.getVal1()).equals(this.val1) && (obj.getVal2()).equals(this.val2);
        }
        return false;
    }

    public int hashCode() {
        return Objects.hash(val1, val2);
    }

    public String toString(){
        String rez = "(";
        rez += (this.val1).toString() + ", " + (this.val2).toString() + ")";

        return rez;
    }

    public List<Valoare> contine(long valoare){
        List<Valoare> lista = new ArrayList<>();

        List<Valoare> listaVal1 = val1.contine(valoare);
        for(Valoare val : listaVal1){
            lista.add(val);
        }

        List<Valoare> listaVal2 = val2.contine(valoare);
        for(Valoare val : listaVal2){
            lista.add(val);
        }

        return lista;
    }
}

class Grup extends Valoare{
    private Set<Valoare> grup = new HashSet<>();

    public void adauga(Valoare... valori){
        for(Valoare val : valori){
            grup.add(val);
        }
    }

    public boolean equals(Object o){
        if(o instanceof Grup){
            Grup obj = (Grup)o;
            return Objects.equals(this.grup, obj.grup);
        }
        return false;
    }

    public int hashCode() {
        return Objects.hash(grup);
    }

    public String toString(){
        String rez = "[";
        for(Valoare val : this.grup){
            rez += val.toString() + ",";
        }

        if (!grup.isEmpty()) {
            rez = rez.substring(0, rez.length() - 1);
        }

        rez += "]";

        return rez;
    }

    public List<Valoare> contine(long valoare){
        List<Valoare> lista = new ArrayList<>();

        Iterator<Valoare> iterator = (this.grup).iterator();
        while(iterator.hasNext()){
            Valoare val = iterator.next();
            lista.addAll(val.contine(valoare));
        }

        return lista;
    }
}

public class Main {
    public static void main(String[] args) {
        // 1. Construim structura pas cu pas: [(1, 2), (3, [3])]

        // Cream valorile numerice de baza
        ValoareNumerica v1 = new ValoareNumerica(1);
        ValoareNumerica v2 = new ValoareNumerica(2);
        ValoareNumerica v3 = new ValoareNumerica(3);

        // Perechea (1, 2)
        PerecheDeValori p1 = new PerecheDeValori(v1, v2);

        // Grupul interior [3]
        Grup grupInterior = new Grup();
        grupInterior.adauga(v3);

        // Perechea (3, [3])
        PerecheDeValori p2 = new PerecheDeValori(v3, grupInterior);

        // Grupul principal [(1, 2), (3, [3])]
        Grup grupPrincipal = new Grup();
        grupPrincipal.adauga(p1, p2);

        // 2. Tiparim grupul la iesirea standard
        System.out.println("Grup initial: " + grupPrincipal);

        // 3. Incercam adaugarea unei perechi (1, 2) diferite ca obiect, dar egale ca valoare
        // Cream obiecte noi de tip ValoareNumerica pentru a forta o alta adresa de memorie
        ValoareNumerica v1_nou = new ValoareNumerica(1);
        ValoareNumerica v2_nou = new ValoareNumerica(2);
        PerecheDeValori p1_duplicat = new PerecheDeValori(v1_nou, v2_nou);

        grupPrincipal.adauga(p1_duplicat);

        // 4. Retiparim grupul (ar trebui sa arate la fel daca equals/hashCode merg bine)
        System.out.println("Grup dupa incercare adaugare duplicat: " + grupPrincipal);
        System.out.println("------------------------------------------------------");

        // 5. Apelam contine(3) si salvam rezultatul intr-o lista
        List<Valoare> rezultate = grupPrincipal.contine(3);

        // 6. Tiparim rezultatele conform cerintei (pe linii diferite)
        // Folosim obligatoriu for normal cu get() si size()
        System.out.println("Rezultatele cautarii valorii 3:");
        for (int i = 0; i < rezultate.size(); i++) {
            Valoare v = rezultate.get(i);

            // Afisam obiectul, hashCode-ul calculat si cel de identitate (adresa)
            System.out.print("Obiect: " + v.toString());
            System.out.print(" | hashCode: " + v.hashCode());
            System.out.println(" | identityHashCode: " + System.identityHashCode(v));
        }
    }
}