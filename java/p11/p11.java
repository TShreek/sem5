import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

@WebServlet("/CheckAge")
public class CheckAge extends HttpServlet{
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException,IOException{
        String name = request.getParameter("name");
        int age = request.parseInt(request.getParameter("age"));
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        out.println("<html><body>");
        if(age <18){
            out.println("<p>SORRY " + name + " YOU ARE NOT AUTHORIZED TO VIEW THIS PAGE<p>");
        }
        else{
            out.println("<p>Welcome to the website "+ name + "!!<p>");
        }
        out.println("</body></html>");
        out.close();
    }
}
