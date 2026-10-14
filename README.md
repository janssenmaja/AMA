# Ray Tracing auf Freiformflächen: Vergleich des Newton- und des Broyden-Verfahrens

## 1. Projektbeschreibung

Dieses Projekt berechnet Schnittpunkte zwischen einem Strahl und einer bikubischen Bézier-Fläche. Dazu wird ein nichtlineares Gleichungssystem aufgestellt und mit zwei numerischen Verfahren gelöst:

- Newton-Verfahren
- Broyden-Verfahren

Für verschiedene Startwerte vergleicht das Programm unter anderem die Anzahl der Iterationen, die Laufzeiten, die Residualnormen und die Gültigkeit der berechneten Schnittpunkte. Außerdem wird eine Visualisierung der Bézier-Fläche, des Strahls und einer ausgewählten Lösung erstellt.

## 2. Voraussetzungen

- Anaconda oder Miniconda
- Python 3.10 (Das Projekt wurde mit Python 3.9 und Python 3.10 getestet)
- Externe Bibliotheken: NumPy und Matplotlib.

Die benötigten Versionen und Bibliotheken sind in `environment.yml` festgelegt. Alle übrigen Module sind eigene Python-Dateien im Projektordner.

## 3. Installation
### Schritt 1: Miniconda installieren | falls bereits installiert, diesen Schritt einfach überspringen

Miniconda stellt Conda zur Verfügung, mit dem eine separate Python-Umgebung für das Projekt erstellt und verwaltet werden kann.

Öffnen Sie die offizielle Installationsseite:

https://www.anaconda.com/download/success?reg=skipped


Laden Sie den grafischen Installer (Graphical Installer) für Windows oder Mac 64-Bit herunter und führen Sie die Installation mit den empfohlenen Standardeinstellungen durch.

Öffnen Sie anschließend über das Windows-Startmenü den Miniconda Prompt oder Anaconda Prompt.

Überprüfen Sie die Installation mit folgendem Befehl:

```bash
conda --version
```
Wenn eine Versionsnummer angezeigt wird, ist Conda verfügbar.


### Schritt 2: Terminal im Projektordner öffnen

Öffnen Sie den Miniconda bzw. Anaconda Prompt oder einen anderen Terminal und wechseln Sie in den Projektordner, also den Ordner, in dem sich diese README sowie `Main.py` und `environment.yml` befinden. Beispiel:

Windows:

```bash
cd "C:\Pfad\zum\Projektordner"
```

MacOS:

```bash
cd "/Pfad/zum/Projektordner"  
```


Ersetzen Sie den Beispielpfad durch den tatsächlichen Speicherort Ihres Projektordners. Führen Sie die folgenden Befehle in diesem Ordner aus.

### Schritt 3: Conda-Umgebung einrichten

```bash
conda env create -f environment.yml
conda activate ama-newton-broyden
```

Der erste Befehl legt die Umgebung `ama-newton-broyden` mit Python 3.10, NumPy und Matplotlib an. Er wird nur einmal benötigt. Der zweite Befehl aktiviert die Umgebung. Danach steht `(ama-newton-broyden)` vor der Eingabezeile.


## 4. Ausführung des Programms

### Über die Kommandozeile

Führen Sie in der aktivierten Umgebung im Projektordner folgenden Befehl aus:

```bash
python Main.py
```

(Falls `python` unter macOS/Linux nicht gefunden wird, verwenden Sie `python3 Main.py`.)


### Was passiert beim Ausführen?

Das Programm führt die Berechnungen mit dem Newton- und dem Broyden-Verfahren durch und gibt die Ergebnisse im Terminal aus.

**Hinweis zur Terminal-Ausgabe:** Während der Laufzeitmessung erscheinen sehr viele Zeilen der Form `Iteration 1: x = [...]` (insgesamt mehrere tausend). Das ist normal und kein Fehler: Die Solver geben jeden Iterationsschritt aus, und die Messung wird 1.000-mal wiederholt. Die zusammengefasste Ergebnistabelle steht **ganz am Ende der Ausgabe** unter der Überschrift `ERGEBNISSE`.

Die Spalten der Ergebnistabelle bedeuten:

