import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt

class Signal:
    def __init__(self, fs, signal):
        self.name = ''
        self.save = True
        self.signal = signal
        self.fs = fs # Sampling frequency
        self.shape = signal.shape
        self.Ns = 0 # Total num of samples

        # Dual-channel signals will be averaged to single channel.
        if (self.shape[0] == 2):
            signal = signal.sum(axis=1) / 2
            self.Ns = self.shape[1]
        else:
            self.Ns = self.shape[0]

        self.secs = self.Ns / fs # Length of track
        self.Ts = 1.0/fs # Sample interval

        self.t = np.arange(0, self.secs, self.Ts)

        self.ft = self.Ts * np.fft.fft(self.signal)
        self.ftfreq = np.fft.fftfreq(self.Ns, d=self.Ts)
        self.ft_magn = np.abs(self.ft)

    def __str__(self):
        return 'Channels:' + str(self.shape[0]) + '|| Sampling rate:' +\
               str(self.fs) + 'Hz || Total samples:' + str(self.Ns) + \
               '|| Track length:' + str(self.secs) + 's || Sample intervals:' + \
               str(self.Ts) + 's'

    def __getitem__(self, item):
        return self.signal[item]

    def argmax_freq_within(self, f_l, f_r):
        n_l, n_r = int(f_l/self.fs*self.Ns), int(f_r/self.fs*self.Ns)
        #n_l = np.where(self.ftfreq == f_l)[0][0]
        #n_r = np.where(self.ftfreq == f_r)[0][0]
        n_m = n_l + np.argmax(self.ft_magn[n_l:n_r])
        f_m = self.ftfreq[n_m]
        return f_m

    def plot_magnitude_spec(self, f_range=None, amp=None):
        plt.figure()
        plt.plot(self.ftfreq, self.ft_magn, c="b", linewidth=0.7)
        if (f_range != None):
            plt.xlim(left = f_range[0], right = f_range[1])
        else:
            plt.xlim(left = 0, right = self.fs/2)
        if (amp != None):
            plt.ylim(bottom=0, top = amp)
        plt.xlabel(r"Frequency, $f$ / Hz")
        plt.ylabel(r"Magnitude spectrum, $|X(\omega)|$", fontsize=16)
        plt.grid()
        if self.save:
            plt.savefig(self.name + "_magn_spec.pdf")
        plt.show()

    def plot_signal(self, t_range=None):
        plt.figure()
        plt.plot(self.t, self.signal, c="b", linewidth=0.7)
        if (t_range != None):
            plt.xlim(left = t_range[0], right = t_range[1])
        plt.xlabel(r"Time, $t$ / s")
        plt.ylabel(r"Signal, $x(t)$", fontsize=16)
        plt.grid()
        if self.save:
            plt.savefig(self.name + "_signal.pdf")
        plt.show()

def read_wav(filename, bitdepth):
    print('Reading "' + filename + '".')
    fs, signal = wavfile.read(filename)
    signal = signal/2.0**(bitdepth - 1) # Normalize signal to [-1,1)
    return fs, signal