from math import floor

frame_rate = 11025

def tri(frequency, amplitude=0.3):
    """A continuous triangle wave."""
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

def saw(frequency, amplitude=0.3):
    """A non-continuous saw wave."""
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        return amplitude * saw_wave
    return sampler

def square(frequency, amplitude=0.3):
    period = frame_rate // frequency
    def sampler(t):
        if ((t // period) % 4) < 2:
            square_wave = -3
        else:
            square_wave = 3
        return amplitude * square_wave
    return sampler

