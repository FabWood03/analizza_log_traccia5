import manage_log as ml
import argument_parser as ap


def main():
    # Crea il parser degli argomenti
    args = ap.create_parser()

    # Estrae i percorsi dei file dagli argomenti
    filepath = args.file_input
    newfilepath = args.file_output

    # Gestisce il processo di estrazione, elaborazione e salvataggio dei log
    log_data = ml.extract_log(filepath)
    result = ml.elaborate_log(log_data)
    ml.save_log(newfilepath, result)


if __name__ == "__main__":
    main()
