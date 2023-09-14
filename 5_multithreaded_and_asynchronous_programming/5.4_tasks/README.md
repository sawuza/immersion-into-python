# 5.4 Tasks

### Client for sending metrics
>In large projects, with a large number of users, it is necessary to carefully observe all the processes occurring in it. Information about processes can be represented by various numerical indicators, for example: the number of requests to your application, the response time of your service to each request, the number of users per day, and others. We will call these different numerical indicators as metrics.
> 
> There are ready-made solutions for collecting, storing and displaying such metrics, for example Graphite, InfluxDB. In this course, we will develop our own system for collecting and storing metrics based on client-server architecture.
>
> This week we will start by developing a client to send and receive metrics. Next week, as a final assignment, you will be asked to implement a server to store the metrics.
