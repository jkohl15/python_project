# Curling League Manager
This project brings together various classes and a user interface to create a functioning league management solution.  Team members, teams, competitions, and leagues can all be utilized in this solution.  
- Each team member can be given a name and email address.
- Teams can be given a name and are composed of a list of team members.
- Competitions include the teams involved, the location of the game, and the time of the game.
- The league can be given a name, includes a list of all the participating teams, and includes a list of all competitions.
- The league database is used to keep track of all leagues being managed.  A few features of this database include the ability to import leagues, export leagues, save leagues, and load previously saved leagues.  
- The user interface includes three levels of dialog boxes.  The top level of the user interface allows leagues to be saved, loaded, added, imported, deleted, and edited.
- The second level of the user interface allows for editing selected leagues.  Teams in the selected league can be added, deleted and edited.  Also, the selected league can be exported as a CSV file.
- The third and final layer of the user interface allows for editing selected teams.  Team members can be added, deleted, and updated in selected teams. 

The Curling League Manager utilizes a few external packages.  Yagmail and keyring are used to support active email functionality to participants in the league.  This email functionality is not a part of the user interface.
 