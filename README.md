# Twitter Data Pipeline using SnowFlake
## Project Description
  ![image](https://user-images.githubusercontent.com/48169929/226802676-755f4bdb-9cb4-43f1-ac35-2072fccddbed.png)
1. **Data Collection**: In this phase, we used Python and the snscrape package to extract tweets related to a specific keyword from Twitter.
2. **Apache Airflow Setup**: In this phase, we created an EC2 instance on Amazon Web Services and installed Apache Airflow on it.
3. **Airflow DAG Creation**: In this phase, we created an Airflow DAG (Directed Acyclic Graph) that defines the workflow for extracting and storing tweets in S3. The DAG will include tasks for extracting tweets, transforming them into a format suitable for storage in S3, and uploading them to S3.
4. **Data Storage**: In this phase, you will create an S3 bucket on Amazon Web Services and configure the necessary permissions for storing the extracted tweets.
