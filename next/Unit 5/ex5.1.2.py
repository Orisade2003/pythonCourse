import winsound


def create_music():
    """
    the function plays the rhythm of 'Yonatan HaKatan' "
    """
    freqs = {"la": 220,
             "si": 247,
             "do": 261,
             "re": 293,
             "mi": 329,
             "fa": 349,
             "sol": 392,
             }
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    notes_list = notes.split("-")
    notes_itr = iter(notes_list)
    print(type(notes_list))
    print(dir(notes_list))
    for note in notes_itr:
        note_and_freq = note.split(',')
        winsound.Beep(freqs.get(note_and_freq[0]), int(note_and_freq[1]))


def main():
    create_music()


if __name__ == "__main__":
    create_music()
