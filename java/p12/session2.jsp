<%@ page language="java" import = "java.util.*"%>
<%
String name = (String) session.getAttribute("name");
Long startTime = (Long) session.getAttribute("time");

long duration = (new Date().getTime - startTime) / 1000;
%>

<html>
  <head><title></title></head>
  <body>
  <p> thank you for logging in <%= name %> !, you were logged in for <%= duration %> seconds </p>
  </body>
  </html>
