interface Actiuni{
    public String canta();
}

class Muzician implements Actiuni{
    private String nume;
    private Integer experienta;

    public Muzician(String nume, Integer experienta){
        this.nume = nume;
        this.experienta = experienta;
    }

    public String toString(){
        String rez = "";
        rez += "Ma numesc " + this.nume + " si cant de " + this.experienta + " ani.";

        return rez;
    }
    
    public String canta(){
        return "";
    }
    
    public String getNume(){
        return this.nume;
    }

    public Integer getExperienta(){
        return this.experienta;
    }

    public boolean exista(Muzician[] muzicieni){
        for(int i = 0; i < muzicieni.length; i++){
            if(this.equals(muzicieni[i]))
                return true;
        }

        return false;
    }
}

class Chitarist extends Muzician{
    private String tipChitara;
    
    public Chitarist(String tipChitara, String nume, Integer experienta){
        super(nume, experienta);
        this.tipChitara = tipChitara;
    }

    public String canta(){
        return super.getNume() + " canta la " + this.tipChitara;
    }
    
    public String toString(){
        return super.toString() + "Instrumentul la care cant e " + this.tipChitara + ".";
    }

    public String getInstrument(){
        return this.tipChitara;
    }

    public boolean equals(Object o){
        if(o instanceof Chitarist){
            Chitarist obj = (Chitarist)o;
            return (obj.getNume()).equals(super.getNume())
                    && obj.getExperienta() == super.getExperienta()
                    && (obj.getInstrument()).equals(this.tipChitara);
        }
        return false;
    }
}

class Violonist extends Muzician{
    private String tipVioara;

    public Violonist(String tipViolonist, String nume, Integer experienta){
        super(nume, experienta);
        this.tipVioara = tipViolonist;
    }

    public String canta(){
        return super.getNume() + " canta la " + this.tipVioara;
    }

    public String toString(){
        return super.toString() + "Instrumentul la care cant e " + this.tipVioara + ".";
    }

    public String getInstrument(){
        return this.tipVioara;
    }

    public boolean equals(Object o){
        if(o instanceof Violonist){
            Violonist obj = (Violonist)o;
            return (obj.getNume()).equals(super.getNume())
                    && obj.getExperienta() == super.getExperienta()
                    && (obj.getInstrument()).equals(this.tipVioara);
        }
        return false;
    }
}

public class Main{



    public static void main(String[] args){
        Muzician[] formatie = new Muzician[2];
        formatie[0] = new Chitarist("chitara electrica", "Alex", 12);
        formatie[1] = new Violonist("vioara mica", "Daniel", 5);

        System.out.println(formatie[0].toString());
        System.out.println(formatie[1].toString());

        System.out.println(formatie[0].canta());
        System.out.println(formatie[1].canta());

        Muzician cantaret1 =  new Chitarist("chitara electrica", "Alex", 12);
        System.out.println(cantaret1.exista(formatie));

        Muzician cantaret2 =  new Violonist("vioara mica", "Daniel", 5);
        System.out.println(cantaret2.exista(formatie));


        Muzician cantaret3 =  new Chitarist("chitara electrica", "Alexandru", 12);
        System.out.println(cantaret3.exista(formatie));

        Muzician cantaret4 =  new Violonist("vioara mica", "Daniela", 5);
        System.out.println(cantaret4.exista(formatie));


    }
}