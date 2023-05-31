# **AWS(Amazon Web Services)**

It is a secure cloud services platform that offeers variety of service includes storage,computing,and networking.

## Different services in aws

1. **EC2(Elastic Computer Cloud)**

   It stands for Elastic Computer Cloud. It is a service that provide secure, resizable compute capacity in the cloud .It allows you to create a virtual computer on the cloud. you can choose OS,RAM,MEMORY and then can rent

   It enables you to increase or decreasae capacity within minutes, not hours or days

   Example: we can use ec2 instance as server for web applications.

   **key points:**

   - Virtual Computing
   - Scalability(can add more isntances)
   - Flexibility and Customization
   - Pay-As-You-Go Pricing
   - Elasticity(dynamically adjust capacity of instances-increase/decrease)
   - Intergraion with other servieces(rds,s3)
   - Rapid Provisioning(provision new isntances within minutes, quickly deploy and scale applications)

2. **S3(Simple Storage Service)**

   S3 is like a secure storage room that keeps all your files safe and organized.

   **key points:**

   - Secure Storage
   - Scalability(store virtually inlimited amounts of data).
   - Orgainzational Structure(s3 organize data into buckets which are like folders or containers for your files)
   - Durability and Redundancy(stores multiple copies of data across different data centers within a region)

for external storage we can use s3 for example in social media application users are storing their or videos

3. **ELB(Elastic Load Balancer)**

   It helps distributing multiple network requests to different targets such as EC2 instances.
   The main purpose of ELB is to evenly distribute the incoming traffic across multiple resources, enabling efficient utilization of computing resources and improving the overall performance, availability, and fault tolerance of the application

   **key points:**

   - Even Distribution of Traffic
   - High Availability(routing traffic only to healthy instances)
   - Scalability(enables to handle increased traffic and scale horizontally based on demand)
   - Fault Tolerance(automatically distrubuting traffic accross multiple resources.if one fails it automatically transfer traffic to healthy resources)

4. **IAM(Identity And Access Management)**
   It helps you control who can access your AWS **resources** and what **actions** they can perform. It allows you to create and manage different identities, such as users, groups, and roles, and assign specific permissions to them
   It helps in keeping your AWS account secure and managing access to your resources effectively.

   **key points:**

   - Acess Control
   - User Management
   - Role-Based Access
   - Multi-Factor Authentication
   - Integration with different AWS Services(EC2,S3,RDS)

5. **RDS(Relational Database Service)**
   It's a service that makes it easier to set up, operate and scale a relational database in the cloud.

   What's the need of using RDS service ?

   - AWS takes over many of the difficult and tedious management tasks of a relational database.
   - Handles time consuming taks such as database setup, patching, backups, and routine maintenance
   - **Scalability and performance**
     RDS enables us to scale our database as our application grows. we can choose appropriate database istance size and scale up or down according to our need.

     **key points:**

   - Simplified Management
   - Time Saving
   - Reliable and Resilient(automatic backups, replication, and failover to ensure data durability and high availability.)
   - Compatible(mysql,oracle,postgresql)
   - Security integration with IAM
   - Monitoring and Metrics
   - Cost Optimization(ability to stop or pause if there is low demand)

6. **LAMBDA**
   AWS Lambda is a compute service that lets you run code without provisioning or managing servers.
   we provide or organize our code in lamda function then when a request comes it computes the result for us and we only pay when lamda is performing some tasks

   **key points:**

   - Code Execution
   - No Server Management
   - Compute on Demand
   - Pay for Usage

   can be used to convert video of different formats

7. **API GATEWAY**
   Service that makes it wasy to create,deploy, and manage APIs at any scale. act as a front door for bakend services

   Simplify the process of creating and managing APIs

   **key points:**

   - API Management(centralized platform for managing and hosting APIs)
   - API Deployment(easily deploy APIs to different stages->development,testing,and production)
   - API Authorization and Authentication

8. **SES(Simple Email Service)**
   It's a cloud based email sending and recieving service. allows to send and recieve emails using your application or system without the need to manage ane email server.

   **key points:**

   - Email Sending
   - High Deliverability
   - Content Management
   - Email Recieving and processing(configure to store in s3 bucket or rrigger AWS labda function to perform action)
   - Cost-Effective

9. **SQS(Simple Queue Service)**
   Fully managed messaged queuing service.
10. **SNS(Simple Notification Service)**

    Fully managed messaging service. enables to send messages or notifcations to a variety of endpoints, such as emails, SMS,mobile push notifications.

    **key points:**

    - Message Brodcasting
    - Flexible format support
    - multi-protocol support
    - Integration with aws services(s3 bucket)

    Example: food restaurant website notification when order reaches the location

11. **VPC(Virtual Private Cloud)**
    allow to create and manage your own isolated virtual network within the aws cloud environment.
12. **ROUTE 53**
    DNS Service
13. **CloudFront**

    it's CDN service in aws

    it uses Edge Location to extract data

14. **ElasticCache**(for cache like redis)
15. **Rekoginition**(for filter content ex nudity)
16. **Cloud Watch** used to monitor the entire application
17. **KMS(Key Management System)** used to encrypt data
