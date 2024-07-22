/* 0x11. What happens when you type google.com in your browser and press Enter */

What happens when you type https://www.google.com in your browser and press Enter.
Behind the Scenes: From URL to Google Homepage - A Software Engineer's Journey
Have you ever wondered what happens in the blink of an eye when you type a URL like "https://www.google.com" and press Enter? As a software engineer, I can tell you it's a fascinating journey that involves several layers of technology working together seamlessly. Today, let's delve into the magic behind this everyday action.
1. DNS Request
When you enter "https://www.google.com", your browser sends a request to a Domain Name System (DNS) server to resolve the domain name to an IP address. The DNS server acts as a phonebook, mapping domain names to IP addresses. In this case, the DNS server returns the IP address associated with Google's server.
DNS Cache Check: The browser first checks its cache to see if it has a recent DNS record for www.google.com. If not, it proceeds to query the local DNS resolver, usually provided by your ISP.
DNS Query: If the local resolver doesn’t have the answer, it queries the root DNS servers, which direct the query to the .com top-level domain (TLD) servers. These TLD servers then point to Google's authoritative DNS servers.
Response: Google’s DNS servers respond with the IP address of the Google server closest to your location, optimizing for speed and load distribution.
2. TCP/IP Connection
Your browser establishes a connection with Google's server using the Transmission Control Protocol/Internet Protocol (TCP/IP). TCP ensures reliable data transfer, while IP routes the data packets between networks. Your browser and Google's server exchange a series of packets to establish a connection
TCP Handshake: The browser initiates a TCP connection with the server using a three-step handshake process:
SYN: The browser sends a SYN (synchronize) packet to the server.
SYN-ACK: The server responds with a SYN-ACK (synchronize-acknowledge) packet.
ACK: The browser sends an ACK (acknowledge) packet back to the server.
IP Protocol: This handshake is part of the TCP/IP protocol suite, which ensures reliable communication over the internet.
3. Firewall
Before your request reaches Google's server, it might encounter a firewall. This security system acts as a gatekeeper, filtering incoming and outgoing traffic based on predefined rules. If your request is deemed safe, the firewall allows it to pass through.
Client-Side Firewall: Your device's firewall checks outgoing packets to ensure they are allowed.
Network Firewalls: ISPs and intermediate networks may have firewalls that inspect packets to enforce security policies.
Server-Side Firewall: Google's firewalls protect their servers from unauthorized access and malicious traffic.
4. HTTPS/SSL
The "https" in the URL indicates a secure connection. Here, HTTPS (Hypertext Transfer Protocol Secure) comes into play. It uses SSL (Secure Sockets Layer) to encrypt the communication between your browser and Google's server. This encryption scrambles the data, making it unreadable to anyone eavesdropping on the conversation.
SSL/TLS Handshake:
The browser sends a "ClientHello" message, which includes supported SSL/TLS versions and cipher suites.
The server responds with a "ServerHello" message, selecting the SSL/TLS version and cipher suite.
The server sends its SSL certificate to the browser to authenticate its identity.
The browser verifies the certificate against a trusted Certificate Authority (CA) list.
Both parties generate session keys for encrypting the communication.
5. Load Balancer
Imagine millions of users trying to access Google at once! To handle this traffic efficiently. The request is routed to a load balancer, a server that distributes incoming traffic across multiple servers to ensure efficient use of resources and minimize downtime. The load-balancer may use various algorithms to determine which server should handle a given request, such as round-robin or least connections. The load balancer directs the request to one of Google's available servers.
Load Distribution: The load balancer forwards your request to one of the available web servers based on the current load and server health.
Session Persistence: In some cases, the load balancer ensures that a user's requests are consistently routed to the same server for the duration of their session.
6. Web Server
The request reaches a web server, such as Apache or Nginx, which hosts Google's website. The request finally reaches one of Google's web servers. This server houses the core functionality of the website. It understands your request (to display the homepage) and retrieves the necessary files like HTML, CSS, and JavaScript.
Request Handling: The web server (e.g., Apache, Nginx) processes the request. It checks for cached content to serve the response quickly. If the requested resource is dynamic or not cached, it forwards the request to an application server.


7. Application Server
In some cases, the web server might hand off the request to an application server. This server handles complex tasks like personalizing search results based on your past searches (if you're logged in) or performing database queries.
Business Logic: The application server runs the backend logic, querying databases, processing data, and executing application-specific code.
Frameworks: This could involve frameworks like Node.js, Django, Ruby on Rails, or custom backend systems used by Google.
8. Database
The application server may interact with a database, such as MySQL or MongoDB, to retrieve or store data. Speaking of databases, some of the content you see on Google might be stored in a database. This is a structured storage system that holds information like website content, user profiles, and search history. If needed, the application server might interact with the database to retrieve relevant data for your request.
Query Execution: The application server sends a query to the database server (e.g., MySQL, PostgreSQL, Google’s Spanner).
Data Retrieval: The database processes the query, retrieves the necessary data, and sends it back to the application server.
Caching: To improve performance, frequently accessed data may be stored in a cache (e.g., Redis, Memcached).
9. Response Assembly and Return
Once the web server (and potentially the application server) gathers all the necessary pieces, often in HTML, JSON, or XML format, it sends them back to your browser. Your browser then interprets the code, renders the images and text, and voila! The familiar Google homepage appears on your screen.
Response Construction: It combines data from various sources, processes it, and constructs the response.
Return Path: The response travels back through the web server, load balancer, and eventually over the internet to your browser.
10. Rendering the Page
Upon receiving the response, your browser then interprets the code, renders the images and text, and voila! The familiar Google homepage appears on your screen.
HTML Parsing: The browser parses the HTML, building the Document Object Model (DOM).
Resource Loading: It requests additional resources like CSS, JavaScript, images, etc., often repeating the DNS, TCP, and HTTPS steps for each resource.
JavaScript Execution: JavaScript is executed, enhancing interactivity and dynamic content.
Conclusion
This entire process, from typing https://www.google.com to seeing the web page, involves numerous steps and technologies working together harmoniously. It showcases the complexity and efficiency of the web stack, ensuring fast, secure, and reliable delivery of content to users around the globe.
I hope this post has provided you with a deeper understanding of the magic that happens when you type (link unavailable) and press Enter. Happy coding!

