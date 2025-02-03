<%@ page language="java" import = "java.util.*"%>
<%
String name = (String) session.getParameter("name");
Long startTime = (long) session.getParameter("time");

long duration = (new date().getTime - startTime) / 1000;
%>

<html>
  <head><title></title></head>
  <body>
  <p> thank you for logging in <%= name %> !, you were logged in for <%= duration %> seconds > </p>
  </body>
  </html>
