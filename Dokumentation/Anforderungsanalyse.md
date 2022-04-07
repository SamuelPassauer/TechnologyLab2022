# Anforderungsanalyse

Die folgende Beschreibung soll einen Überblick über die Anforderungen liefern, welche an den Funktionsalitätsumfang der Dienste, die das Zielsystem abbilden soll, gestellt werden und unter welchen Gegebenheiten dieses Zielsystem entwickelt werden und betrieben werden soll.

### Zielsystem
1. Das Zielsystem soll das Erlernen von zueinander passenden Musik-Samples ermöglichen.

2. Das Zielsystem verfügt über eine **Audio Komponente**.
    1. Die Komponente kann mit Audio-Files (Tracks) im mp3 Format umgehen.
    2. Die Tracks können durch die Komponente nach einer wählbaren Strategie in Samples (Chunks des Tracks) zerlegt werden.
    3. Für die entstehenden Samples sind geeignete Namen zu verwenden
    4. Für die entstehenden Samples sind ggf. weitere Metdadaten zu verwalten.
    5. Die Komponente kann Samples zu Tracks konkatenieren.
    6. Die Komponente kann Tracks laden.
    7. Die Komponente kann Tracks speichern.
    8. Die Komponente kann Tracks hinsichlich der Audioeigenschaften geeignet analysieren.

3. Das Zielsystem verfügt über eine **Compiler Komponente**.
    1. Die Komponente kann Samples in für die Machine Learning Komponente geeignete Form übersetzen (Tensoren).
    2. Die Umwandlung muss in eine Zahlenform erfolgen.


4. Das Zielsystem verfügt über eine **Machine Learning Komponente**.
    1. Die Komponente verfügt über ein geeignetes Neuronales Netz, welches die Sequenzen von Musik wahrnimmt und über eine geeignete Reihenfolge von Samples entscheiden kann.
    2. Das Neuronale Netz bewertet dabei im Kern ob zwei Samples konkateniert werden können. 
    3. Das Neuronale Netz wird mit Tensorflow umgesetzt.
    4. Für das Lernen sind Ansätze wie LSTM, Recurrent Neural Networks (RNN), Attention etc. in Betracht zu ziehen.
    5. Es können Ansätze wie Reinforcement Learning eingesetzt werden.
    6. Die Komponente bezieht weitere Eigenschaften des Audiomaterials (Lautstärke, Tempo, Spektrum, etc.) ein.    
    7. Die Komponente ermöglicht durch ihre Funktionalität das Erstellen neuer Tracks.
    8. Die Komponente meldet an die Audio Komponente ob zwei Samples konkateniert werden können.

5. Für Training, Test und Betrieb des Systems werden geeignete **Daten** bereitgestellt.

6. Das Zielsystem soll eine Sandbox für Experimente zur Beantwortung der Forschungsfragen bereitstellen.

### Entwicklung und Betrieb
1. Alle Entwicklungsschritte werden mithilfe von **GitHub** dokumentiert.
2. Alle Aspekte der Entwicklung, welche keinen Source Code darstellen, sind über **Mark-Down Files** zu dokumentieren.
3. Zusätzliche Bilder, Illustrationen und Schaubilder sind als separate **Dateien** bereitzustellen und in Mark-Down Files einzubinden.
4. Die Textuelle Beschreibung umfasst auch eine **Installations- und Bedienungsanleitung**.
5. Software-Strukturen werden mittels der **Unified Modeling Language** (UML) oder / und einer deklarativen Beschreibung mit **User Stories** dokumentiert.
6. UML-Diagramme sind mittels **Star-UML** zu erstellen.
7. Zusätzlich verwendete **APIs** werden hinsichtlich von Verfügbarkeit (lizenzrechtlich und wirtschaftlich) analysiert und geeignet dokumentiert.
8. Es erfolgt eine ausreichende Dokumentation des Source Codes.
9. Die Entwicklung erfolgt in **Python** unter dem PEP 8 Standard.
10. Auch bei verwendeten Diensten sind Python APIs zu nutzen, sofern verfügbar.
11. Wenn erforderlich müssen Web Services nach dem **REST-Ansatz** integriert werden.
12. Die Entwicklung erfolgt über Schnittstellen, welche während des Entwicklungsverlaufs ausdefiniert werden.
