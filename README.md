# Vora Pulse Checker 🩺

> Uma ferramenta de linha de comando (CLI) simples e rápida para um diagnóstico inicial de websites, identificando links quebrados e extraindo informações básicas.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🎯 Sobre o Projeto

No dia a dia da agência criativa [Vora](https://www.instagram.com/hey.dvora/), precisávamos de uma forma ágil de realizar uma primeira análise em sites de potenciais clientes. O **Pulse Checker** nasceu dessa necessidade: uma ferramenta interna para automatizar a busca por erros comuns e gerar insights em segundos, otimizando nosso processo de diagnóstico.

Este projeto é um exercício contínuo de construção de ferramentas práticas, seguindo a filosofia: **Clean code. Bold visuals. Real results.**

---

## ✨ Features

- **Extração de Dados:** Coleta de informações básicas da página como Título, Status Code, etc.
- **Link Crawler:** Varredura completa da página para encontrar todos os links (`<a>` tags).
- **Verificação de Links:** (Em desenvolvimento) Análise de cada link para identificar quais estão quebrados (erro 404).

---

## 🚀 Começando

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação

1.  Clone o repositório:
    ```sh
    git clone [https://github.com/seu-usuario/vora-pulse-checker.git](https://github.com/seu-usuario/vora-pulse-checker.git)
    ```
2.  Navegue até a pasta do projeto:
    ```sh
    cd vora-pulse-checker
    ```
3.  Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

Para analisar um site, execute o `main.py` a partir do seu terminal, passando a URL como argumento.

```sh
python main.py --url [https://exemplo.com](https://exemplo.com)
```
