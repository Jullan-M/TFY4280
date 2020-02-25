from Assignment5.spectrum_analyzer import *
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

if (__name__ == '__main__'):
    fs, sig_wav = read_wav('guitar.wav')

    gtr = Signal(fs, sig_wav)
    gtr.name = 'guitar'

    intrvls = [[0.4,     1.75],
              [1.8,     3.15],
              [3.2,     4.5],
              [4.55,    5.8],
              [5.85,     7.2],
              [7.3,     8.8],
              [10.5,    11.6],
              [11.7,    12.8],
              [12.9,    13.9],
              [14.0,    15.0],
              [15.1,    16.3],
              [16.4,    17.8]]

    gtr.plot_signal(intrvls=intrvls)

    strings = []

    for i in range(12):
        strings.append(Signal(gtr.fs,
                              gtr[int(intrvls[i][0]*gtr.fs):int(intrvls[i][1]*gtr.fs)]))
        strings[i].name = 'str' + str(i + 1)

    # Standard tuning of guitar
    stds = [329.63, 246.94, 196, 146.83,    110,    82.41]
    #       E4      B3      G3      D3      A2      E2
    f_l, f_r = 0, 500
    for string in strings:
        plt.figure()
        for std in stds:
            plt.axvline(x=std, c='r', linewidth=0.6, linestyle='-.')
        plt.plot(string.ftfreq, string.ft_magn, c="b", linewidth=0.7)
        plt.xlim(left = f_l, right = f_r)
        plt.xlabel(r"Frequency, $f$ / Hz")
        plt.ylabel(r"Magnitude spectrum, $|X(\omega)|$", fontsize=16)
        plt.grid()
        plt.savefig(string.name + "_magn_spec.pdf")
        plt.show()

    for s in range(6):
        print()
        print('String', s+1, 'fundamental frequency:', stds[5-s])
        print('First:\t', strings[s].argmax_freq_within(stds[5 - s] - 10, stds[5 - s] + 10))
        print('Second:\t', strings[11-s].argmax_freq_within(stds[5 - s] - 10, stds[5 - s] + 10))
