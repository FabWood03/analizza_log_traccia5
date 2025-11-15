import argparse as ap
import os


def create_parser():
    """
    Crea e configura il parser degli argomenti della riga di comando.
    """
    # Crea il parser con una descrizione
    parser = ap.ArgumentParser(description="Process log files and save the output to a specified location.",
                               formatter_class=ap.RawDescriptionHelpFormatter)

    # Imposta i percorsi di default per input e output
    default_input = os.path.join(os.path.dirname(__file__), 'test_data', 'test_small.json')
    default_output = os.path.join(os.path.dirname(__file__), 'test_data', 'test_small_output.json')

    # Aggiunge gli argomenti per input e output
    parser.add_argument("-i", "--input", dest="file_input", help="Insert the input file containing the logs",
                        default=default_input)
    parser.add_argument("-o", "--output", dest="file_output", help="Insert the output file containing the logs",
                        default=default_output)

    return parser.parse_args()
