import java.util.*;

public class nested_arrayList {
    public static void main(String args[]){

        List<ArrayList<Integer>> a = new ArrayList<>();

        ArrayList<Integer> al1 = new ArrayList<Integer>();
      //  ArrayList<Integer> al2 = new ArrayList<Integer>();
      //  ArrayList<Integer> al3 = new ArrayList<Integer>();

        al1.add(1);
        al1.add(2);
        al1.add(3);

       // al2.add(4);
       // al2.add(5);
       // al2.add(6);

       // al3.add(7);
       // al3.add(8);
       // al3.add(9);

        a.add(al1);
      //  a.add(al2);
      //  a.add(al3);

        for(ArrayList obj: a){
            ArrayList<Integer> temp = obj;
            for(Integer num : temp){
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }


}
