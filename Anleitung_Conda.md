# Ray Tracing auf Freiformflächen: Vergleich des Newton- und des Broyden-Verfahrens

## 1. Projektbeschreibung

Dieses Projekt berechnet Schnittpunkte zwischen einem Strahl und einer bikubischen Bézier-Fläche. Dazu wird ein nichtlineares Gleichungssystem aufgestellt und mit zwei numerischen Verfahren gelöst:

- Newton-Verfahren
- Broyden-Verfahren

Für verschiedene Startwerte vergleicht das Programm die Anzahl der Iterationen, die Laufzeiten, die Residualnormen und die Gültigkeit der berechneten Schnittpunkte. Zusätzlich wird eine Visualisierung der Bézier-Fläche, des Strahls und einer ausgewählten Lösung erstellt.

## 2. Voraussetzungen

Für die Ausführung werden benötigt:

- Miniconda zur Verwaltung der Python-Umgebung
- Python 3.10 innerhalb der Conda-Umgebung
- NumPy
- Matplotlib

Das Projekt verwendet zusätzlich eigene Python-Module, die im Projektordner enthalten sind. Diese müssen nicht separat installiert werden.

## 3. Installation

### Schritt 1: Miniconda herunterladen

Miniconda stellt Conda zur Verfügung, mit dem eine separate Python-Umgebung für das Projekt erstellt und verwaltet werden kann.

Öffnen Sie die offizielle Installationsseite:

https://www.anaconda.com/docs/getting-started/installation

Wählen Sie Miniconda und anschließend den grafischen Installer (*Graphical installer*) für Windows 64-Bit aus.

Laden Sie die Installationsdatei herunter und starten Sie sie.

### Schritt 2: Miniconda installieren

Folgen Sie den Anweisungen des Installationsprogramms.

Bei den erweiterten Installationsoptionen können Sie folgende Einstellungen verwenden:

- **Create shortcuts:** aktiviert lassen.
- **Add installation to my PATH environment variable:** nicht aktivieren.
- **Register Miniconda3 as my default Python:** nicht aktivieren.
- **Clear the package cache upon completion:** nicht aktivieren.

Klicken Sie anschließend auf „Install“ und warten Sie, bis die Installation abgeschlossen ist.

### Schritt 3: Anaconda Prompt öffnen

Öffnen Sie das Windows-Startmenü und suchen Sie nach „Anaconda Prompt“ oder „Miniconda Prompt“.

Starten Sie das Programm. Es öffnet sich ein Terminal, in das die folgenden Befehle eingegeben werden.

Überprüfen Sie zunächst, ob Conda installiert wurde:

```bash
conda --version
```

Wenn eine Versionsnummer ausgegeben wird, ist Conda verfügbar.

### Schritt 4: Projekt von GitHub herunterladen

Öffnen Sie die GitHub-Seite des Projekts:

https://github.com/janssenmaja/AMA

Klicken Sie auf den grünen Button „Code“ und wählen Sie „Download ZIP“.

Entpacken Sie die heruntergeladene ZIP-Datei. Es entsteht ein Ordner mit dem Namen `AMA-main`.

Öffnen Sie diesen Ordner im Datei-Explorer und überprüfen Sie, ob sich darin die Datei `Main.py` befindet.

### Schritt 5: In den Projektordner wechseln

Wechseln Sie im Anaconda Prompt in den Ordner, in dem sich die Datei `Main.py` befindet.

Wenn Sie den Projektordner beispielsweise im Download-Ordner entpackt haben, lautet der Befehl:

```powershell
cd "$HOME\Downloads\AMA-main"
```

Falls sich der Ordner an einer anderen Stelle befindet, muss der Pfad entsprechend angepasst werden.

Alternativ können Sie den Ordner im Datei-Explorer öffnen, den vollständigen Pfad aus der Adressleiste kopieren und im Terminal nach `cd` einfügen. Setzen Sie den Pfad in Anführungszeichen, wenn er Leerzeichen enthält.

Überprüfen Sie anschließend den Ordnerinhalt:

```powershell
dir
```

In der Dateiliste sollte `Main.py` erscheinen.

### Schritt 6: Conda-Umgebung erstellen

Erstellen Sie eine separate Conda-Umgebung mit Python 3.10 und den benötigten Bibliotheken:

```bash
conda create -n raytracing python=3.10 numpy matplotlib
```

Conda zeigt gegebenenfalls Nutzungsbedingungen (*Terms of Service*) an. Lesen Sie diese und akzeptieren Sie sie mit `a`, sofern Sie zustimmen. Drücken Sie anschließend Enter.

Wenn die Abfrage `Proceed ([y]/n)?` erscheint, geben Sie `y` ein und drücken Sie Enter.

Conda lädt nun Python und die benötigten Bibliotheken herunter und installiert sie. Dieser Vorgang kann einige Minuten dauern.

Nach erfolgreicher Installation erscheint eine Meldung, die unter anderem auf den Befehl `conda activate raytracing` hinweist.

### Schritt 7: Conda-Umgebung aktivieren

Aktivieren Sie die neu erstellte Umgebung:

```bash
conda activate raytracing
```

Vor dem Pfad in der Eingabezeile sollte nun `(raytracing)` stehen.

Beispiel:

```text
(raytracing) C:\Users\Benutzername>
```

Damit ist die separate Python-Umgebung aktiv. Alle weiteren Befehle müssen innerhalb dieser Umgebung ausgeführt werden.

### Schritt 8: Installation überprüfen

Überprüfen Sie die installierte Python-Version:

```bash
python --version
```

Es sollte Python 3.10 angezeigt werden.

Prüfen Sie anschließend, ob NumPy und Matplotlib importiert werden können:

```bash
python -c "import numpy, matplotlib; print('Bibliotheken erfolgreich importiert')"
```

Wenn die Meldung „Bibliotheken erfolgreich importiert“ erscheint, ist die Umgebung korrekt eingerichtet.

## 4. Ausführung des Programms

Stellen Sie sicher, dass die Conda-Umgebung `raytracing` aktiviert ist und sich das Terminal im Projektordner befindet, in dem `Main.py` liegt.

Starten Sie das Programm mit folgendem Befehl:

```bash
python Main.py
```

Das Programm führt die Berechnungen mit dem Newton- und dem Broyden-Verfahren durch und gibt die Ergebnisse im Terminal aus.




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
