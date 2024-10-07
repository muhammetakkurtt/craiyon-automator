# CraiyonAutomator

CraiyonAutomator is a tool that automates the Craiyon image generation process. This project allows users to automatically process multiple prompts and save the URLs of the generated images.

## Features

- Graphical interface
- Batch processing of multiple prompts
- Automatic image generation and URL capture
- Save results in JSON format

## System Requirements

This project has been tested only on Windows and Ubuntu operating systems.

## Tools and Plugins Used

The following open-source tools and plugins are used in this project:

- [Selenium-Driverless](https://github.com/kaliiiiiiiiii/Selenium-Driverless)
- [CDP-Patches](https://github.com/Kaliiiiiiiiii-Vinyzu/CDP-Patches)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/muhammetakkurtt/craiyon-automator.git
   ```

2. Navigate to the project directory:
   ```
   cd craiyon-automator
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the program:
   ```
   python main.py
   ```

2. In the opened interface, enter your prompts, one per line.

3. Click the "Generate Images" button and wait for the process to complete.

4. Once the process is complete, the URLs of the generated images will be saved in the `generated_images.json` file.

### Development Suggestions

- **Performance Improvement**: Time optimization can be done for faster operation.
- **Cloudflare Captcha Solution**: A more effective method can be developed for Cloudflare captcha.

## License

This project is licensed under the MIT license. For more information, see the `LICENSE` file.

## Contact

For questions or feedback, please open an issue or contact me via [e-mail](muhammetakkurtt@icloud.com).