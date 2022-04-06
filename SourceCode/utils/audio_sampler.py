from SourceCode.utils.audio_compiler import AudioCompiler


import pydub

class AudioSampler:

    def __init__(self) -> None:
        self.audio_compiler = AudioCompiler()
    
    def check_samples_exist(self, track) -> None:
        #ToDo
        pass

    def load_track(self, track_path) -> None:
        #ToDo
        pass

    def disassemble_track(self, track, disassembling_strategy, sampling_size) -> None:
        sample_list = []
        #ToDo Disassemble Track
        for sample in sample_list:
            self.save_sample(sample)
        pass

    def save_sample(self, sample) -> None:
        #ToDo
        pass

    def disassemble_tracks(self, disassembling_strategy, sampling_size, track_selection_list) -> None:
        for track_path in track_selection_list:
            is_existing = self.check_samples_exist(track_path)

            if is_existing == False:
                track_loaded = self.load_track(track_path)

                self.disassemble_track(track_loaded, disassembling_strategy, sampling_size)

        print('Disassembling finished.')
 

    def concatenate_samples(self) -> None:
        #ToDo Challenge 2
        pass    

    def save_track(self) -> None:
        #ToDo Cahllenge 2
        pass


        
    