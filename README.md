# FlappyBird

Diese Anleitung zeigt wie man eine Version vom bekannten Handyspiel FlappyBird in Python mit PyGame scheiben kann. 
Zuerst muss ( sofern nicht schon erfolgt ) pygame installiert werden über : 
  ```python
  python -m pip install pygame 
  ```

Wenn das funktioniert hat kann man die Python Datei in einem beliebigen Editor erstellen. 
Der Vollstände Code befindet sich zum nachschlagen in der Datei FlappyBird.py
Dieses Projekt wurde Objektorientiert erstellt. Das heißt letzendlich nur alle Elemente vom Spiel 
einem Spielobjekt zugeordnet werden. Im Synthax werden diese dann immer über  ```self. ``` aufgerufen. 
Das beudetet nur dass dieses Attribut bzw. Variable zu dem entsprechenden Objekt gehört. 
Es ist jedoch nicht nötig das ganze Objektorientiert zu schreiben. Mann kann es auch problemlos "normal" programmieren.

## Schritt 1: imports 
Als erstes schauen wir uns die Imports an. Ein import fügt unserem Programm einfach bereits geschriebenen Code hinzu den wir dann weiter verwenden können. Für dieses Projekt brauchen wird einerseits Pygame und zusätzlich noch die in Python vorhandene random funktion.
  ```python
  import pygame
  import random
  ```
  
## Schritt 2: Pygame Fenster Aufsetzten 
PyGame als unsere Spieleengine ermöglicht es uns ziemlich einfach ein Fenster zu erstellen, in das wir dann Bilder und Texturen zeichnen können. Dieses Fenster können wir mit folgenden Befehlen erstellen : 
 ```python
  pygame.init()
  self.SCREEN = pygame.display.set_mode((self.screenWidth,self.screenHeight))
  ```

