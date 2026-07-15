title = "常见故障Runbook（一）：高CPU/内存"

content = """\
- 症状：CPU使用率持续>90%或内存>92%。影响：应用响应变慢，可能触发OOM。
- 排查步骤：1）登录主机，执行`top`或`htop`查看进程占用。2）使用`ps aux --sort=-%cpu`定位高CPU进程。3）使用`strace -p <PID>`跟踪系统调用（若怀疑死循环）。4）检查应用日志（`journalctl -u <service>`或`tail -f /var/log/app.log`）是否有异常。
- 缓解措施：若为应用Bug，立即重启服务（`systemctl restart <service>`）。若为突发流量，临时扩容（增加Pod副本或升级实例规格）。若为内存泄漏，重启后需联系研发分析堆转储（heap dump）。
- 预防：配置HPA自动扩容；设置OOM Killer保护（`oom_score_adj`）；定期分析JVM/Node.js内存使用。
"""

version = "0.0.1"
