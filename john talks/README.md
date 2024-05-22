## Description of main.py

`main.py` is a Python script implementing a voice-controlled assistant system. It utilizes the SpeechRecognition library to capture audio input from the microphone and the Google Web Speech API for speech recognition. The script listens for specific trigger phrases and executes corresponding actions based on the recognized phrases.<br><br>
**Why "John"?** After testing various names, I discovered that many were misinterpreted. For example, when I said "teddy" (the previous name), the program recognized it as "daddy" 😂. "John" is the most universally recognized and straightforward name I found.

### Functionality:
- Listens for trigger phrases such as:
  - "john banana" (turn off my PC and exits the program)
  - "john hibernate" (hibernates the PC and exits the program)
  - "john lock" (locks the PC and doesn't exit the program)
  - "bye john" (exits the program)
- Executes corresponding actions like:
  - Shutting down the PC
  - Hibernating the PC
  - Locking the PC
- Supports termination by saying "Bye John".

### Dependencies:
- `speech_recognition`: Library for speech recognition.
- `os`: Standard library module for interacting with the operating system.



## Instructions for Creating Executable

To create an executable from `main.py`, you can use PyInstaller, a popular Python package that converts Python scripts into standalone executables.

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Navigate to the directory containing main.py using the command line.

3. Run PyInstaller to generate the executable:
    ```bash
    pyinstaller --onefile --noconsole --name johnTalks main.py
    ```
This command will create a single executable file named JanaAssistant.exe without a console window.

4. After the process completes, you can find the generated executable in the dist directory within your project folder.

### Additional Notes:
Include any additional information or tips that might be helpful for users, such as troubleshooting tips or customization options.

Example:
## Additional Notes

- If you encounter any errors during the PyInstaller process, make sure all dependencies are installed and up to date.

- You can customize the behavior of the executable by modifying the trigger phrases and corresponding actions in `main.py` before creating the executable.


## ➕ Make it run on windows boot (Additional section)
<a href="https://support.microsoft.com/en-us/windows/add-an-app-to-run-automatically-at-startup-in-windows-10-150da165-dcd9-7230-517b-cf3c295d89dd">Microsoft guide</a>
- With the file location open, press the Windows logo key  + R, type shell:startup, then select OK. This opens the Startup folder.
- Create a copy of the original exe and paste it into autostart folder ![image](https://github.com/matiwan3/project-scripts-and-scrappers/assets/93386476/bcd4593c-b4f9-4004-87dd-3b6bd6412096)
- In the autostart tab you should see now that our johnTalks is added and enabled ![image](https://github.com/matiwan3/project-scripts-and-scrappers/assets/93386476/91649329-03b5-42c3-9b42-93fd1556be77)



