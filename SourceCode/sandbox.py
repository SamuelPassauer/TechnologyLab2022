

from utils.audio_sampler import AudioSampler


class Sandbox:

    def __init__(self) -> None:
        self.audio_sampler = AudioSampler()
        print("Welcome to the Lounge Music Generator!")
        print()
        print("1: Generate music samples")
        print()
        self.start()


    def start(self):
        action = input("Please select your desired action from the list above: ")

        if action == '1':
            self.generate_samples()

        elif action == 'exit':
            print("Execution interrupted.")
            return

        else: 
            print('This input is not available. Try again!')
            self.start()


    def generate_samples(self)  -> None:
        print("You selected sample generation.")
        print()
        #ToDo Prevent wrong input
        disassembling_strategy_selection = int(input("Please type in 1 for stochastic and 2 for equidistant dissasembling strategy: "))
        print()
        disassembling_strategy_list = {1:"stochastic", 2:"equidistant"}
        disassembling_strategy = disassembling_strategy_list[disassembling_strategy_selection]
        
        #ToDo Prevent wrong input
        sampling_size = int(input("Please type in the sampling size: "))
        print()

        track_selection = input("Please type in the track you want to disassemble: ")
        print()
        track_selection_list = []

        while track_selection != "exit":
            track_selection_list.append(track_selection)
            track_selection = input("Another track to add? If yes, type in your track, if no type exit. ")

        self.audio_sampler.disassemble_tracks(disassembling_strategy, sampling_size, track_selection_list)


if __name__ == "__main__":
    sandbox = Sandbox()