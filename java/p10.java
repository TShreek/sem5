import java.sql.*;

public class p10 {
    public static void main(String[] args) {
        try {
            // Establishing a connection
            Connection connection = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/your_database", // Add your database name
                "root",
                "password"
            );

            // Creating a statement
            Statement statement = connection.createStatement();

            // INSERT query (corrected syntax)
            String insertQuery = "INSERT INTO STUDENT (id, name, age, department) VALUES (1, 'John', 21, 'Computer Science')";
            statement.executeUpdate(insertQuery); // Use executeUpdate for INSERT
            System.out.println("Record inserted successfully.");

            // SELECT query
            String readQuery = "SELECT * FROM STUDENT";
            ResultSet resultSet = statement.executeQuery(readQuery); // Use executeQuery for SELECT
            while (resultSet.next()) {
                System.out.println(
                    resultSet.getInt("id") + " - id, " +
                    resultSet.getString("name") + " - name, " +
                    resultSet.getInt("age") + " - age, " +
                    resultSet.getString("department") + " - department"
                );
            }

            // UPDATE query
            String updateQuery = "UPDATE STUDENT SET age = 20 WHERE name = 'John'";
            statement.executeUpdate(updateQuery); // Use executeUpdate for UPDATE
            System.out.println("Record updated successfully.");

            // DELETE query
            String deleteQuery = "DELETE FROM STUDENT WHERE name = 'John'";
            statement.executeUpdate(deleteQuery); // Use executeUpdate for DELETE
            System.out.println("Record deleted successfully.");

            // Close the connection
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace(); // Handle SQL exceptions
        }
    }
}
