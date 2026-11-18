# kiosk · 社区借阅柜日历、请求和副本调运

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m kiosk week data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

营业记录 `windows` 以 `day/cabinet` 为键，布尔 `request_log` 表示能够接收未满足请求，`state` 为 open、closed、counting 或 offline。`inventory` 是按日开门的可借副本，`requests` 中 `ticket` 是渠道共享的业务票号，`requested` 与 `loaned` 分别表示原读物和最终借出（空值表示未借到）。请求时间为相对开门分钟。
`restocks` 是同日柜机副本的非借出变动，时间同请求；借出扣减按最后实际借出的读物归属。`shipping` 以日为单位记录发出及到达时间；在借 `returns` 是已知归还日；`transfers` 的 confirmed 是已占用承诺。`floors` 是送出柜须可满足的请求份数底线。周报目前只统计借出实绩与已登记的运输选项。
