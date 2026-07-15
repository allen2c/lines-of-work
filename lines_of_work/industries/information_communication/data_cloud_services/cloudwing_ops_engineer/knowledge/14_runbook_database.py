title = "常见故障Runbook（三）：数据库慢查询/死锁"

content = """\
- 症状：慢查询日志激增，应用报错"Lock wait timeout exceeded"。影响：业务响应缓慢。
- 排查步骤：1）登录数据库，执行`SHOW FULL PROCESSLIST`查看当前查询状态。2）使用`SELECT * FROM information_schema.INNODB_TRX`查看事务。3）使用`SHOW ENGINE INNODB STATUS\G`查看死锁信息。4）分析慢查询日志，使用`pt-query-digest`汇总。
- 缓解措施：若为死锁，Kill阻塞事务（`KILL <thread_id>`）。若为慢查询，添加索引或改写SQL（需研发配合）。若为锁等待，调整`innodb_lock_wait_timeout`（默认50秒，可临时调低至10秒以快速失败）。
- 预防：开启慢查询日志（long_query_time=1秒），定期分析；使用连接池（如HikariCP）限制并发；读写分离。
"""

version = "0.0.1"
