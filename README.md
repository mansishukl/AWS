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



![Screenshot 2024-08-26 145032](https://github.com/user-attachments/assets/280d2949-2142-45d2-8b5e-fb19e5a42931)

![Screenshot 2024-08-26 144859](https://github.com/user-attachments/assets/0948a2d2-bf94-46c5-bc14-a916a019cf06)

![Screenshot 2024-08-26 144756](https://github.com/user-attachments/assets/c38c7a09-58fe-499c-87f3-e965484b022c)

![Screenshot 2024-08-26 144715](https://github.com/user-attachments/assets/bc0997ec-3b6c-47ee-9a14-42fef45d8508)

![Screenshot 2024-08-26 144627](https://github.com/user-attachments/assets/fa5541e2-b5c1-404a-b602-118914f1c5a4)

![Screenshot 2024-08-26 144507](https://github.com/user-attachments/assets/206fd577-fc66-4f59-9590-33be665b7239)

![Screenshot 2024-08-26 144348](https://github.com/user-attachments/assets/074f0c75-80e8-487e-a8e2-8a5950e58513)

![Screenshot 2024-08-26 145946](https://github.com/user-attachments/assets/5bcbe478-b722-4997-b64d-de060985bd0f)

![Screenshot 2024-08-26 151327](https://github.com/user-attachments/assets/0ec6a901-05bd-4ef9-a8f0-d718a17243eb)

![Screenshot 2024-08-26 151327](https://github.com/user-attachments/assets/d036dd36-9e1a-42b2-a40b-7518f903dc98)

![Screenshot (122)](https://github.com/user-attachments/assets/bee9fd0e-9768-4873-b80c-fe95077ed56a)

![Screenshot (124)](https://github.com/user-attachments/assets/adeac769-adb1-49d7-bccf-2732d654ba0f)

![Screenshot (125)](https://github.com/user-attachments/assets/4de8ef1a-549e-4c30-8697-c6b9e2f27968)





