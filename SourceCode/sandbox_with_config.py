from concurrent.futures import process
from dis import disassemble
import configparser
from utils.audio_sampler import AudioSampler


class Sandbox:

    def __init__(self) -> None:
        self.audio_sampler = AudioSampler()
        self.path = 'C:/Users/elina/VisualStudioCodeProjects/TechnologyLab2022/'
        print("Welcome to the Lounge Music Generator!")
        print("Please fill in the configuration.yaml file and save it.")
        proceed = 'y'
        # proceed = input("Do you want to start sampling? [y/n] ")
        if proceed == 'y':
            self.start_sampling()
        else:
            pass
        

    def start_sampling(self):
        ds, ss, tsl = self.read_ini(self.path+'SourceCode/config.ini')
        self.generate_samples(ds, ss, tsl)
    

    def read_ini(self, file_path):
        config = configparser.ConfigParser()
        config.read(file_path)

        # Todo: prevent wrong input
        disassembling_strategy = config['MUSIC_GENERATOR']['DISASSEMBLING_STRATEGY']
        sampling_size = int(config['MUSIC_GENERATOR']['SAMPLING_SIZE'])
        track_selection_list = config['MUSIC_GENERATOR']['TRACK_SELECTION_LIST'].replace(" ","").split(',') 

        return disassembling_strategy, sampling_size, track_selection_list   


    def generate_samples(self, disassembling_strategy, sampling_size, track_selection_list)  -> None:

        self.audio_sampler.disassemble_tracks(disassembling_strategy, sampling_size, track_selection_list)


if __name__ == "__main__":
    sandbox = Sandbox()