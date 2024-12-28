import serial
import matplotlib.pyplot as plt

# Настройка последовательного порта
ser = serial.Serial('COM3', 115200)

try:
    while True:
        data = ser.read(1024 * 2)  # Читаем 1024 * 2 байта
        if len(data) == 1024 * 2:  # Проверяем, что получены все данные
            adc_values = []
            for i in range(0, len(data), 2):
                adc_value = data[i] | (data[i+1] << 8)  # Собираем uint16_t из двух байт
                adc_values.append(adc_value)

            # Визуализация данных
            plt.plot(adc_values)
            plt.xlabel('Sample')
            plt.ylabel('ADC Value')
            plt.title('ADC Data')
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
