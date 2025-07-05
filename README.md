# PDF结构化解析为Markdown

本项目实现端到端的PDF文档结构化解析，自动将多页PDF文档转换为标准Markdown文本，涵盖正文、标题、表格、公式等结构。支持批量处理，输出为result.csv，格式为["file_id", "answer"]。

## 依赖安装
```bash
pip install -r requirements.txt
```

## 使用方法
1. 将待解析PDF放入`pdfs/`目录。
2. 运行：
```bash
python src/main.py
```
3. 结果保存在`results/result.csv`。

## 目录结构
- pdfs/           # 存放PDF文件
- results/        # 输出CSV结果
- src/            # 主要代码 