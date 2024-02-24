0x09. Web infrastructure design

The project Tasks to be fulfilled

0-simple_web_stack contains the URL of an image includes the design of a one server web infrastructure that hosts the website that is reachable via www.foobar.com. You can start your explanation by having a user wanting to access your website.

Elements that can be used in the design:

1 server.

1 web server (Nginx).

1 application server.

1 application files (your code base).

1 database (MySQL).

1 domain name foobar.com configured with a www record that points to the server IP 8.8.8.8.


1-distributed_web_infrastructure includes the URL of an image consists the design of a three server web infrastructure that hosts the website www.foobar.com.

Elements that can be added to the previous design:

2 servers.

1 web server (Nginx).

1 application server.

1 load-balancer (HAproxy).

1 set of application files (your code base).

1 database (MySQL).

2-secured_and_monitored_web_infrastructure includes the URL of an image consists the design of a three server web infrastructure that hosts the website www.foobar.com. It must be secured, serve encrypted traffic, and be monitored.

Elements that can be added to the previous design:

3 firewalls.

1 SSL certificate to serve www.foobar.com over HTTPS.

3 monitoring clients (data collector for Sumologic or other monitoring services).

3-scale_up Includes the URL of an image consists the design of a scaled up web infrastructure that hosts the website www.foobar.com.

Elements that can be added to the previous design:
1 server.

1 load-balancer (HAproxy) configured as cluster with the other one.

Split components (web server, application server, database) with their own server.
