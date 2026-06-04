

import java.util.Scanner;

abstract class ruang2D{
    abstract double hitungLuas();
    abstract double hitungKeliling();
}

class segiempat extends ruang2D {
    double panjang;
    double lebar;

    segiempat(double p, double l){
        panjang = p;
        lebar = l;
    }

    @Override
    double hitungLuas() {
        return panjang * lebar;
    }

    @Override
    double hitungKeliling() {
        return 2 * (panjang + lebar);
    }
}

class segitiga extends ruang2D {
    double alas;
    double tinggi;

    segitiga(double a, double t){
        alas = a;
        tinggi = t;
    }

    @Override
    double hitungLuas() {
        return 0.5 * alas * tinggi;
    }

    @Override
    double hitungKeliling() {
        return alas + tinggi + Math.sqrt(alas*alas + tinggi*tinggi);
    }
}

public class LKP_06A{
        public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double luassegiempat = 0;
        double luassegitiga = 0;

        double kelilingsegiempat = 0;
        double kelilingsegitiga = 0;

        while (true) {
            String tipe = input.next();
            if (tipe.equals("x")){
                break;
            }

            double p = input.nextDouble();
            double l = input.nextDouble();

            if (tipe.equals("r")){
                segiempat s = new segiempat(p, l);

                luassegiempat += s.hitungLuas();
                kelilingsegiempat += s.hitungKeliling();
            }

            else if (tipe.equals("t")){
                segitiga s = new segitiga(p, l);

                luassegitiga += s.hitungLuas();
                kelilingsegitiga += s.hitungKeliling();
            }        
            
        }

        System.out.println("luas");
        System.out.println("segiempat: " + luassegiempat);
        System.out.println("segitiga: " + luassegitiga);
        System.out.println("keliling");
        System.out.println("segiempat: " + kelilingsegiempat);
        System.out.println("segitiga: " + kelilingsegitiga);
    }
}