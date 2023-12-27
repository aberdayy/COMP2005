<b>Encryption Decrypting Application</b>

This code creates a simple graphical user interface (GUI) using the tkinter library in Python. The GUI has two text boxes where you can input data and a pair of buttons for encryption and decryption.

Here's what each part of the code does:

Import Libraries: It imports necessary libraries - Fernet from cryptography.fernet for encryption and decryption, and tkinter for GUI.

GUI Initialization: It sets up the main window (master) with a title, size, and geometry.

Functions:

Encrypt(): Reads input from the first text box, generates an encryption key, encrypts the input message, displays the original and encrypted messages, saves the encryption key and encrypted message to a file named "demo.txt".
Decrypt(): Reads input from the first text box as the encrypted message and the second text box as the decryption key. It decrypts the message using the provided key and displays the decrypted message.
GUI Components:

Labels (lbl) for displaying text information.
Text boxes (inputtxt and keyInput) for user input.
Buttons (EncryptButton and DecryptButton) that trigger the encryption and decryption functions respectively.
Main Loop: master.mainloop() starts the main event loop, allowing the GUI to be displayed and interacted with by the user.

This code essentially creates a simple interface for encrypting and decrypting messages using the Fernet symmetric encryption scheme and allows users to input text for encryption and decryption.





