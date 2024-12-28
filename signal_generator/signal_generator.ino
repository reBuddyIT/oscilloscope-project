// Установите значение ШИМ (от 0 до 255)
int pwmValue = 255;

void setup()
{
  // Установите вывод 9 как выход
  pinMode(9, OUTPUT);

  // Установите значение ШИМ на выводе 9
  analogWrite(9, pwmValue);
}

void loop()
{

}
