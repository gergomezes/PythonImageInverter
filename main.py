import os
import cv2

# Define input and output folders
input_folder = "Original"
output_folder = "Edited"

# Create the output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Get the list of image files in the input folder
files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Process each image
for file in files:
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file)

    # Load the image
    image = cv2.imread(input_path)

    if image is None:
        print(f"Error loading: {file}")
        continue

    # Invert colors
    inverted_image = cv2.bitwise_not(image)

    # Save the processed image
    cv2.imwrite(output_path, inverted_image)

    # Print status to terminal
    print(f"Processed: {file}")

print("All images have been processed.")