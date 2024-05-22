## Description of main.py

`main.py` is a Python script that implements a speech recognition system. It listens for specific trigger phrases and executes commands based on the recognized phrases. The script utilizes the SpeechRecognition library to capture audio input from the microphone and Google Web Speech API for speech recognition.

### Functionality:
- Listens for trigger phrases such as "Jana turn off my PC" or "Jana hibernate my PC".
- Executes corresponding actions like shutting down or hibernating the PC when trigger phrases are recognized.

### Dependencies:
- speech_recognition: Library for speech recognition.
- os: Standard library module for interacting with the operating system.

## Instructions for Creating Executable

To create an executable from `main.py`, you can use PyInstaller, a popular Python package that converts Python scripts into standalone executables.

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Navigate to the directory containing main.py using the command line.

3. Run PyInstaller to generate the executable:
    ```bash
    pyinstaller --onefile --noconsole --name JanaAssistant main.py
    ```
This command will create a single executable file named JanaAssistant.exe without a console window.

4. After the process completes, you can find the generated executable in the dist directory within your project folder.

### Additional Notes:
Include any additional information or tips that might be helpful for users, such as troubleshooting tips or customization options.

Example:
```markdown
## Additional Notes

- If you encounter any errors during the PyInstaller process, make sure all dependencies are installed and up to date.

- You can customize the behavior of the executable by modifying the trigger phrases and corresponding actions in `main.py` before creating the executable.


**make it run on windows boot**


