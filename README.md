# Favorite LoL Champions
## Introduction
Ever wondered how many games you or your friends have played on each champion? This Python application will graph that for you. Just create a .txt file called api-key.txt, which contains your Riot Games API key, in the same directory as all of the .py files. Then, run gui.py to see the names of champions graphed on the y-axis and the number of games played on that champion on the x-axis. You can also download the .exe and .app files below, too.

## Screenshots
![GUI Prompting User to Enter Summoner Name](https://i.postimg.cc/hvLsT8BL/GUI-example.png)

![Graph of the Number of Times Each Champion Was Played](https://i.postimg.cc/RVf5p2Md/acofspads.png)

## Link to .exe and .app files
[.exe file (Windows)](https://drive.google.com/file/d/1IK2Yn6Lgaq9Ozs2Pd_zNnMapN0oywPw4/view?usp=sharing)

[.app file (MacOS)](https://drive.google.com/drive/folders/1YTI2FNBYyIplQ4Vw0k1qnvJ3qCPYHVhE?usp=sharing)

## Technologies Used
This app gets data from Riot's API and then plots it using Matplotlib. It also uses tkinter for the GUI that users can input summoner names into. Finally, it uses PyInstaller to package the app into .exe and .app files.

## Problems
- The .exe and .app files will stop working when my API key expires. It may be better to fork the repository and add a file named api-key.txt, which contains your Riot Games API key, in the same directory as all of the .py files.
- The app is limited to the data that Riot has in their API, so it may only count games played from season 5 and on.
