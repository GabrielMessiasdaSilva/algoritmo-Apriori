'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
"""
"""

from itertools import combinations
from collections import defaultdict


class AprioriBasico:
    """Implementação básica do algoritmo Apriori"""
    
    def __init__(self, min_suporte=0.3):
        """
        Inicializa o Apriori
        
        Args:
            min_suporte: suporte mínimo (entre 0 e 1)
        """
        self.min_suporte = min_suporte
        self.transacoes = []
        self.num_transacoes = 0
        self.itemsets_frequentes = {}
        self.regras = []
    
    def carregar_dados(self, transacoes):
        """Carrega os dados de transações"""
        self.transacoes = transacoes
        self.num_transacoes = len(transacoes)
        print(f"✓ {self.num_transacoes} transações carregadas")
    
    def calcular_suporte(self, itemset):
        """Calcula o suporte de um itemset"""
        contagem = sum(1 for transacao in self.transacoes 
                      if itemset.issubset(transacao))
        return contagem / self.num_transacoes
    
    def encontrar_itemsets_frequentes_1(self):
        """Encontra itemsets frequentes de tamanho 1"""
        itens_unicos = defaultdict(int)
        
        for transacao in self.transacoes:
            for item in transacao:
                itens_unicos[item] += 1
        
        # Filtra por suporte mínimo
        itemsets_freq = {}
        for item, contagem in itens_unicos.items():
            suporte = contagem / self.num_transacoes
            if suporte >= self.min_suporte:
                itemsets_freq[frozenset([item])] = suporte
        
        return itemsets_freq
    
    def gerar_candidatos(self, itemsets_anteriores, k):
        """Gera candidatos combinando itemsets anteriores"""
        items = list(itemsets_anteriores.keys())
        candidatos = set()
        
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                uniao = items[i] | items[j]
                if len(uniao) == k:
                    candidatos.add(uniao)
        
        return candidatos
    
    def executar(self):
        """Executa o algoritmo Apriori completo"""
        print(f"\n{'='*60}")
        print(f"Algoritmo Apriori - Suporte Mínimo: {self.min_suporte*100}%")
        print(f"{'='*60}\n")
        
        # Passo 1: Encontrar itemsets frequentes de tamanho 1
        itemsets_atuais = self.encontrar_itemsets_frequentes_1()
        k = 1
        
        self.itemsets_frequentes[k] = itemsets_atuais
        print(f"Itemsets frequentes de tamanho {k}: {len(itemsets_atuais)}")
        for itemset, suporte in list(itemsets_atuais.items())[:5]:
            print(f"  {set(itemset)} - Suporte: {suporte:.2%}")
        
        # Passos 2+: Encontrar itemsets frequentes maiores
        while len(itemsets_atuais) > 1:
            k += 1
            candidatos = self.gerar_candidatos(itemsets_atuais, k)
            
            if not candidatos:
                break
            
            itemsets_atuais = {}
            for candidato in candidatos:
                suporte = self.calcular_suporte(candidato)
                if suporte >= self.min_suporte:
                    itemsets_atuais[candidato] = suporte
            
            if itemsets_atuais:
                self.itemsets_frequentes[k] = itemsets_atuais
                print(f"Itemsets frequentes de tamanho {k}: {len(itemsets_atuais)}")
                for itemset, suporte in list(itemsets_atuais.items())[:3]:
                    print(f"  {set(itemset)} - Suporte: {suporte:.2%}")
        
        print(f"\n{'='*60}")
        print(f"Total de itemsets frequentes encontrados: {sum(len(v) for v in self.itemsets_frequentes.values())}")
        print(f"{'='*60}\n")
    
    def gerar_regras(self, min_confianca=0.6):
        """Gera regras de associação com confiança mínima"""
        print(f"Gerando regras (Confiança Mínima: {min_confianca*100}%)...\n")
        
        self.regras = []
        
        # Iterar sobre todos os itemsets frequentes com tamanho >= 2
        for k in sorted(self.itemsets_frequentes.keys()):
            if k < 2:
                continue
            
            for itemset, suporte_AB in self.itemsets_frequentes[k].items():
                itemset_list = list(itemset)
                
                # Para cada item no itemset, criar regra
                for i in range(len(itemset_list)):
                    A = frozenset([itemset_list[i]])
                    B = frozenset(itemset_list[:i] + itemset_list[i+1:])
                    
                    # Calcular confiança: P(B|A) = P(A ∩ B) / P(A)
                    suporte_A = self.itemsets_frequentes.get(1, {}).get(A, 0)
                    
                    if suporte_A > 0:
                        confianca = suporte_AB / suporte_A
                        
                        if confianca >= min_confianca:
                            # Calcular lift: P(A ∩ B) / (P(A) * P(B))
                            suporte_B = self.itemsets_frequentes.get(1, {}).get(B, 0)
                            if suporte_B > 0:
                                lift = suporte_AB / (suporte_A * suporte_B)
                            else:
                                lift = 0
                            
                            self.regras.append({
                                'antecedente': set(A),
                                'consequente': set(B),
                                'suporte': suporte_AB,
                                'confianca': confianca,
                                'lift': lift
                            })
        
        # Ordena por confiança decrescente
        self.regras.sort(key=lambda x: x['confianca'], reverse=True)
        
        print(f"Total de regras encontradas: {len(self.regras)}\n")
        
        # Exibe as top 10 regras
        print("Top 10 Regras de Associação:\n")
        for i, regra in enumerate(self.regras[:10], 1):
            print(f"{i}. {regra['antecedente']} => {regra['consequente']}")
            print(f"   Suporte: {regra['suporte']:.2%} | Confiança: {regra['confianca']:.2%} | Lift: {regra['lift']:.2f}")
            print()
        
        return self.regras


