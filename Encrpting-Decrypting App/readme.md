<b>Encryption Decrypting Application</b>

<b><i>How to Use</i></b></br>
<b>For Encrypting </b></br>
1-Give your desired input to the 'Data' field.</br>
2-Click 'Encrypt Data' button</br>
3-You should be able to see the encrypted version of your data. (You cannot copy this data)</br>
4-You can not reach your master key via application for security reasons.</br></br>
</br><b>For Decrypting </b></br>
1-Give your encrypted data to 'Data' field.</br>
2-Give your master key to the second input box.</br>
3-Press the 'Decrypt Data' field.</br>
4-You should be able to see the encrypted version of your data.</br>

<b>For security reasons master key and encrypted data only reacheable via Demo.txt file.</b></br></br>

<b><i>Explanation</i></b><br>
This code creates a simple graphical user interface (GUI) using the tkinter library in Python. The GUI has two text boxes where you can input data and a pair of buttons for encryption and decryption.
Functions:
Encrypt(): Reads input from the first text box, generates an encryption key, encrypts the input message, displays the original and encrypted messages, saves the encryption key and encrypted message to a file named "demo.txt".
Decrypt(): Reads input from the first text box as the encrypted message and the second text box as the decryption key. It decrypts the message using the provided key and displays the decrypted message.

GUI Components:
Labels (lbl) for displaying text information.
Text boxes (inputtxt and keyInput) for user input.
Buttons (EncryptButton and DecryptButton) that trigger the encryption and decryption functions respectively.
Main Loop: master.mainloop() starts the main event loop, allowing the GUI to be displayed and interacted with by the user.

This code essentially creates a simple interface for encrypting and decrypting messages using the Fernet symmetric encryption scheme and allows users to input text for encryption and decryption.





