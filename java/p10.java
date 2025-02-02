import java.sql.*;

public class p10{
    public static void main(String[] args) {
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/demodb","root","");
            Statement statement = conn.createStatement();

            //INSERT
            String iQ1 = "INSERT INTO STUDENT (id,name,dept,age) VALUES (1,'aa','mech',21)";
            String iQ2 = "INSERT INTO STUDENT (id,name,dept,age) VALUES (2,'bb','civil',24)";
            statement.executeUpdate(iQ1);
            statement.executeUpdate(iQ2);

            //READ : 
            String rQ1 = "SELECT * FROM STUDENT WHERE name = 'aa'";
            ResultSet resultSet = statement.executeQuery(rQ1);
            while(resultSet.next()){
                System.out.println("Name :" + resultSet.getString("name") + "ID : " + resultSet.getInt("id") + "DEPT : " + resultSet.getString("dept"));
            }

            //UPDATE 
            String uQ1 = "UPDATE STUDENTS SET age = 60 WHERE name = 'bb'";
            statement.executeUpdate(uQ1);

            //DELETE : 
            String dQ1 = "DELETE FROM STUDENTS WHERE id = 1";
            statement.executeUpdate(dQ1);
            conn.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
