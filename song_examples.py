from song_create import *
from walking_bass import *

sunny = note(tri(e_freq), 0, 1/2)
sunny = both(sunny, note(tri(g_freq), 1/2, 3/4))
sunny = both(sunny, note(tri(c_freq * 2), 3/4, 1))
sunny = both(sunny, note(tri(e_freq * 2), 1, 4/3))
sunny = both(sunny, note(tri(c_freq * 2), 4/3, 5/3))
sunny = both(sunny, note(tri(g_freq), 5/3, 2))
sunny = both(sunny, note(tri(e_freq), 2, 2 + (1/8)))
sunny = both(sunny, note(tri(c_freq), 2 + (1/8), 2 + (1/4)))
sunny = both(sunny, note(tri(g_freq), 2 + (1/4), 2 + (3/8)))
sunny = both(sunny, note(tri(c_freq), 2 + (3/8), 2 + (1/2)))

lick = note(tri(d_freq), 0, 1/4)
lick = both(lick, note(tri(e_freq), 1/4, 1/2))
lick = both(lick, note(tri(f_freq), 1/2, 3/4))
lick = both(lick, note(tri(g_freq), 3/4, 1))
lick = both(lick, note(tri(eb_freq), 1, 1.05))
lick = both(lick, note(tri(e_freq), 1.05, 1.5))
lick = both(lick, note(tri(c_freq), 1.5, 1.75))
lick = both(lick, note(tri(d_freq), 1.75, 2.5))

sans = note(saw(d_freq), 0, 1/8 - 0.05)
sans = both(sans, note(saw(d_freq), 1/8, 1/4 - 0.05))
sans = both(sans, note(saw(d_freq * 2), 1/4, 1/2 - 0.05))
sans = both(sans, note(saw(a_freq), 1/2, 3/4 - 0.05))
sans = both(sans, note(saw(ab_freq), 7/8, 9/8 - 0.05))
sans = both(sans, note(saw(g_freq), 9/8, 11/8 - 0.05))
sans = both(sans, note(saw(f_freq), 11/8, 13/8 - 0.05))
sans = both(sans, note(saw(d_freq), 13/8, 7/4 - 0.05))
sans = both(sans, note(saw(f_freq), 7/4, 15/8 - 0.05))
sans = both(sans, note(saw(g_freq), 15/8, 2 - 0.05))

play(walking_bass_line([c, d, e, g, f, a, f, d, c, d, e, g, e, d, c, g, f, g, a, eb, f, a, 
                        eb, db, c, d, e, d, db, bb, a, g, f, e, d, c, d, f, g, b, c], 0.25), name='bass_line1.wav', seconds=11)
play(walking_bass_line([c, e, c, d, eb, d, c, d, c, g, a, g, bb, a, g, e, f, db, eb, f, g, 
                        ab, bb, b, c, d, e, d, db, bb, a, g, gb, a, d, e, gb], 0.25), name='bass_line2.wav', seconds=11)
play(walking_bass_line([e, d, c, d, e, e, e, e, d, d, d, d, e, g, g, g, e, d, c, d, e, e, 
                        e, c, d, d, e, d, c, g, c], 0.5), name='bass_line3.wav', seconds=16)
play(walking_bass_line([c, b, ab, a, e ,g, e, eb, d, db, bb, g, f, d, db, d, g, bb, a, g, gb, 
                        d, f, ab, g, c, d, f, e, c, e, d, c, c, c, c, c], 0.20), name='bass_line4.wav', seconds=30)

play(sunny, name='sunny_sound.wav', seconds=3)
play(lick, name='thelick.wav', seconds=2.75)
play(sans, name='sans.wav', seconds=2.25)
