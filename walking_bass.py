from notes import *
from song_create import *

def walking_bass_line(notes, note_length):
    """Creates a row of notes with each note 
    lasting a duration of note_length.
    """
    start_time = 0
    bass_line = note(notes[0], start_time, start_time + note_length - 0.05)
    notes, start_time = notes[1:], start_time + note_length
    while notes != []:
        bass_line = both(bass_line, note(notes[0], start_time, start_time + note_length - 0.05))
        notes, start_time = notes[1:], start_time + note_length
    return bass_line
