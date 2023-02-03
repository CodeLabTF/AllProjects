
import java.util.Scanner;
public class osa2_ül4_display_certain_numbers_array {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);  //Scanner object
        Scanner st = new Scanner(System.in);  //Scanner object

        int f = 0;
        int[] NRS  = new int[30];

        int e = 0;

/*
        for(int i = 0; i < e ; i++){                  // do this 10 times
            System.out.printf("enter a value>>"); // print a statement to the screen
            xfilesArray[i] = st.nextInt();          // read an integer from the user and store it into the array
        }
*/
        System.out.println("Sisestage positiivne number!");
        int AB = sc.nextInt();



        // NRS array'sse arvude lisamine
        for(int i = 0 ; i < AB ; i++){
            NRS[i] = i + 1;

        }

        //NRS array'sse


 /*
        int[] NRS = new int[100];
        for (int i = 0; i < a; i++) {
            NRS[i] = i + 1;

            System.out.println(NRS[i]);
*/
            System.out.println("Jagatav 3'ga:");
            for( int i=0;i<AB;i++){
                if(NRS[i]%3==0){
                    System.out.println(NRS[i]);
                }
            }

            System.out.println("Jagatav 7'ga:");
            for(int i=0;i<AB;i++){
                if(NRS[i]%7==0){
                    System.out.println(NRS[i]);
                }
            }


        }


    }















//        int x;


      /*  for(x=1; x<=a; x++) {
        if (a%3==0) {
            System.out.println("Fizz");
        }
        if (){


        }*/