| Spalte | Bedeutung |
|---|---|
| `Startwert` | Startschätzung $(u_0, v_0, t_0)$ |
| `Newton It.` / `Broyden It.` | Anzahl der Iterationen bis zur Konvergenz ($\lVert F \rVert < 10^{-6}$, max. 20) |
| `Newton Zeit` / `Broyden Zeit` | Mittlere Laufzeit eines vollständigen Solver-Aufrufs in **Millisekunden**, gemittelt über 1.000 Wiederholungen |
| `Newton Res.` / `Broyden Res.` | Residualnorm $\lVert F(u, v, t) \rVert$ an der berechneten Lösung |
| `Newton` / `Broyden` | `gültig`, wenn $u, v \in [0, 1]$ und $t \ge 0$, sonst `ungültig` |

Die Laufzeiten hängen vom Rechner ab und weichen daher von den Werten im Bericht ab.

Anschließend öffnet sich (bei Ausführung über die Kommandozeile) ein Grafikfenster mit der Bézier-Fläche, dem Kontrollnetz, dem Strahl und, sofern vorhanden, dem ersten gültigen Schnittpunkt des Newton-Verfahrens (orangefarbener Stern). Das Fenster lässt sich mit der Maus drehen. Das Programm ist erst beendet, wenn Sie dieses Fenster schließen. In Test Case 3 gibt es keinen gültigen Schnittpunkt, deshalb wird dort kein Stern eingezeichnet.

## 5. Aufbau des Projekts

- `Main.py` – Haupteinstiegspunkt. Legt die Bézier-Fläche, den Strahl und die Startwerte fest, führt die Lösungsverfahren aus, wertet die Ergebnisse aus und ruft die Visualisierung auf.
- `bezier_surface.py` – Implementiert die Bézier-Fläche und deren Auswertung.
- `ray.py` – Beschreibt den Strahl und berechnet Punkte entlang des Strahls.
- `equation_system.py` – Definiert das nichtlineare Gleichungssystem für den Schnittpunkt zwischen Strahl und Bézier-Fläche.
- `jacobian.py` – Berechnet die Jacobi-Matrix.
- `newton_solver.py` – Implementiert das Newton-Verfahren.
- `broyden_solver.py` – Implementiert das Broyden-Verfahren.
- `visualization.py` – Erstellt die Visualisierung der Bézier-Fläche, des Strahls und der ausgewählten Lösung.
- `testcase2.png` – Beispielausgabe der Visualisierung für Test Case 2 (schräger Strahl): Bézier-Fläche mit Kontrollnetz, Strahl und berechnetem Schnittpunkt.
- `environment.yml` – Definiert die Conda-Umgebung mit Python 3.10 sowie den benötigten Bibliotheken NumPy und Matplotlib.

## 6. Hinweise

- Führen Sie `Main.py` aus dem Projektordner aus, damit die lokalen Module korrekt importiert werden können.
- Der verwendete Strahl und die Startwerte sind in `Main.py` festgelegt. Standardmäßig ist **Test Case 2** (schräger Strahl) aktiv.
- Um einen anderen Testfall auszuführen, kommentieren Sie in `Main.py` die aktive `ray = ...`-Zeile aus und entfernen das `#` vor der gewünschten Zeile:

  ```python
  #ray = Ray([0.7, 1.2, -1.2], [0, 0, 1])           # Test Case 1: senkrechter Strahl
  ray = Ray([0.4, 1.0, -0.6875], [0.3, 0, 1])       # Test Case 2: schräger Strahl
  #ray = Ray([0.35, 0.6, 0.8], [0.2, 0, -0.1])      # Test Case 3: kein gültiger Schnittpunkt
  ```

  Es darf immer nur genau eine `ray = ...`-Zeile aktiv sein. In Test Case 3 konvergieren die Verfahren zwar numerisch, die Lösung liegt aber außerhalb des gültigen Parameterbereichs und wird daher als „ungültig“ ausgegeben. Das ist so beabsichtigt.
- Die Laufzeitmessungen werden für jedes Lösungsverfahren und jeden Startwert 1.000-mal wiederholt. Ein Programmdurchlauf dauert daher etwa 10–20 Sekunden (abhängig vom Rechner und vom Testfall).
