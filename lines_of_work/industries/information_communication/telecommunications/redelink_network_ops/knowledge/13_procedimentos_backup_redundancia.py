title = "Procedimentos de Backup e Redundância"

content = """
- Todos os roteadores core possuem redundância ativa/passiva. Em caso de falha, o failover deve ocorrer em menos de 10 segundos.
- O operador deve verificar semanalmente o status dos links redundantes (ex: link de backup via satélite para sites remotos).
- Backups de configuração são feitos automaticamente às 02h e armazenados em servidor externo. Em caso de falha de hardware, restaurar a configuração do backup mais recente.
- Testes de failover devem ser realizados a cada trimestre, com registro no Change Management.
"""

version = "0.0.1"
