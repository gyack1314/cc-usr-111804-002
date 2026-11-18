# 智能化能力分级检测证据的跨来源采集

现有项目保存分级测项与等级说明的冻结来源响应。transport 核对请求和原文字节，domain 提取来源声明的资料身份，ledger 原子保存版本，view 展示已收资料及待核状态。collection 将来源收据与接收进度持久保存，archive 保留已发布视图所引用的资料状态；跨来源业务归属尚未形成。合成样例不访问外部站点。来源字段见 docs/source-contract.md。

在项目根目录运行：

    python -m unittest discover -s tests -v
    python -m compileall -q capture_service tests
    python -m capture_service.cli inspect data/normal.json

容器运行：docker build -t robot-collection-002 .；docker run --rm robot-collection-002。
