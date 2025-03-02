Postmortem Report DR#403

Postmortem: E-commerce Platform Outage - 30 January 2025 12:30 CAT to 30 January 2025 15:20 CAT

Issue Summary:
Our e-commerce platform experienced a service outage lasting for 2 hours and 20 minutes, impacting 100% of users during peak buying hours on the 30th of January 2025. Users encountered error messages while trying to add items to their carts and proceed to checkout.
The root cause of the outage was identified as a surge in traffic due to an unannounced flash sale promotion.

Timeline:

30 January 2025 12:30 CAT: Monitoring alerts indicated a significant increase in website traffic.

30 January 2025 12:50 CAT: Engineers observed a spike in API calls to the shopping cart functionality.

30 January 2025 12:55 CAT: The shopping cart service became unresponsive, causing errors for users.

30 January 2025 12:55 - 14:05 CAT: The engineering team initially investigated potential database connection issues and application errors. This path proved to be a dead end as resources were functioning within normal parameters.

30 January 2025 13:55 CAT: The incident was escalated to the infrastructure team after identifying the issue was likely related to server capacity limitations.

30 January 2025 14:45 CAT: The infrastructure team initiated horizontal scaling of the shopping cart service instances to handle the increased load.

30 January 2025 15:20 CAT: The shopping cart service recovered, and normal functionality resumed.

30 January 2025 16:00 CAT: The post-incident review process commenced.

Root Cause and Resolution:

The outage was caused by an unexpected surge in traffic exceeding the capacity of our shopping cart service. This surge was attributed to a flash sale promotion that was not communicated to the engineering team for proper load balancing adjustments.

To resolve the issue, the infrastructure team horizontally scaled the shopping cart service instances, allowing for more efficient handling of the increased user load. This restored normal functionality to the platform.

Corrective and Preventative Measures:

Improved communication: Implement a mandatory notification process for marketing and sales promotions to ensure the engineering team can prepare for potential traffic spikes.

Capacity planning: Conduct regular load testing that simulates real-world traffic scenarios, including flash sales, to identify and address capacity limitations proactively.

Monitoring enhancements: Fine-tune monitoring alerts to trigger based on specific metrics related to the shopping cart service, such as API call volume and response times. This will allow for faster identification of performance bottlenecks.

Automatic scaling: Investigate and implement automated horizontal scaling solutions for critical services to handle unexpected traffic surges without requiring manual intervention.



This postmortem report serves as a learning experience to prevent similar outages in the future. By implementing the corrective and preventative measures outlined above, we can ensure a more resilient and scalable ecommerce platform that can handle peak traffic demands.

