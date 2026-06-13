from src import image_viewer
from src import object_detection


print("AI Image Processing Project")
print("1 - View Image")
print("2 - Object Detection")

choice = input("Choose option: ")

if choice == "1":
    image_viewer

elif choice == "2":
    object_detection

else:
    print("Invalid choice")
