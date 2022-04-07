#from utils.audio_compiler import AudioCompiler


import pydub
from pydub import AudioSegment
import os

class AudioSampler:

    def __init__(self) -> None:
        #self.audio_compiler = AudioCompiler()
        self.path = 'C:/Users/elina/VisualStudioCodeProjects/TechnologyLab2022/'
    
    def check_samples_exist(self, samples_folder) -> None:
        if os.path.exists(self.path+samples_folder):
            is_existing = True
        else:
            is_existing = False

        return is_existing

    def load_track(self, track_path) -> None:
        track = AudioSegment.from_mp3(self.path + 'data/tracks/' + track_path)
        return track

    def disassemble_track(self, track, disassembling_strategy, sampling_size, samples_folder) -> None:
        sample_list = []
        track_length = track.duration_seconds

        if disassembling_strategy == 'equidistant':
            sample_length = track_length/sampling_size * 1000
            start_cut = 0

            for cut in range(sampling_size):
                end_cut = start_cut + sample_length
                sample = track[start_cut : end_cut]
                sample_list.append(sample)
                print('Cut for ', start_cut, ' done.')
                start_cut = end_cut

        elif disassembling_strategy == 'stochastic':
            # Todo
            pass

        try:
            os.makedirs(self.path+samples_folder)
        except OSError:
            print("[ERROR] Creation of the directory %s failed" %samples_folder)
        
        counter = 1
        for sample in sample_list:
            if len(str(counter)) == 1:
                position = '00'+str(counter)
            elif len(str(counter)) == 2:
                position = '0'+str(counter)
            elif len(str(counter)) == 3:
                position = str(counter)
            
            sample.export(self.path+samples_folder+'/sample_'+position+'.mp3',format="mp3")
            counter+=1
        

    def save_sample(self, sample) -> None:
        # ToDo
        pass

    def disassemble_tracks(self, disassembling_strategy, sampling_size, track_selection_list) -> None:
        for track_path in track_selection_list:
            track_interpret, track_name = track_path.split('_')
            samples_folder = 'data/samples/' + track_interpret + '/' + track_name[:-4] + '/' + disassembling_strategy + '/samplingsize_' + str(sampling_size)
            is_existing = self.check_samples_exist(samples_folder)

            if is_existing == False:
                track_loaded = self.load_track(track_path)
                self.disassemble_track(track_loaded, disassembling_strategy, sampling_size, samples_folder)
            else:
                print("[INFO] Samples for this track, disassembling stretegy and samplinz size already exist.")

        print('Disassembling finished.')
 

    def concatenate_samples(self) -> None:
        #ToDo Challenge 2
        pass    

    def save_track(self) -> None:
        #ToDo Cahllenge 2
        pass


        
    