import serial
import matplotlib.pyplot as plt

# Настройка последовательного порта
ser = serial.Serial('COM3', 115200)
ADC_BUFFER_SIZE = 64

try:
    while True:
        data = ser.read(ADC_BUFFER_SIZE * 2)  # Читаем буфер * 2 байта
        if len(data) == ADC_BUFFER_SIZE * 2:  # Проверяем, что получены все данные
            adc_values = []
            for i in range(0, len(data), 2):
                adc_value = data[i] | (data[i+1] << 8)  # Собираем uint16_t из двух байт
                adc_values.append(adc_value)

            # Продублирование массива
            duplicated_adc_values = [value for value in adc_values for _ in range(2)]

            # Визуализация данных
            plt.plot(duplicated_adc_values)

            plt.xlabel('Sample')
            plt.ylabel('ADC')
            plt.title('Data')
            plt.grid(True)
            plt.pause(0.001)
            plt.clf()
        else:
            print("Incomplete data received")
except KeyboardInterrupt:
    print("Программа остановлена пользователем")
finally:
    ser.close()
    plt.close()
