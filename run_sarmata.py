#!/usr/bin/env python
# -*- coding: utf-8 -*-

from techmo_sarmata_pyclient.utils.wave_loader import load_wave
from techmo_sarmata_pyclient.service.sarmata_settings import SarmataSettings
from techmo_sarmata_pyclient.service.sarmata_recognize import SarmataRecognizer
from techmo_sarmata_pyclient.service.asr_service_pb2 import ResponseStatus
from address_provider import AddressProvider
import os


def print_results(responses):
    if responses is None:
        print("Empty results - None object")
        return

    counter = 0

    for response in responses:
        if response is None:
            print("Empty results - skipping response")
            continue

        print("Received response with status: {}".format(ResponseStatus.Name(response.status)))

        if response.error:
            print("[ERROR]: {}".format(response.error))

        for n, res in enumerate(response.results):
            transcript = " ".join([word.transcript for word in res.words])
            if not res.semantic_interpretation:
                counter += 1
            else:
                print("[{}.] {} /{}/ ({})".format(n, transcript, res.semantic_interpretation, res.confidence))
            if counter == n+1:
                print("powtorz")






def get_results(wave_file, grammar_file):
        ap = AddressProvider()
        address = ap.get("sarmata")
        audio = load_wave(wave_file)
        settings = SarmataSettings()
        session_id = os.path.basename(wave_file)
        settings.set_session_id(session_id)
        settings.load_grammar(grammar_file)
        recognizer = SarmataRecognizer(address)
        results = recognizer.recognize(audio, settings)
        return results


# wave_file = "waves/example_atm.wav"
# grammar_file = "grammars/atm.abnf"
# print_results(get_results(wave_file,grammar_file))
