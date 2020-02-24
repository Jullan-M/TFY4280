import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt

class Signal:
    def __init__(self, signal, fs):
        self.name = ''
        self.signal = signal
        self.fs = fs # Sampling frequenct
        self.sig_shape = signal.shape
        self.Ns = 0 # Total num of samples

        # Dual-channel signals will be averaged to single channel.
        if (self.sig_shape[0] == 2):
            signal = signal.sum(axis=1) / 2
            self.Ns = self.sig_shape[1]
        else:
            self.Ns = self.sig_shape[0]

        self.secs = self.Ns / fs # Length of track
        self.Ts = 1.0/fs # Sample interval

        self.t = np.arange(0, self.secs, self.Ts)

        self.sig_ft = self.Ts * np.fft.fft(signal)
        self.sig_ftfreq = 2 * np.pi * np.fft.fftfreq(self.Ns, d=self.Ts)
        self.sig_fft_magn = np.abs(self.sig_ft)

    def __str__(self):
        return 'Channels:' + str(self.sig_shape[0]) + '|| Sampling rate:' +\
               str(self.fs) + 'Hz || Total samples:' + str(self.Ns) + \
               '|| Track length:' + str(self.secs) + 's || Sample intervals:' + \
               str(self.Ts) + 's'

    def plot_magnitude_spec(self, f_range=None, amp=None):
        plt.figure()
        plt.plot(self.sig_ftfreq, self.sig_fft_magn, c="b", linewidth=0.7)
        if self.name:
            plt.title(self.name)
        if (f_range != None):
            plt.xlim(left = f_range[0], right = f_range[1])
        else:
            plt.xlim(left = 0, right = self.fs/2)
        if (amp != None):
            plt.ylim(bottom=0, top = amp)
        plt.xlabel(r"Frequency, $f$ / Hz")
        plt.ylabel(r"Magnitude spectrum, $|X(\omega)|$", fontsize=16)
        plt.grid()
        plt.savefig(self.name + "magn_spec.pdf")
        plt.show()

def read_wav(filename, bitdepth):
    print('Reading "' + filename + '".')
    fs, signal = wavfile.read(filename)
    signal = signal/2.0**(bitdepth - 1) # Slice and normalize signal [-1,1)
    return fs, signal

print()

