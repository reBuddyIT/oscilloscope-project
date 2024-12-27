import serial
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 115200)  # Замените COM3 на ваш порт

while True:
    data = ser.read(1024 * 2)  # Читаем 1024 * 2 байта (BUFFER_SIZE * 2)
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
        plt.pause(0.001)  # Небольшая задержка для обновления графика
        plt.clf()  # Очистка графика для следующего цикла
    else:
        print("Incomplete data received")
