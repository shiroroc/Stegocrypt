# StegoCrypt

StegoCrypt is a **steganography-based tool** that allows users to securely hide secret messages within images. By combining steganography (hiding data within images) with password protection, StegoCrypt ensures that your private communications remain confidential and secure.

This project is lightweight, easy to use, and built using Python, OpenCV, and NumPy.

---

## Features ✨

- **Hide Secret Messages**: Embed text messages inside images without visibly altering the image.
- **Password Protection**: Secure your hidden messages with a passcode for added security.
- **Simple and Lightweight**: Built using Python, OpenCV, and NumPy for efficient and easy-to-understand implementation.
- **Cross-Platform**: Works on any system with Python installed.

---

## Technologies Used 🛠️

- **Python**: The core programming language used for the project.
- **OpenCV**: For image processing and manipulation.
- **NumPy**: For handling pixel data and numerical operations.

---

## How to Use 🚀

### Step 1: Download Python
If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

### Step 2: Clone the Repository
Clone the StegoCrypt repository to your local machine:
```bash
git clone https://github.com/shiroroc/Stegocrypt.git
cd Stegocrypt
```

### Step 3: Install Required Libraries
Install the required Python libraries using pip:
```bash
pip install opencv-python numpy
```

### Step 4: Embedding the message (Hiding the Message)
1. Run the script:
   ```bash
   python stegocrypt.py
   ```
2. Choose the **embed text (1)** option.
3. Provide the path to the image file where the message will be hidden.
4. Enter the secret message you want to hide.
5. Set a passcode for added security.
6. The tool will generate a new image file (`stego_output.png`) containing the hidden message.

### Step 5: Extracting the message (Revealing the Message)
1. Run the script:
   ```bash
   python stegocrypt.py
   ```
2. Choose the **extract text (2)** option.
3. Provide the path to the embedded image file (`stego_output.png`).
4. Enter the passcode used during embedding.
5. The tool will extract and display the hidden message.

---

## Sample Output 📜

![image](https://github.com/user-attachments/assets/2be2bbd7-afef-4236-a802-b4e375def079)




