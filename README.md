#  Energia Solar e Automação: Um Sistema Inteligente para Casas

Este projeto demonstra um protótipo funcional simples de um sistema inteligente de energia, integrando sensores, automação de cargas e controle com ESP32, com foco em eficiência e sustentabilidade.

## Objetivos

- Gerenciar o consumo de energia com base na luminosidade e temperatura.
- Automatizar o acionamento de cargas.
- Simular uso inteligente de energia solar e estado de bateria.
- Mostrar viabilidade técnica de automação com IoT e ESP32.

##  Tecnologias Utilizadas

- **ESP32 DevKit v1**
- **Sensores LDR** (luminosidade)
- **Sensor DHT22** (temperatura)
- **Relé** para carga
- **LED** como carga visual
- **Simulação no Wokwi**

##  Funcionalidades

- Acionamento de LED baseado na luz (LDR).
- Controle de carga baseado na temperatura (DHT22).
- Leitura de dados em tempo real via serial.
- Pronto para simular no [Wokwi][(https://wokwi.com/)](https://wokwi.com/projects/433415244644545537).

##  Demonstração em Vídeo

🔗 [Link do vídeo no YouTube](https://youtube.com/shorts/0qvz5Rx2lQ8?feature=share)

##  Relatório Técnico
- No projeto, usei o simulador Wokwi para montar um protótipo com ESP32, dois sensores de luz (LDR) e um servo motor. A ideia foi fazer o ESP32 ler a intensidade da luz em dois pontos diferentes e ajustar o servo para “apontar” para onde tem mais luz, simulando um rastreador solar.

- O código faz a leitura contínua dos LDRs e compara os valores para controlar o movimento do servo. Quando um sensor detecta mais luz, o servo se move para ajustar a posição, buscando sempre o ponto de maior luminosidade.

- Durante a simulação, consegui verificar pelo monitor serial que os sensores respondem conforme a luz e o servo movimenta conforme esperado. Isso mostra que o controle básico funciona e que o sistema pode ser a base para uma automação mais complexa de energia solar.

- Apesar de ser uma simulação, o resultado foi positivo para validar o funcionamento do protótipo antes de partir para uma montagem física.

## Justificativas do Projeto
- O projeto busca melhorar o aproveitamento da energia solar, tornando o consumo mais inteligente e eficiente. Com sensores de luz (LDR) e temperatura (DHT22), o sistema automatiza cargas e simula um rastreador solar, ajudando a captar mais energia conforme a posição do sol.

- O ESP32 foi escolhido por ser acessível, potente e com Wi-Fi, ideal para soluções em IoT. Além de otimizar o uso da energia disponível, o projeto promove sustentabilidade, podendo ser expandido para controle remoto, monitoramento via internet e integração com assistentes virtuais.

- A simulação no Wokwi confirmou que o sistema funciona, servindo como uma base segura para evoluir para uma versão física e mais completa.

##  Autores

- Pedro Henrique Oliveira Marques (RM563054)
- Pedro Mirabella Tonarque (RM563419)
- Guilherme Mota Melo (RM565887)

---
