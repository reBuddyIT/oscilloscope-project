void setup()
{
  // Инициализация последовательного порта
  Serial.begin(115200);
}

void loop()
{
  // Отправка сообщения
  Serial.write("Message send by UART!");

  // Задержка на 2 мс
  delay(2);
}
