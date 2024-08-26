# AWS Rekognition Face Recognition Project

This project demonstrates a simple face recognition system using AWS Rekognition and Python. The system detects faces in images stored in an Amazon S3 bucket and analyzes various facial attributes, including emotions, age range, and gender.

## Features

- Detect faces in images using AWS Rekognition.
- Analyze facial attributes like emotions, age range, and gender.
- Simple and beginner-friendly Python implementation.

## Prerequisites

- **AWS Account**: You need an AWS account with access to Amazon Rekognition and S3 services.
- **Python 3.x**: Ensure you have Python 3.x installed.
- **AWS CLI**: Install the AWS CLI and configure your credentials.

1. Upload Images to S3
Upload the images you want to analyze to your S3 bucket. For example, if you want to detect faces in an image called face1.jpg, you should upload it to your bucket.


2. Install Required Python Packages
Install the necessary Python packages using pip:

bash
Copy code
pip install boto3

3. Configure AWS Credentials
Use the AWS CLI to configure your credentials:

bash
Copy code
aws configure
Provide your AWS Access Key ID, Secret Access Key, default region name, and output format (e.g., json).

4. Write Python Code to Use AWS Rekognition
import boto3

# Initialize the Rekognition client
rekognition = boto3.client('rekognition')

# Define the S3 bucket and image
bucket_name = 'your-bucket-name'  # Replace with your bucket name
image_name = 'your-image-name.jpg'  # Replace with your image name

# Call AWS Rekognition to detect faces
response = rekognition.detect_faces(
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': image_name
        }
    },
    Attributes=['ALL']  # Analyze all facial attributes (e.g., emotions, age range)
)

# Print the detected face details
for faceDetail in response['FaceDetails']:
    print(f"Confidence: {faceDetail['Confidence']:.2f}%")
    print("Emotions:")
    for emotion in faceDetail['Emotions']:
        print(f"  {emotion['Type']}: {emotion['Confidence']:.2f}%")
    print(f"Gender: {faceDetail['Gender']['Value']}")
    print(f"Age Range: {faceDetail['AgeRange']['Low']} - {faceDetail['AgeRange']['High']}\n")

5. Run the Script
Execute the script by running it in your Python environment. The script will analyze the image using AWS Rekognition and print details about the detected faces, such as confidence levels, emotions, gender, and age range.

6.Example Output
When you run the script, it might produce output like this:

Confidence: 99.87%
Emotions:
  HAPPY: 85.50%
  CALM: 12.00%
  SURPRISED: 2.50%
Gender: Male
Age Range: 25 - 35

7. Clean Up
After running your project, make sure to delete any unnecessary resources like S3 buckets or uploaded images to avoid incurring charges.
