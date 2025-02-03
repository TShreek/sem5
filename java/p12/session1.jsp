<%@ page language = "java" import "java.util.*" %>
<%
String name = request.getParameter("name");

session.setAttribute("name",name);
session.setAttribute("time",new Date().getTime());

String serverPort = request.getServerPort();
%>

<html>
  <head><title> JSP PROGRAM </title></head>
  <body>
  <p align = "right"> start time = <%= new Date() %></p>
<h2> Hello <%= name %> Welcome to site </h2>
<form action = "http://localhost:<%= serverPort %>/JspSessions/jspsession2" method = "get">
  <input type="submit" value="logout">
  </form>
  </body>
  </html>
