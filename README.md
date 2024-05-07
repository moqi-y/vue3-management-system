### 目录结构
```
.
├── app                  # 「app」是一个 Python 包
│    ├── __init__.py      # 这个文件使「app」成为一个 Python 包
│    ├── main.py          # 「main」模块，例如 import app.main
│    ├── dependencies.py  # 「dependencies」模块，例如 import app.dependencies
│    └── routers          # 「routers」是一个「Python 子包」
│    │   ├── __init__.py  # 使「routers」成为一个「Python 子包」
│    │   ├── items.py     # 「items」子模块，例如 import app.routers.items
│    │   └── users.py     # 「users」子模块，例如 import app.routers.users
│    └── middleware
│    │   ├── __init__.py
│    │   └── cors.py      # 跨域配置
│    └──sql_app           # 数据库配置
│    │   ├── __init__.py
│        │   └── models.py    # 数据库模型
│        └── database.py   # 数据库连接
│    └──utils           # 工具函数
│    │   ├── __init__.py
│    │   └── status_code.py # 状态码

```