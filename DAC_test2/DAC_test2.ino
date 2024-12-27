const int outputPin = 9; // ШИМ-выход
const int sampleRate = 21000; // Частота дискретизации (Гц). Чем выше, тем точнее, но требует больше ресурсов.
const float frequency = 100; // Частота синусоиды (Гц)

void setup()
{
  pinMode(outputPin, OUTPUT);
}

void loop()
{
  for (int i = 0; i < 256; i++)
  { // 256 шагов для аппроксимации синусоиды
    float angle = (float)i * 2.0 * PI / 256.0; // Расчет угла
    int pwmValue = 127 + (127 * sin(angle)); // Расчет значения для analogWrite()
    analogWrite(outputPin, pwmValue);
    delayMicroseconds(1000000 / sampleRate); // Задержка для установки частоты (важно!)
  }
}
