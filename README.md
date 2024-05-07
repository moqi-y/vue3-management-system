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
|——web                      # 前端Web页面文件
```

### 前端项目启动

```bash
# 切换目录
cd /web

# 安装 pnpm
npm install pnpm -g

# 安装依赖
pnpm install

# 启动运行
pnpm run dev
```

### 前端项目部署

```bash
# 项目打包
pnpm run build:prod

# 上传文件至远程服务器
将打包生成在 `dist` 目录下的文件拷贝至 `/usr/share/nginx/html` 目录

# nginx.cofig 配置
server {
	listen     80;
	server_name  localhost;
	location / {
			root /usr/share/nginx/html;
			index index.html index.htm;
	}
	# 反向代理配置
	location /prod-api/ {
			proxy_pass http://vapi.youlai.tech/; # vapi.youlai.tech替换成你的后端API地址
	}
}
```

### 其他

前端项目地址为：[youlaitech/vue3-element-admin: 🔥基于 vue3 + vite5 + typescript + element-plus 构建的后台管理前端模板（配套后端源码），vue-element-admin 的 vue3 版本。 (github.com)](https://github.com/youlaitech/vue3-element-admin)，该项目根据上述前端进行后端的开发练习。在此特别感谢`youlaitech/vue3-element-admin`项目。