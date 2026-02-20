import os
import cv2

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

    # Sort images to keep processing order consistent
    files.sort()

    return files


def main():
    # Define where input images are stored
    data_dir = "data"

    # Get all image file paths
    image_paths = list_images(data_dir)

    # Stop if no images are found
    if not image_paths:
        print(f"No images found in: {data_dir}")
        return

    # Select the first image for testing
    first_path = image_paths[0]

    # Load the image using OpenCV (allowed)
    img = cv2.imread(first_path)

    # Stop if image failed to load
    if img is None:
        print(f"Failed to load image: {first_path}")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Print basic information about the image
    print("Loaded:", os.path.basename(first_path))
    print("Original shape (H, W, C):", img.shape)
    print("Gray shape (H, W):", gray.shape)
    print("Data type:", gray.dtype)


# Run main function
if __name__ == "__main__":
    main()