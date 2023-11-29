import java.util.Scanner;
public class pattern
{
    public static void main(String[] args)
    {
        int i,j,n;
        Scanner ref=new Scanner(System.in);
        System.out.println("Enter limit");
        n=ref.nextInt();
        for(i=0;i<n;i++)
        {
            for(j=1;j<n;j++)
            {
                System.out.println("*");
            }
            
        }
        System.out.println();
    }
}