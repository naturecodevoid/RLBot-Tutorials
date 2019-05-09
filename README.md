Status: active development
#
# RLBot-Tutorials
All the scripts from the RLBot tutorial series by Blocks_ (@TheBlocks) on https://www.reddit.com/r/RocketLeagueBots/.
Scripts are being updated, fixed, and maintained by @naturecodevoid

Note: I'm not focusing *at all* on the Advanced Bot. Right now, the changes listed below **are for How to make a RL bot** ***only***. 

## Running

I warn you, don't read this giant essay. Just read the numbered instructions below the essay. The essay is also a little different and I recommend the list.

So, you want to run the bots the easiest way, huh? Well, I fully recommend RLBot's new gui, which can be downloaded at their wiki, which is located at https://github.com/RLBot/RLBot/wiki. **BUT BEFORE YOU OPEN THAT SETUP**, ***make sure you download Python 3.7 at https://python.org/downloads/***. After you've installed the gui, you might want to have a look at the Antivirus notes on their wiki (https://github.com/RLBot/RLBot/wiki). As stated there, you may have to add exclusions for the dll in the AppData for RLBotGui. The next step is to get started with RLBot/RLBotPythonExample. Download it, but you can delete everything besides the license (to be safe with the license :smile:), the rlbot.cfg file, and the python_example folder. If you want the training too, don't delete it. Now, copy any of the tutorials in this or TheBlocks/RLBot-Tutorials repository and replace python_example/python_example.py. Now, don't worry! If you want that code back, just go back to the RLBot/RLBotPythonExample repository. Now, run the newly installed gui and add your rlbot.cfg file or the python_example folder. Press start match. You'll get a pop-up on steam saying that it needs to open Rocket League the rlbot way. Press ok. You should see RL pop up and a match beginning with the bots you selected on the gui. If not, try press start match again, or close RL and the gui and try it again. If your *still* having problems like I did, ask people on the Discord. Anyways, thanks for reading my running essay. :smile: I'll also re-write this in steps:

1. Download Python 3.7 at https://python.org/downloads/
1. Open the python 3.7(or 37) setup (which is probably in your downloads folder). Wait for it to install.
1. You may also need to download and install Java, but you probably won't have to. I was fine and was able to run my bot but it gave me some warning/errors so I downloaded Java.
1. Download RLBot's gui at https://github.com/RLBot/RLBot/wiki 
1. Open the gui setup (which is probably in your downloads folder). Wait for it to install.
1. Download RLBot/RLBotPythonExample at https://github.com/RLBot/RLBotPythonExample/
1. In start, open RLBotGui.
1. Add your python_example folder to the gui or the rlbot.cfg to the gui.
1. Paste any of the code in this/TheBlocks' in python_example/python_example.py
1. Press start match.
1. A confirmation will pop upin steam. Press ok.
1. Wait for RL to open. A match will hopefully start
1. If not, press start match again.

## Changelog:

- Add `import`s for rlbot
- Change `Agent` to `PythonExample(BaseAgent)` so you can copy 'n paste into `RLBot/RLBotPythonExample/python_example/python_example.py`
- Change `distance` function to global on part 4 + part 5
- Add a controller for parts missing one and assigning it with `self.<controllerPart>`
