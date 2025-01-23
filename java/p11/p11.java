import java.util.*;
import java.io.*;
import jakarta.servlet.x;
import jakarta.servlet.http.*;
public class ValidateAgeServlet extends HttpServlet{
    protected void doPost(HttpServletRequest request, HttpServletResponse response throws ServletException, IDException){
        String name = request.getParameter("name");
        int age = Integer.parseInt(request.getParameter("age"));

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        (age > 18)? out.println("<h1>Welcome " + name + "</h1>") : out.println("<h1>Sorry " + name + ", you are not eligible to vote.</h1>");
        out.println("</body></html>");
        out.close();
    }

}