# ============================================================================
# DADOS: Cenário de Fraude em Ingressos de Jogos
# ============================================================================
# Cada transação representa um ingresso suspeito com seus atributos
# Atributos: valor_alto, mesmo_cartao, multiplos_ingressos, mesma_ip, 
#           venda_rapida, pais_diferente, documento_invalido

transacoes_ingressos = [
    # Transação 1: Fraude óbvia
    frozenset(['valor_alto', 'mesmo_cartao', 'multiplos_ingressos', 'mesma_ip', 'venda_rapida']),
    
    # Transação 2: Padrão suspeito
    frozenset(['valor_alto', 'multiplos_ingressos', 'mesma_ip', 'pais_diferente']),
    
    # Transação 3: Fraude combinada
    frozenset(['mesmo_cartao', 'multiplos_ingressos', 'venda_rapida', 'documento_invalido']),
    
    # Transação 4: Suspeita de revenda
    frozenset(['multiplos_ingressos', 'mesma_ip', 'venda_rapida']),
    
    # Transação 5: Potencial fraude
    frozenset(['valor_alto', 'mesmo_cartao', 'pais_diferente']),
    
    # Transação 6: Legítima
    frozenset(['valor_normal']),
    
    # Transação 7: Padrão fraude comum
    frozenset(['valor_alto', 'multiplos_ingressos', 'mesma_ip']),
    
    # Transação 8: Fraude com documento
    frozenset(['mesmo_cartao', 'documento_invalido', 'pais_diferente']),
    
    # Transação 9: Suspeita simples
    frozenset(['multiplos_ingressos', 'mesma_ip']),
    
    # Transação 10: Legítima
    frozenset(['valor_normal', 'documento_valido']),
    
    # Transação 11: Padrão fraude internacional
    frozenset(['valor_alto', 'pais_diferente', 'mesma_ip']),
    
    # Transação 12: Revenda suspeita
    frozenset(['multiplos_ingressos', 'venda_rapida', 'mesma_ip']),
    
    # Transação 13: Legítima
    frozenset(['valor_normal']),
    
    # Transação 14: Fraude múltipla
    frozenset(['valor_alto', 'mesmo_cartao', 'multiplos_ingressos']),
    
    # Transação 15: Suspeita combinada
    frozenset(['pais_diferente', 'mesma_ip', 'venda_rapida']),
    
    # Transação 16: Fraude IP
    frozenset(['multiplos_ingressos', 'mesma_ip', 'documento_invalido']),
    
    # Transação 17: Legítima
    frozenset(['valor_normal']),
    
    # Transação 18: Padrão fraude clássico
    frozenset(['valor_alto', 'multiplos_ingressos', 'venda_rapida']),
    
    # Transação 19: Suspeita documento
    frozenset(['documento_invalido', 'mesma_ip']),
    
    # Transação 20: Legítima
    frozenset(['valor_normal']),
]


# ============================================================================
# EXECUÇÃO
# ============================================================================

if __name__ == "__main__":
    # Criar instância do Apriori
    apriori = AprioriBasico(min_suporte=0.25)
    
    # Carregar dados
    apriori.carregar_dados(transacoes_ingressos)
    
    # Executar Apriori
    apriori.executar()
    
    # Gerar regras de associação
    regras = apriori.gerar_regras(min_confianca=0.5)
    
    # Análise de Fraude
    print(f"{'='*60}")
    print("ANÁLISE DE PADRÕES DE FRAUDE EM INGRESSOS")
    print(f"{'='*60}\n")
    
    print("Padrões Suspeitos Identificados:")
    print("-" * 60)
    
    for i, regra in enumerate(apriori.regras[:5], 1):
        antecedente = ', '.join(sorted(regra['antecedente']))
        consequente = ', '.join(sorted(regra['consequente']))
        
        print(f"\n{i}. PADRÃO:")
        print(f"   Se: {antecedente}")
        print(f"   Então: {consequente}")
        print(f"   Risco: {'ALTO' if regra['confianca'] > 0.7 else 'MÉDIO' if regra['confianca'] > 0.5 else 'BAIXO'}")
        print(f"   Confiabilidade: {regra['confianca']:.1%}")
    
    print(f"\n{'='*60}")
    print("Recomendações:")
    print("- Transações com valor_alto + multiplos_ingressos: Revisar manualmente")
    print("- Padrão mesma_ip + venda_rapida: Possível bot de revenda")
    print("- documento_invalido + pais_diferente: Alto risco de fraude")
    print(f"{'='*60}\n")