from spectrum_analyzer import *
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

if (__name__ == '__main__'):
    # Intervals on which to perform Fourier transform.
    # Note that the intervals are NOT of the same length.
    # Therefore Fourier magnitude plots will not useful for
    # comparing amplitudes. Here it is not a problem since
    # we are only interested in where the peaks are placed.
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

    # Standard tuning of guitar
    stds = [329.63, 246.94, 196, 146.83,    110,    82.41]
    std_names = [r'$E_4$', r'$B_3$', r'$G_3$', r'$D_3$', r'$A_2$', r'$E_2$']

    # Calculation begins here
    fs, sig_wav = read_wav('guitar.wav')

    gtr = Signal(fs, sig_wav)
    gtr.name = 'guitar'
    gtr.plot_signal(intrvls=intrvls)

    strings = []
    for i in range(12):
        strings.append(Signal(gtr.fs,
                              gtr[int(intrvls[i][0]*gtr.fs):int(intrvls[i][1]*gtr.fs)]))
        strings[i].name = 'str' + str(i + 1)

    f_l, f_r = 0, 500
    for s in range(6):
        plt.figure()
        s_ = 5 - s
        plt.title(std_names[s_])
        for st in range(6):
            plt.axvline(x=stds[st], c='g' if s_==st else 'r',
                        linewidth=0.6, linestyle='-.')
        plt.plot(strings[s].ftfreq, strings[s].ft_magn, c="b", linewidth=0.7, alpha=0.8)
        plt.plot(strings[11-s].ftfreq, strings[11-s].ft_magn, c="m", linewidth=0.7, alpha=0.8)
        plt.xlim(left = f_l, right = f_r)
        plt.ylim(bottom=0)
        plt.xlabel(r"Frequency, $f$ / Hz", fontsize=16)
        plt.ylabel(r"$|X(\omega)|$", fontsize=16)
        plt.grid()
        plt.savefig(strings[s].name + "_magn_spec.pdf")
        plt.show()

    for s in range(6):
        print()
        print('String', s+1, 'fundamental frequency:', stds[5-s], 'Hz')
        print('First:\t', strings[s].argmax_freq_within(stds[5 - s] - 10, stds[5 - s] + 10))
        print('Second:\t', strings[11-s].argmax_freq_within(stds[5 - s] - 10, stds[5 - s] + 10))
