import java.util.Scanner;

public class Main{
    public static void main(String args[]){
        int num= (int) (Math.random()*100);
        Scanner sc=new Scanner(System.in);
        int guess_num=0;
        do{
            System.out.println("User Enter the guessing number ");
            guess_num=sc.nextInt();
            System.out.println("User number is here "+" "+ guess_num);
            if (guess_num==num){
                System.out.println("Your Number is equal to Random Number"+" "+guess_num);
                System.out.println("Random number is "+" "+num);
                break;
            }
            else if(guess_num>num) {
                System.out.println("number is greater" + " " + guess_num);
                System.out.println("Random number is "+" "+num);
            }
            else{
                System.out.println("your number is too small"+" "+guess_num);
                System.out.println("Random number is "+" "+num);
            }
            System.out.println("Want to leave then press any - number");
        }while(guess_num>0);
        System.out.println("The END");
    }
}
