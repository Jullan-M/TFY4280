from Assignment5.spectrum_analyzer import *

if (__name__ == '__main__'):
    fs, sig_wav = read_wav('fysikk.wav', 16)
    car = Signal(fs, sig_wav)

    # Analyzing the FIRST pass of the car
    # From 8s to 14s
    c1_1 = Signal(car.fs, car[int(8*car.fs):int(10.5*car.fs)])
    c1_1.name = '8-10.5'

    c1_2 = Signal(car.fs, car[int(10.5*car.fs):int(11.5*car.fs)])
    c1_2.name = '10.5-11.5'

    c1_3 = Signal(car.fs, car[int(11.5*car.fs):int(14.0*car.fs)])
    c1_3.name = '11.5-14.0'

    f_l1, f_r1 = 2400, 2800

    c1_1.plot_magnitude_spec(f_range=[f_l1,f_r1], amp=0.001)
    c1_2.plot_magnitude_spec(f_range=[f_l1,f_r1], amp=0.001)
    c1_3.plot_magnitude_spec(f_range=[f_l1,f_r1], amp=0.001)

    print('Max amp @',c1_1.argmax_freq_within(f_l1, f_r1))
    print('Max amp @',c1_2.argmax_freq_within(f_l1, f_r1))
    print('Max amp @',c1_3.argmax_freq_within(f_l1, f_r1))

    # Analyzing the SECOND pass of the car
    # From 21s to 27s
    c2_1 = Signal(car.fs, car[int(21*car.fs):int(24.5*car.fs)])
    c2_1.name = '21-24.5'

    c2_2 = Signal(car.fs, car[int(24.5*car.fs):int(25.0*car.fs)])
    c2_2.name = '24.5-25.0'

    c2_3 = Signal(car.fs, car[int(25.0*car.fs):int(27.0*car.fs)])
    c2_3.name = '25.0-27.0'

    f_l2, f_r2 = 1100, 1500

    c2_1.plot_magnitude_spec(f_range=[f_l2,f_r2], amp=0.002)
    c2_2.plot_magnitude_spec(f_range=[f_l2,f_r2], amp=0.002)
    c2_3.plot_magnitude_spec(f_range=[f_l2,f_r2], amp=0.002)

    print('Max amp @',c2_1.argmax_freq_within(1200, f_r2))
    print('Max amp @',c2_2.argmax_freq_within(f_l2, f_r2))
    print('Max amp @',c2_3.argmax_freq_within(f_l2, f_r2))