import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("D:\\Python\\DSA\\modulo5_poo\\aplausos5.wav")
play_obj = wave_obj.play()
play_obj.wait_done()