from run_sarmata import print_results, get_results
from record_to_wav import record
import os.path
from run_trybun import play_tts_wav_file

play_tts_wav_file("Witaj! Czym mogę służyć?", "init.wav")


filename = "request.wav"
record(filename)

if __name__ == '__main__':
    while True:
        if os.path.isfile(filename):
            break

    wave_file = filename
    grammar_file = "grammars/atm.abnf"
    print_results(get_results(wave_file=wave_file, grammar_file=grammar_file))

