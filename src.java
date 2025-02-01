import java.io.*;
import java.util.*;

public class src {
    public static void main(String[] args){
        String path = "/Users/SAM/Desktop/SSIS/student.csv";
        String line = "";

        try{
        BufferedReader br = new BufferedReader(new FileReader(path));
        while((line = br.readLine()) != null){
            String values[] = line.split(",");
            System.out.println(values[1]);
        }


        } catch (FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
