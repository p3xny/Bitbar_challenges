For the test to work correctly, you have to:
	I. Install modules from "requirements.txt" file using "pip" (package installer for python)
	   in your CLI (Command Line Interface, i.e.: command prompt - Windows / terminal - Linux)		
	   To install it, you have to:
			1. Open the CLI in the same folder as "requirements.txt" file.
			2. Enter command "pip install --upgrade -r requirements.txt" without "".
	
	II. Download Chromium (Google Chrome webdriver) version that best matches your Google Chrome browser version
		NOTE:
			- Version of the webdriver shouldn't be signed with a higher number than the version of your browser.
			- To check your current Google Chrome version, type "chrome://version" in the browsers search bar.
	
	III. Create "SeleniumDrivers" folder in your "C:\" directory.

	IV. Transfer the downloaded "chromedriver.exe" to "C:\SeleniumDrivers" directory.

	V. Now you should be able to successfully run the tests from the "bitbar_challenges.py" file.
		Note:
			- You can run a python file with the use of CLI, while in the same folder simply type:
				1. "python bitbar_challenges.py" without "" or
				2. "python3 bitbar_challenges.py"
