from PIL import Image
from PIL import ImageFilter

# Method to apply the filter
def applyMaximumFilter(image):
    return image.filter(ImageFilter.MaxFilter);

# Load the image
imagePath   = "matahari2.jpeg";
imageObject = Image.open(imagePath);

# Apply maximum filter
filterApplied = imageObject;
for i in range(0, 10):
    print(i);
    filterApplied = applyMaximumFilter(filterApplied);

# Display images
imageObject.show();
filterApplied.show();