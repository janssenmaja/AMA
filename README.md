# Ray Tracing auf Freiformflächen: Vergleich des Newton- und des Broyden-Verfahrens

## 1. Projektbeschreibung

Dieses Projekt berechnet Schnittpunkte zwischen einem Strahl und einer bikubischen Bézier-Fläche. Dazu wird ein nichtlineares Gleichungssystem aufgestellt und mit zwei numerischen Verfahren gelöst:

- Newton-Verfahren
- Broyden-Verfahren

Für verschiedene Startwerte vergleicht das Programm unter anderem die Anzahl der Iterationen, die Laufzeiten, die Residualnormen und die Gültigkeit der berechneten Schnittpunkte. Außerdem wird eine Visualisierung der Bézier-Fläche, des Strahls und einer ausgewählten Lösung erstellt.

## 2. Voraussetzungen

Für die Ausführung werden benötigt:

- Python 3
- NumPy
- Matplotlib

Das Projekt verwendet zusätzlich eigene Python-Module, die im Projektordner enthalten sind.

## 3. Installation

### Schritt 1: Python installieren

Installieren Sie Python von der offiziellen Website:

https://www.python.org/downloads/

Das Projekt wurde mit Python 3 entwickelt. Eine konkrete Python-Version sollte verwendet werden, sofern sie mit den installierten Bibliotheken kompatibel ist.

### Schritt 2: Projektordner öffnen

Entpacken Sie die ZIP-Datei. Öffnen Sie anschließend ein Terminal im Projektordner, in dem sich die Datei `Main.py` befindet.

### Schritt 3: Benötigte Bibliotheken installieren

Installieren Sie die benötigten Bibliotheken mit folgendem Befehl:

## bash
python -m pip install -r requirements.txt


Falls der Befehl `python` auf Ihrem System nicht verfügbar ist, können Sie unter Windows stattdessen Folgendes versuchen:

## powershell
py -m pip install -r requirements.txt


## 4. Ausführung des Programms

Führen Sie im Projektordner folgenden Befehl aus:

## bash
python Main.py

Das Programm führt die Berechnungen mit dem Newton- und dem Broyden-Verfahren durch und gibt die Ergebnisse im Terminal aus. Anschließend wird eine Visualisierung angezeigt. Falls die Programmausführung auf das Schließen des Grafikfensters wartet, schließen Sie das Fenster, um die Ausführung abzuschließen.

## 5. Aufbau des Projekts

- `Main.py` – Haupteinstiegspunkt. Legt die Bézier-Fläche, den Strahl und die Startwerte fest, führt die Lösungsverfahren aus, wertet die Ergebnisse aus und ruft die Visualisierung auf.
- `bezier_surface.py` – Implementiert die Bézier-Fläche und deren Auswertung.
- `ray.py` – Beschreibt den Strahl und berechnet Punkte entlang des Strahls.
- `equation_system.py` – Definiert das nichtlineare Gleichungssystem für den Schnittpunkt zwischen Strahl und Bézier-Fläche.
- `jacobian.py` – Berechnet die Jacobi-Matrix.
- `newton_solver.py` – Implementiert das Newton-Verfahren.
- `broyden_solver.py` – Implementiert das Broyden-Verfahren.
- `visualization.py` – Erstellt die Visualisierung der Bézier-Fläche, des Strahls und der ausgewählten Lösung.
- `testcase2.png` – Im Projekt enthaltene Bilddatei.
- `requirements.txt` – Liste der benötigten externen Python-Bibliotheken.

## 6. Hinweise

- Führen Sie `Main.py` aus dem Projektordner aus, damit die lokalen Module korrekt importiert werden können.
- Der verwendete Strahl und die Startwerte sind in `Main.py` festgelegt. Weitere dort auskommentierte Testkonfigurationen können bei Bedarf aktiviert werden.
- Die Laufzeitmessungen werden für jedes Lösungsverfahren und jeden Startwert 1.000-mal wiederholt. Daher kann die Ausführung etwas Zeit in Anspruch nehmen.
