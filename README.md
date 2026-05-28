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
cd apriori-fraude-ingressos

# Não há dependências externas!
# Usa apenas bibliotecas padrão do Python
```

### Uso Básico

```python
from apriori_fraude_ingressos import AprioriBasico

# Dados de transações
transacoes = [
    frozenset(['valor_alto', 'multiplos_ingressos', 'mesma_ip']),
    frozenset(['venda_rapida', 'mesma_ip']),
    frozenset(['documento_invalido', 'pais_diferente']),
    # ... mais transações
]

# Executar Apriori
apriori = AprioriBasico(min_suporte=0.25)
apriori.carregar_dados(transacoes)
apriori.executar()

# Gerar regras
regras = apriori.gerar_regras(min_confianca=0.5)

# Exibir resultados
for regra in regras[:5]:
    print(f"{regra['antecedente']} => {regra['consequente']}")
    print(f"Confiança: {regra['confianca']:.1%}")
```

### Executar Exemplos

```bash
# Rodas a análise principal
python apriori_fraude_ingressos.py

# Ver 6 exemplos práticos detalhados
python exemplos_praticos_apriori.py
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

## 💡 Próximos Passos

### Para Melhorar

- [ ] Adicionar persistência em banco de dados
- [ ] Criar API REST para verificação em tempo real
- [ ] Integrar com sistema de pagamento
- [ ] Dashboard de visualização
- [ ] Validação cruzada com dados históricos
- [ ] Cálculo automático de suporte/confiança ideais

### Para Estender

- [ ] Detecção de anomalias com Isolation Forest
- [ ] Classificação com Random Forest
- [ ] Redes neurais para padrões complexos
- [ ] Ensemble de modelos

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

## 🔍 Visualizar Documentação

Abra `GUIA_APRIORI_FRAUDE.md` para:

1. ✅ O que é Apriori
2. ✅ Como funciona (passo a passo)
3. ✅ Aplicação em fraude
4. ✅ Exemplos com dados reais
5. ✅ Vantagens e desvantagens
6. ✅ Comparação com outras técnicas
7. ✅ Parâmetros e tuning
8. ✅ Implementação prática
9. ✅ Casos de uso
10. ✅ Conclusões

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

## 📚 Referências

- Agrawal & Srikant (1994). "Fast algorithms for mining association rules"
- Han et al. (2012). "Data Mining: Concepts and Techniques"

## 📄 Licença

MIT License - Sinta-se livre para usar, modificar e distribuir.

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## ❓ Dúvidas?


---

**Desenvolvido por Gabriel e Diogo** 🎯
