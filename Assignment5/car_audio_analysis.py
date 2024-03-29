from spectrum_analyzer import *
from matplotlib import rc

# Latex font rendering
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

if (__name__ == '__main__'):
    intrvls1 = [[7,10.5], #[10.5,11.5],
                [11.9,13.8]]
    intrvls2 = [[21,24.5], #[24.5,25.0],
                [25.0,27.0]]
    fs, sig_wav = read_wav('Assignment5/fysikk.wav')
    car = Signal(fs, sig_wav)
    car.name = 'car'
    car.plot_signal(t_range=[0,28.0], intrvls=(intrvls1 + intrvls2) )
    # Analyzing the FIRST pass of the car
    # From 7s to 14s
    cs1 = []
    for i in range(len(intrvls1)):
        cs1.append(Signal(car.fs, car[int(intrvls1[i][0]*car.fs):int(intrvls1[i][1]*car.fs)]))
        cs1[i].name = str(intrvls1[i][0]) + '-' + str(intrvls1[i][1])

    f_l1, f_r1 = 2300, 2725
    cs1[0].plot_magnitude_spec(f_range=[f_l1,f_r1], amp=0.001)
    cs1[1].plot_magnitude_spec(f_range=[f_l1,f_r1], amp=0.0002)
    for c in cs1:
        print('Max amp @', c.argmax_freq_within(f_l1, f_r1))

    # Analyzing the SECOND pass of the car
    # From 21s to 27s
    cs2 = []
    for i in range(len(intrvls2)):
        cs2.append(Signal(car.fs, car[int(intrvls2[i][0]*car.fs):int(intrvls2[i][1]*car.fs)]))
        cs2[i].name = str(intrvls2[i][0]) + '-' + str(intrvls2[i][1])

    f_l2, f_r2 = 1135, 1400
    cs2[0].plot_magnitude_spec(f_range=[f_l2,f_r2], amp=0.003)
    cs2[1].plot_magnitude_spec(f_range=[f_l2,f_r2], amp=0.0005)
    for c in cs2:
        print('Max amp @', c.argmax_freq_within(f_l2, f_r2))

    car.plot_spectrogram(t_range=[0,28.0], intrvls=(intrvls1 + intrvls2), freqs=[2683, 2359,1376,1140])
