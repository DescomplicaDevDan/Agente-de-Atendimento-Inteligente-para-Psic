# 🤖 Agente de Atendimento Inteligente para Psicólogos

[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)]()
[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)]()

Este projeto é um **Agente de Atendimento Inteligente** projetado para otimizar a rotina de psicólogos, automatizando fluxos críticos como agendamento de consultas e gestão de dados de pacientes. O sistema é construído sobre uma arquitetura robusta, priorizando a segurança de dados sensíveis e a eficiência operacional.

---

## 🏗 Arquitetura do Sistema
O sistema foi desenhado para ser escalável e independente, utilizando **Docker** para isolamento de ambiente e **n8n** como motor de orquestração de fluxos.

- **Orquestração:** n8n (Self-hosted via Docker).
- **Integração de Dados:** Google Sheets API.
- **Gestão de Agenda:** Google Calendar API.
- **Comunicação:** Meta WhatsApp Business API (em integração).
- **Backend/Scripts:** Python (para automação e validação).

---

## 🚀 Destaques da Sprint 1 (Infraestrutura e Segurança)
* **Configuração de Ambiente Isolado:** Implementação de ambientes virtuais (`.venv`) para garantir a integridade das dependências.
* **Segurança em Camadas:** Utilização de `Service Accounts` (Google Cloud IAM) com privilégios limitados, seguindo o princípio do privilégio mínimo.
* **Gestão de Versão:** Controle rigoroso de versionamento com `.gitignore` configurado para impedir a exposição de credenciais sensíveis (secrets).

---

## 🔒 Compromisso com a Ética e Privacidade
Entendo a natureza sensível da psicologia. Por isso, a arquitetura deste agente é pensada para:
1. **Privacidade por Design:** Credenciais e tokens de acesso são tratados como variáveis de ambiente, nunca expostos no código-fonte.
2. **Conformidade:** Estrutura pronta para atender aos requisitos de armazenamento seguro e confidencialidade exigidos para profissionais da saúde.

---

## 🛠 Como rodar este projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/DescomplicaDevDan/Agente-de-Atendimento-Inteligente-para-Psic.git](https://github.com/DescomplicaDevDan/Agente-de-Atendimento-Inteligente-para-Psic.git)