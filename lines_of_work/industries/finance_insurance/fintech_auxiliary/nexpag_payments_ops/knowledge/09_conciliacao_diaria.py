title = "Conciliação Diária de Transações PIX"

content = """
- Processo executado todos os dias úteis às 8h, utilizando arquivos de liquidação (formato .RET) baixados do sistema do BCB (Sisbacen).
- Passos: (1) importar arquivo .RET para o ReconPro; (2) comparar cada transação (EndToEndId, valor, data) com o banco interno; (3) marcar como conciliada ou divergente.
- Divergências comuns: valor diferente (arredondamento), transação não encontrada (falha de registro), transação a mais (duplicidade).
- Prazo para resolver divergências: até 48h úteis; após isso, abrir chamado para o BCB via Sisbacen.
"""

version = "0.0.1"
