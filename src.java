import java.io.*;
import java.util.*;


public class src {
    public static void main(String[] args){
        String path = "/Users/SAM/Desktop/SSIS/student.csv";
        String line = "";
        

        try{
            BufferedReader br = new BufferedReader(new FileReader(path));
            while((line = br.readLine()) != null){
                System.out.println(line);
            }
            br.close();

            Scanner newinpt = new Scanner(System.in);
            System.out.println("Enter new data to append:");
            String x = newinpt.nextLine();

            BufferedWriter inptdata = new BufferedWriter(new FileWriter(path, true));
            inptdata.newLine();
            inptdata.write(x);
            inptdata.close();

        } catch (FileNotFoundException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
