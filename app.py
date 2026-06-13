from src.image_viewer import show_image
from src.object_detection import detect_objects


print("AI Image Processing Project")
print("---------------------------")

print("1 - View Image")
print("2 - Object Detection")

choice = input("Choose option: ")


if choice == "1":
    show_image()

elif choice == "2":
    detect_objects()

else:
    print("Invalid choice")
