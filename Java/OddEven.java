public class OddEven {
    public static void main(String args[]){

        int a[]={1,2,5,6,3,2,7,10,14};

        System.out.println("Jagatav 3'ga:");



        for(int i=0;i<a.length;i++){
            if(a[i]%3==0){
                System.out.println(a[i]);
            }
        }

        System.out.println("Jagatav 7'ga:");
        for(int i=0;i<a.length;i++){
            if(a[i]%7==0){
                System.out.println(a[i]);
            }
        }
    }
}
