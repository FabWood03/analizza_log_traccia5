import json


def extract_log(filepath: str):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return []
    except json.decoder.JSONDecodeError:
        print(f"Error decoding JSON from file {filepath}.")
        return []
    except PermissionError:
        print(f"File {filepath} not accessible due to permission issues.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")


def save_log(filepath: str, log_data):
    try:
        with open(filepath, 'w') as f:
            json.dump(log_data, f, indent=4)
    except PermissionError:
        print(f"File {filepath} not accessible due to permission issues.")
    except Exception as e:
        print(f"An error occurred: {e}")


def elaborate_log(log_data):
    """
    Elabora i dati dei log per calcolare il numero di utenti unici e di eventi unici per ogni data.

    """

    # Dizionari per tenere traccia degli utenti e degli eventi unici per data
    unique_user = {}
    unique_event = {}

    try:
        # Itera sui dati dei log
        for data in log_data:
            data_ora = data[0]
            user_id = data[1]
            event = data[2]

            data = data_ora.split(" ")[0]

            # Aggiunge l'utente e l'evento ai rispettivi set per la data
            unique_user[data] = unique_user.get(data, set())
            unique_user[data].add(user_id)

            # Aggiunge l'evento al set degli eventi unici per la data
            unique_event[data] = unique_event.get(data, set())
            unique_event[data].add(event)

        # Risultato con il conteggio degli utenti e degli eventi unici per data
        result = {
            "unique_user": {k: len(v) for k, v in unique_user.items()},
            "unique_event": {k: len(v) for k, v in unique_event.items()}
        }
    except (IndexError, KeyError, ValueError) as e:
        print(f"Error processing log data: {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

    return result
