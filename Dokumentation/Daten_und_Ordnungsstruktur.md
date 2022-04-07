# Daten und Ordnerstruktur für Tracks und Samples

Im folgenden soll erläutert werden, wie die im Projekt generierten Trainings- und Testdaten abgelegt werden, wie die Metadaten gesichert werden und in welcher Struktur die Daten vorzufinden sind.

## Speicherlocation für Tracks und Samples
Da die mp3 Datein (Tracks) nicht direkt in Github Ordnern gespeichert werden können, muss hierfür ein Workaround gefunden werden.
Die mp3 Datein werden demnach in einem privaten One Drive Ordner gespeichert und die Samples in dem Repo. Die Ordnerstruktur und Namens Konventionen sind so gewählt, dass die Samples eindeutig ja nach Disassembling Strategie und Sampling Size den Tracks zugeordnet werden können.

## Pfadstruktur
<pre><code>
tracks/interpret/track_name/disassembling_strategy/sampling_size/sample_name.mp3
</code></pre>

Der Sample Name setzt sich dabei aus Interpret, Tracknamen, Disassembling Strategie, Sampling Size und der Position des Samples zusammen.
Die Disassembling Strategie ist entweder stochastisch oder äquidistant. Die Sampling Size bestimmt in wie viele Samples ein Track zerlegt wird.   

**Beispiel:**
<pre><code>
tracks/SoundBehaviour/SubliminalLove/stochastic/samplingsize_10/SoundBehaviour_SubliminalLove_s_10_0001.mp3
</code></pre>

## Ordnerstruktur:

**Beispiel:**
<pre><code>
tracks
  SoundBehaviour
    SubliminalLove
      stochastic
        samplingsize_10
          SoundBehaviour_SubliminalLove_s_10_0001
          SoundBehaviour_SubliminalLove_s_10_0002
          SoundBehaviour_SubliminalLove_s_10_0003
          ...
        samplingsize_25
          SoundBehaviour_SubliminalLove_s_25_0001
          SoundBehaviour_SubliminalLove_s_25_0002
          SoundBehaviour_SubliminalLove_s_25_0003
          ...
      equidistant
        samplingsize_15
          SoundBehaviour_SubliminalLove_e_15_0001
          SoundBehaviour_SubliminalLove_e_15_0002
          SoundBehaviour_SubliminalLove_e_15_0003
          ...
    
</code></pre>

Die Samples und deren zugehörige Tensoren werden beide mit dem gleichen Namen (aber unterschiedliche Dateiendung) in demselben Ordner abgelegt.

## Datenstruktur von Metadaten
Um eine gute Übersicht über die verfügbaren Samples zu behalten und die Metadaten zu speichern, um diese für eine etwaige spätere Verwendung vorzuhalten, werden diese Informationen in einem Metdaten-File gespeichert. Das File wird im CSV-Format abgelegt. Sollte es zu Kapazitätsprobleme kommen, so kann eine einfache Überführung der strukturierten Informationen in eine Datenbank erfolgen.

Das CSV-File beeinhaltet die im folgenden tabellarisch dargestellten Informationen zu einem Sample. Die Daten sind zwar in drei Tabellen dargestellt, bilden jedoch im CSV-File eine Gesamtabelle. In der ersten Teiltabelle sind der Speichername des Samples sowie dessen Speicherpfad zu erkennen. Dies ermöglicht ein einfaches Laden von Tensoren und Samples in den späteren Challenges des Projekts.

samplename | path 
-------- | -------- 
SoundBehaviour_SubliminalLove_s_10_0001 | tracks/SoundBehaviour/SubliminalLove/stochastic/samplingsize_10/ 
... | ... | ...  | ...  | ...  | ...  | ... | ... | ... | ...

In der nächsten Teiltabelle befinden sich Informationen zum Track aus dem das Sample stammt, wie dessen Name und die Songdauer. Zusätzlich werden Informationen aus der Songanalyse gespeichert wie die Lautstärke, das Spektrum und das Tempo des Stücks.

| track | length | volume | spectrum | tempo 
| --------  | -------- | --------  | -------- | --------
| SoundBehaviour_SubliminalLove | 2:50 | 60 | 30 | 124 
| ...  | ...  | ...  | ...  | ... 

In der letzten Teiltabelle sind Informationen über die Zerlegung des Tracks in das Sample zu finden. Hier findet sich die Position des Samples im Track, die Strategie unter welcher die Zerlegung stattgefunden hat, die dabei gewählte Sampling-Größe, sowie die Information ob das Sample zu finalen Training genutzt wurde.

| position | disassembling_strategy | sampling_size | used_for_training
| -------- | --------  | -------- | --------
| 1 | s | 10 | False
| ... | ... | ...

*Anmerkung: Die Tabelle der Metadaten befindet sich aktuell nicht in der 3. Normalform. Sollte dies notwendig werden oder im Produktivsystem gefordert sein, ist das Nachführen der Normalisierung jederzeit möglich.*

## Datenstruktur von Samples 
ToDo

## Datenstruktur von Tensoren
ToDo
