import os
import cv2
import time

# Supported image file extensions
IMAGE_EXTS = (".png", ".jpg")


# Get a sorted list of image paths from the data folder
def list_images(data_dir: str) -> list[str]:
    # Store valid image file paths
    files = []

    # Loop through files in the data directory
    for name in os.listdir(data_dir):

        # Check if file ends with a supported image extension
        if name.lower().endswith(IMAGE_EXTS):
            # Add full file path to list
            files.append(os.path.join(data_dir, name))

    # Sort files numerically based on the number in the filename
    files.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x)))))

    return files

# Convert BGR image to grayscale manually
def convert_to_grayscale(img):

    # Get image height and width
    height, width, _ = img.shape

    # Create empty grayscale image
    gray = []

    # Loop through each pixel
    for i in range(height):
        row = []
        for j in range(width):

            # Extract B, G, R values
            b = img[i][j][0]
            g = img[i][j][1]
            r = img[i][j][2]

            # Compute grayscale using weighted formula
            intensity = int(0.299 * r + 0.587 * g + 0.114 * b)

            row.append(intensity)

        gray.append(row)

    return gray

# Process a single image
def process_image(path: str):
    # Load image
    img = cv2.imread(path)

    # Skip if loading failed
    if img is None:
        print(f"Failed to load image: {path}")
        return

    # Convert to grayscale
    gray = convert_to_grayscale(img)

    # Print image information
    print("Processing:", os.path.basename(path))
    print("Original shape (H, W, C):", img.shape)
    print("Gray shape (H, W):", (len(gray), len(gray[0])))
    print("-" * 40)

def main():
    # Define input image folder
    data_dir = os.path.join("..", "data")

    # Get all image paths
    image_paths = list_images(data_dir)

    # Stop if folder is empty
    if not image_paths:
        print(f"No images found in: {data_dir}")
        return

    print(f"Found {len(image_paths)} images.\n")

    # Loop through every image
    for path in image_paths:
        # Start timing
        start_time = time.perf_counter()

        # Call image processing function
        process_image(path)

        # Stop timing
        end_time = time.perf_counter()

        # Calculate processing time
        processing_time = end_time - start_time

        # Print processing time
        print(f"Processing time: {processing_time:.6f} seconds")
        print("=" * 40)


# Run main function
if __name__ == "__main__":
    main()