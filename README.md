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

Das Projekt wurde mit Python 3.9 und 3.10 getestet. Jede Python-Version ab 3.8 sollte funktionieren.

### Schritt 2: Projektordner öffnen

Laden Sie das Projekt auf GitHub (https://github.com/janssenmaja/AMA) über den grünen Button **Code → Download ZIP** herunter und entpacken Sie die ZIP-Datei (der Ordner heißt dann `AMA-main`). Öffnen Sie anschließend ein Terminal im Projektordner, in dem sich die Datei `Main.py` befindet.

> **Hinweis zum Python-Befehl:** Je nach Betriebssystem heißt der Befehl unterschiedlich. Unter **macOS und Linux** verwenden Sie `python3`, unter **Windows** `python` oder `py`. In den folgenden Befehlen steht `python3`. Ersetzen Sie es unter Windows entsprechend.

### Schritt 3 (empfohlen): Virtuelle Umgebung anlegen

Auf neueren macOS- und Linux-Systemen kann `pip install` ohne virtuelle Umgebung mit der Meldung „externally-managed-environment“ abbrechen. Legen Sie deshalb im Projektordner eine virtuelle Umgebung an und aktivieren Sie sie:

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
py -m venv venv
venv\Scripts\activate
```

Nach der Aktivierung steht `(venv)` vor der Eingabezeile. Innerhalb der aktivierten Umgebung funktioniert auch unter macOS/Linux der Befehl `python`.

### Schritt 4: Benötigte Bibliotheken installieren

Installieren Sie die benötigten Bibliotheken mit folgendem Befehl:

```bash
python3 -m pip install -r requirements.txt
```

## 4. Ausführung des Programms

Führen Sie im Projektordner folgenden Befehl aus:

```bash
python3 Main.py
```

(Unter Windows: `python Main.py` bzw. `py Main.py`.)

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

Anschließend öffnet sich ein Grafikfenster mit der Bézier-Fläche, dem Kontrollnetz, dem Strahl und, sofern vorhanden, dem ersten gültigen Schnittpunkt des Newton-Verfahrens (orangefarbener Stern). Das Fenster lässt sich mit der Maus drehen. Das Programm ist erst beendet, wenn Sie dieses Fenster schließen. In Test Case 3 gibt es keinen gültigen Schnittpunkt, deshalb wird dort kein Stern eingezeichnet.

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
- `requirements.txt` – Liste der benötigten externen Python-Bibliotheken.

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
