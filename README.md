# Twitter Data Pipeline using SnowFlake
## Project Description
  ![image](https://user-images.githubusercontent.com/48169929/226802676-755f4bdb-9cb4-43f1-ac35-2072fccddbed.png)
1. For the **Data Collection phase**, we utilized Python and the snscrape package to extract tweets related to a specific keyword from Twitter.
2. In the **Apache Airflow Setup phase**, we set up an EC2 instance on Amazon Web Services and installed Apache Airflow on it and downloded the necessary packages.
3. During the **Airflow DAG Creation phase**, we developed an Airflow DAG (Directed Acyclic Graph) that outlined the workflow for extracting and storing tweets in S3. This involved creating tasks for extracting tweets, transforming them into a suitable format for storage in S3, and then uploading them to S3.
4. To enable **Data Storage**, we created an S3 bucket on Amazon Web Services and configured the necessary permissions to store the extracted tweets.
