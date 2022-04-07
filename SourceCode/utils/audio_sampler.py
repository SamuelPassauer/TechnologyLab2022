#from utils.audio_compiler import AudioCompiler


import pydub
from pydub import AudioSegment
import os
import random

class AudioSampler:

    def __init__(self) -> None:
        #self.audio_compiler = AudioCompiler()
        self.path = 'C:/Users/elina/VisualStudioCodeProjects/TechnologyLab2022/'


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

        print('[INFO] Disassembling finished.')
    

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
        print("[INFO] Disassembling starts now.")

        if disassembling_strategy == 'equidistant':
            sample_list = self.disassemble_equidistant(track, sampling_size)

        elif disassembling_strategy == 'stochastic':
            sample_list = self.disassemble_stochastic(track, sampling_size)

        try:
            os.makedirs(self.path+samples_folder)
        except OSError:
            print("[ERROR] Creation of the directory {} failed".format(samples_folder))
        
        #Todo auslagern
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
        
    def disassemble_equidistant(self, track, sampling_size) -> None:
        sample_list = []
        track_length = track.duration_seconds
        sample_length = track_length/sampling_size * 1000
        start_cut = 0

        for cut in range(sampling_size):
            end_cut = start_cut + sample_length
            sample = track[start_cut : end_cut]
            sample_list.append(sample)
            start_cut = end_cut
        
        return sample_list


    def disassemble_stochastic(self, track, sampling_size) -> None:
        # Todo: bei 10 kommen nur 9 sinnvolle raus
        # Todo: auslagern

        # min und max range bestimmen
        sample_list = []
        track_length = track.duration_seconds
        mean_sample_length = track_length/sampling_size
        min_range = round(mean_sample_length*0.5)
        max_range = round(mean_sample_length*1.5)

        # zahlen random erzeugen
        random_numbers = []
        for x in range(sampling_size):
            rand_num = random.randint(min_range, max_range)
            print('Rand Num ', rand_num)
            random_numbers.append(rand_num)

        # umrechnen in prozent und sample länge
        random_numbers_sum = sum(random_numbers)
        one_percent = 100/random_numbers_sum
        sample_length = []
        for num in random_numbers:
            sample_lenth = num*one_percent * 1000
            sample_length.append(sample_lenth)

        print()
        # cuten
        cut_start = 0
        for length in sample_length:
            print('Length :',length)
            cut_end = cut_start + length
            sample = track[cut_start:cut_end]
            sample_list.append(sample)
            cut_start+= length

        return sample_list


    def save_sample(self, sample) -> None:
        # ToDo Metadaten als csv
        pass


    def concatenate_samples(self) -> None:
        #ToDo Challenge 2
        pass    


    def save_track(self) -> None:
        #ToDo Cahllenge 2
        pass


        
    