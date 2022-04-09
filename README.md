# Technology Lab im Sommersemester 2022
In diesem Repository findet sich das **Lounge Music Generator** Projekt der Gruppe 1. Während des Verlaufs des Sommersemesters entsteht hier eine Sandbox, welche dazu dienen soll herauszufinden, ob es möglich ist mithilfe eines Deep Learning Ansatz aus kleinen Samples, die aus ganzen Tracks geschnitten werden, hörbare Musik zu resampeln.

## Forschungsansatz
Das Projekt möchte sich einer Problemlösung über die folgenden Forschungsfragen annähern:
  1. Lässt sich hörbare Musik erzeugen?
  2. Reicht das stochaistische Sampling? Wie lange ist eine optimale Sampledauer?
  3. Wie ähnlich müssen sich die Ursprungstracks bezüglich Stimmung Genre, etc sein?
  4. Müssen Metdaten wie Lautstärke, Tempo, Spektrum, etc mit einbezogen werden?

Diese Fragen sind im Projektverlauf zu beantworten und stellen somit den Projektrahmen auf. Die Entwicklung des Zielsystems und damit die sukzessive Beantwortung der Forschungsfragen und Abarbeitung der Problemstellung erfolgt in Rahmen von Challenges. Jede Challenge stellt dabei einen Meilenstein des Projekts dar. 

### Challenge 1
Die erste Challenge beschäftigt sich mit den Trainigsdaten für das System. Es soll eine geeignete Infrastruktur bereitgestellt werden, um Tracks in Samples zu zerlegen und so einen synthetischen Trainingsdatensatz herzustellen. Die Daten müssen zusätzlich in eine Form überführt werden, um sie einem Neuronalen netz zugänglich zu machen.

### Challenge 2
In dieser Challenge geht es darum, dass ein ANN trainiert wird, welches abschließend in der Lage sein soll, Samples wieder zu einem Track zusammenzufügen, welche dem ANN bekannt sind.

### Challenge 3
In der letzten Challenge soll versucht werden, aufbauend auf der vorherigen Challenge, ein Resampling von bisher unbekannten Samples zu hörbarer Musik durch das ANN zu ermöglichen.  

Somit wird durch das strukturierte Vorgehen, eine gezielte wissenschaftliche Annäherung an das Problemfeld ermöglicht. Das dazu notwendige theoretische Hintergrundwissen findet sich im [Wiki](https://github.com/JenniferHammen/TechnologyLab2022/wiki) dieses GitHub Repositorys.

## Entwicklungsansatz
Die Entwicklung des Zielsystems orientiert sich stark an den im Forschungsansatz vorgestellten Challenges. Zusätzlich erfolgt jedoch bereits in den früheren Phasen ein Vorausplanen der notwendigen Infrastruktur der Sandbox, um dann eine gezielte Entwicklung und eine Konzentration auf die forschenden Aspekte der Erstellung des Zielsystems zu ermöglichen. Daher ergeben sich in den Challenges die folgenden Meilensteine für die Implementation und Planung.

### Meilenstein 1
- Technische Implementierung von Challenge 1
- Systementwurf für Challenge 2 & 3
- Struktur der Daten

### Meilenstein 2
- Prototyp für Challenge 2

### Meilenstein 3
- Prototyp für Challenge 3

*Anmerkung: Der im Rahmen von Meilenstein 1 angefertigte Systementwurf, bestehend aus Anforderungsanalyse, User Story mit Use Case Diagrammen, Sequenzflussdiagramm und Klassendiagramm sowie eine Beschreibung der Daten- und Ordnerstruktur der Trainingsdaten befindet sich im Ordner [Dokumentation](https://github.com/JenniferHammen/TechnologyLab2022/tree/main/Dokumentation).*

## Installations- und Bedienungsanleitung
Informationen zu Betrieb und Installation des Programmcodes finden sich im Ordner Dokumentation im File [Installations- und Bedienungsanleitung](https://github.com/JenniferHammen/TechnologyLab2022/blob/main/Dokumentation/Installations-%20und%20Bedienungsanleitung.md).

## Coaching
Während des Projekts finden Coachings durch die Betreuenden Professoren statt. Die dabei entstehenden Dokumentationen werden ebenfalls im Repository unter [Protokolle](https://github.com/JenniferHammen/TechnologyLab2022/tree/main/Protokolle) abgelegt.

