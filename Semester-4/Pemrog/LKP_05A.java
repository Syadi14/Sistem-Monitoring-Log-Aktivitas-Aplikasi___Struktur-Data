//Input
// 5
// 70.3
// 85.5
// 93.1
// 66.5
// 78.8

//Output
// 66.50 93.10 = min max
// 78.84 9.35 = avg stdev

import java.util.*;

public class LKP_05A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        double[] data = new double[N];
        
        double terkecil = Double.MAX_VALUE;
        double terbesar = Double.MIN_VALUE;
        double jumlah = 0.0;
        
        for (int i = 0; i < N; i++) {
            data[i] = sc.nextDouble();
            jumlah += data[i];
            
            if (data[i] < terkecil) {
                terkecil = data[i];
            }
            
            if (data[i] > terbesar) {
                terbesar = data[i];
            }
        }
        
        double rataRata = jumlah / N;

        double totalSelisih = 0.0;
        for (int i = 0; i < N; i++) {
            double selisih = data[i] - rataRata;
            totalSelisih += selisih * selisih;
        }
        
        double standarDeviasi;
        if (N == 1) {
            standarDeviasi = 0.0;
        } else {
            standarDeviasi = Math.sqrt(totalSelisih / (N - 1));
        }
        
        System.out.printf("%.2f %.2f\n", terkecil, terbesar);
        System.out.printf("%.2f %.2f", rataRata, standarDeviasi);
        
        sc.close();
    }
}