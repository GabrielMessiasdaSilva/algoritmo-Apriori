# Apriori para Detecção de Fraude em Ingressos 🎟️

Implementação do algoritmo Apriori em Python para identificar padrões de fraude na venda de ingressos de eventos esportivos.

## 📋 O que é?

O **Apriori** é um algoritmo de mineração de dados que descobre padrões frequentes em transações e gera regras de associação. Neste projeto, ele é usado para detectar fraudes em vendas de ingressos.

### Padrões de Fraude Detectados

- 🤖 **Revenda Automática**: Venda rápida + múltiplos ingressos (confiança: 85%)
- 💳 **Cartão Roubado**: Valor alto + país diferente + documento inválido (confiança: 95%)
- 👥 **Gang Organizada**: Mesmo IP + múltiplos usuários + mesma rede de cartões (confiança: 92%)

## 🚀 Como Usar

### Instalação

```bash
# Clonar repositório
git clone https://github.com/GabrielMessiasdaSilva/algoritmo-Apriori.git
cd algoritmo-Apriori

# Não há dependências externas!
# Usa apenas bibliotecas padrão do Python
```

### Executar Exemplos

```bash
# Rodas a análise principal
python main.py

```

## 📁 Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `main.py` | Implementação completa do algoritmo com dados de exemplo |

## 📊 Conceitos Principais

### Suporte
```
Suporte(X) = Transações com X / Total de transações
```
Mede com que frequência um padrão aparece.

### Confiança
```
Confiança(A → B) = Suporte(A ∩ B) / Suporte(A)
```
Mede a força da regra (0-100%).

### Lift
```
Lift(A → B) = Suporte(A ∩ B) / (Suporte(A) × Suporte(B))
```
Mede correlação (>1 = relação forte).

## ⚙️ Parâmetros Recomendados

Para fraude em ingressos:

```python
apriori = AprioriBasico(min_suporte=0.20)  # 20%
regras = apriori.gerar_regras(min_confianca=0.50)  # 50%
```

**Por quê?**
- Detecta padrões com frequência suficiente
- Reduz falsos positivos
- Tempo de execução: < 1 segundo
- Custo computacional: baixo

## 📈 Score de Risco Sugerido

```
< 40 pontos    → APROVAR ✅
40-70 pontos   → REVISAR MANUALMENTE ⚠️
> 70 pontos    → BLOQUEAR ❌
```

## 🎯 Resultados Esperados

Executando o código principal:

```
✓ 20 transações carregadas

Itemsets frequentes encontrados: 10

Top 3 Regras:
1. venda_rapida → multiplos_ingressos
   Confiança: 83% | Lift: 1.67
   
2. valor_alto → multiplos_ingressos
   Confiança: 71% | Lift: 1.43
   
3. multiplos_ingressos → mesma_ip
   Confiança: 70% | Lift: 1.40

Padrões Suspeitos Identificados: 5
```


## 📝 Atributos de Entrada

| Atributo | Tipo | Exemplo | Indica Fraude? |
|----------|------|---------|----------------|
| `valor_alto` | bool | R$ > 500 | Possivelmente |
| `multiplos_ingressos` | bool | 5+ ingressos | Sim |
| `mesma_ip` | bool | Mesmo IP (3+x) | Sim |
| `venda_rapida` | bool | < 2 minutos | Sim |
| `pais_diferente` | bool | País ≠ cadastro | Possivelmente |
| `documento_invalido` | bool | CPF genérico | Sim |
| `mesmo_cartao` | bool | Mesmo card (3+x) | Possivelmente |
| `valor_normal` | bool | Compra legítima | Não |


## 🛠️ Requisitos

- **Python**: 3.6+
- **Dependências**: Nenhuma! (apenas bibliotecas padrão)
- **Compatibilidade**: Linux, macOS, Windows

## 📊 Performance

| Métrica | Valor |
|---------|-------|
| Tempo de execução (20 transações) | < 100ms |
| Tempo de execução (1.000 transações) | < 500ms |
| Tempo de execução (100.000 transações) | ~5-10s |
| Memória necessária | Mínima |
| Escalabilidade | Boa |

## 📄 Licença

MIT License - Sinta-se livre para usar, modificar e distribuir.


---

**Desenvolvido por Gabriel e Diogo** 🎯
