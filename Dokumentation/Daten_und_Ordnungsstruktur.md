# Orderstruktur für Tracks und Samples

Da die mp3 Datein (Tracks) nicht direkt in Github Ordnern gespeichert werden können, muss hierfür ein Workaround gefunden werden.
Die mp3 Datein werden demnach in einem privaten One Drive Ordner gespeichert und die Samples in dem Repo. Die Ordnerstruktur und Namens Konventionen sind so gewählt, dass die Samples eindeutig ja nach Disassembling Strategie und Sampling Size den Tracks zugeordnet werden können   .


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
