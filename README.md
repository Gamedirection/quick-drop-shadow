# quick-drop-shadow
Add a nice drop shadow to your text strips in Blender's video sequence editor

Hi, this is a script that I knocked together in an afternoon using chat GPT.

You can learn more about why i made it and how it works at: https://youtu.be/JINxCFVuouo

Use: Select a text strip in the VSE and, using the f3 menu, search "add text drop shadow". You can add this operator to quick favorites by right clicking on it. Zoom

Limitations:
1. If the text strip you are adding a shadow to has anything occupying tho two channels beneath it, the script will toss the new shadow strips somewhere random in your project.
2. Can't add shadows to multiple text strips at the same time.

Installation:

To load and use your script in Blender, you have several options, ranging from running the script directly in Blender's Text Editor to installing it as an add-on. Here's a step-by-step guide for both methods:
Running the Script Directly in Blender
	1. Open Blender: Start by launching Blender.
	2. Open the Text Editor: In Blender, switch one of the viewports to the Text Editor. You can do this by clicking on the editor type selection button (in the top-left corner of any viewport) and choosing "Text Editor".
	3. Open or Paste Your Script: You can either paste your script directly into the Text Editor or open your script file by clicking "Open" in the Text Editor's header and navigating to your script file.
	4. Run the Script: After your script is in the Text Editor, click the "Run Script" button in the Text Editor's header. This executes the script and registers your operator and panel in the UI.
Installing the Script as an Addon
	To make your script easily reusable across Blender projects, you can install it as an addon. First, ensure your script has the proper bl_info block at the top (which you have), as this is required for Blender addons. Then, follow these steps:
	1. Save Your Script: Save your script to a .py file on your computer if you haven't done so already.
	2. Open Blender and Go to Preferences:
		- Open Blender.
		- Go to "Edit" > "Preferences".
	3. Install the Addon:
		- In the Preferences window, switch to the "Add-ons" section.
		- Click "Install..." at the top of the window.
		- Navigate to where you saved your .py file, select it, and click "Install Add-on".
	4. Activate the Addon:
		- After installation, the addon should appear in the list. However, it might not be enabled by default. Use the search box to find your addon by the name you gave it in the bl_info block.
		- Once you find your addon in the list, check the checkbox next to its name to activate it.
	5. Save Preferences (Optional):
		- If you want Blender to enable this addon by default in new projects, click the "Save Preferences" button at the bottom left of the Preferences window.
After following either method, your script will be running in Blender. If you installed it as an addon, you would find your new panel in the specified category (e.g., "Tool") in the Sequencer's UI side panel, accessible by pressing 'N' in the Sequencer or clicking on the arrow on the right side of the Sequencer to expand the side panel.
