import java.util.*;

class strcmps{
    public int strcmp1(String s1, String s2){
        int x1 = s1.length();
        int x2 = s2.length();
        if(x1>x2){
            return 1;
        }
        else if(x2>x1){
            return -1;
        }
        else{
            int ret=0;
            for(int i=0;i<x1;i++){
                char c1 = s1.charAt(i);
                char c2 = s2.charAt(i);
                ret = c1-c2;
            }
            return ret;
        }
    }

    public int strcmp2(String s1,String s2, int n){
        int x1 = s1.length();
        int x2 = s2.length();
        if(x1>x2){
            return 1;
        }
        else if(x2>x1){
            return -1;
        }
        else{
            int ret=0;
            if(n > x1){
                return -1;
            }
            else{
                for(int i=0;i<n;i++){
                    char c1 = s1.charAt(i);
                    char c2 = s2.charAt(i);
                    ret = c1-c2;
                }
                return ret;
            }
        }
    }
}

public class p5{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two strings");
        String s1 = sc.next();
        String s2 = sc.next();
        strcmps s = new strcmps();
        int res = s.strcmp1(s1,s2);
        if(res>0){
            System.out.println("String 1 is greater than String 2");
        }
        else if(res<0){
            System.out.println("String 1 is less than String 2");
        }
        else{
            System.out.println("String 1 is equal to String 2");
        }

        System.out.println("Enter the value of n");
        int n = sc.nextInt();
        res = s.strcmp2(s1,s2,n);
        if(res>0){
            System.out.println("First N chars of String 1 is greater than String 2");
        }
        else if(res<0){
            System.out.println("First N chars of String 1 is less than String 2");
        }
        else{
            System.out.println("First N chars of String 1 is equal to String 2");
        }
    }
}
