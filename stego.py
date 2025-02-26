import cv2
import numpy as np

def embed_text(image_path, message, password, output_path="stego_output.png"):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return

    # Convert the message to binary
    binary_message = ''.join(f"{ord(char):08b}" for char in message) + '00000000'
    index = 0

    # Embed the message into the image
    for row in img:
        for pixel in row:
            for channel in range(3):  # Iterate over BGR channels
                if index < len(binary_message):
                    bit = int(binary_message[index])
                    # Ensure the value is non-negative and within 0-255
                    value = (pixel[channel] & 0xFE) | bit  # Clear LSB and set to bit
                    pixel[channel] = np.uint8(value)  # Cast to uint8
                    index += 1

    # Save the stego image
    cv2.imwrite(output_path, img)
    print(f"Message embedded. Saved as {output_path}")

def extract_text(image_path, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return

    # Extract the binary message from the image
    binary_message = ""
    for row in img:
        for pixel in row:
            for channel in range(3):  
                binary_message += str(pixel[channel] & 1)
                # Stop if we've extracted enough bits (including the end marker)
                if len(binary_message) % 8 == 0 and binary_message.endswith('00000000'):
                    break
            else:
                continue
            break
        else:
            continue
        break

    # Debugging: Print the extracted binary message
    print("Extracted Binary Message:", binary_message)

    # Split the binary message into 8-bit chunks
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    
    # Debugging: Print the binary chunks
    print("Binary Chunks:", chars)

    # Convert binary to text
    message = ""
    for char in chars:
        if char == "00000000":  # End-of-message marker
            break
        try:
            # Convert binary to integer and then to character
            message += chr(int(char, 2))
        except ValueError:
            print(f"Skipping invalid binary chunk: {char}")

    if message:
        print("Extracted Message:", message)
    else:
        print("No message extracted. Check if the stego image is valid.")

if __name__ == "__main__":
    choice = input("Choose an option: (1) Embed Text (2) Extract Text: ").strip()
    
    if choice == "1":
        img_path = input("Enter image path: ").strip().strip('"')
        msg = input("Enter secret message: ")
        key = input("Enter password: ")
        embed_text(img_path, msg, key)
    
    elif choice == "2":
        img_path = input("Enter stego image path: ").strip().strip('"')
        key = input("Enter password: ")
        extract_text(img_path, key)
    else:
        print("Invalid option.")