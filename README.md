# Detector de Atenção Facial

Projeto desenvolvido como parte da Sprint 3 – IoT / Detecção Facial

---
## Integrantes do Grupo

| **Nome**                   | **RM**   |
|-----------------------------|----------|
| Rodrigo Fernandes Serafim  | RM550816 |
| João Antonio Rihan         | RM99656  |
| Adriano Lopes              | RM98574  |
| Henrique de Brito          | RM98831  |
| Rodrigo Lima               | RM98326  |

---

## 🔍 Descrição

Aplicação local (desktop) que detecta rosto e olhos usando OpenCV e Haar Cascade.  
Se os olhos ficarem fechados por tempo demais, exibe um alerta de atenção na tela.

---

## 🛠 Ferramentas Utilizadas

| Ferramenta | Uso no Projeto |
|-------------|------------------|
| **Python** | Linguagem de desenvolvimento. |
| **OpenCV** | Biblioteca principal para captura de vídeo, conversão de imagem, desenho de retângulos, exibição na tela. |
| **Haar Cascade** (OpenCV) | Modelos pré-treinados para detectar rosto (`haarcascade_frontalface_default.xml`) e olhos (`haarcascade_eye.xml`). |

---

## ⚙ Parâmetros ajustados / abordados

| Parâmetro | Valor no código | Propósito / impacto |
|------------|------------------|------------------------|
| `scaleFactor` em detecção de rosto | ~ **1.2** | Controla quanto a imagem é reduzida em cada escala. Maior valor = detecta rostos maiores, processamento mais rápido, mas pode faltar rostos menores. |
| `minNeighbors` em detecção de rosto | ~ **5** | Quantas janelas vizinhas são necessárias para “confirmar” um rosto. Mais alto = menos falsos positivos, mas risco de perder rostos. |
| `minSize` para rosto | ~ **(80, 80)** | Tamanho mínimo do retângulo de rosto. Desconsidera regiões muito pequenas. |
| Detecção de olhos somente na **metade superior do rosto** | sim | Reduz falsos positivos vindos da boca ou queixos. |
| `minNeighbors` em detecção de olhos | ~ **10** | Para olhos, usamos valor mais alto para aumentar confiança de que é realmente um olho. |
| `minSize` para olhos | ~ **(25, 25)** | Garante que olhos muito pequenos ou muito longe/cortados não sejam detectados erroneamente. |
| `limite_fechado` | **45 frames** | Número de quadros consecutivos sem detectar olhos para disparar o alerta. Aproximadamente **1,5 segundos** se a câmera rodar a ~30 fps. |

---


## 🚀 Como executar

1. Certifique-se de ter Python instalado (versão 3.x).  
2. Instale dependências:

   ```bash
   pip install opencv-python
   python detectorFacial.py

---


## ⚠ Limitações e itens para melhorias
1. Iluminação ruim ou rosto parcialmente virado/obstruído: o Haar Cascade pode falhar quando há óculos escuros, chapéu ou cabelo cobrindo o rosto. 
2. Olhos visíveis apenas: se estiver muito escuro ou mal enquadrado, o sistema pode não detectar nada, gerando falsos alertas.
3. Falsos positivos: algumas regiões do rosto (como boca ou sobrancelhas) podem ser confundidas com olhos – mitigado ao restringir a detecção apenas à metade superior do rosto.
4. Possíveis melhorias: usar MediaPipe Face Mesh para landmarks faciais ou aplicar métricas como Eye Aspect Ratio (EAR), que oferecem detecção de olhos mais robusta e precisa.


