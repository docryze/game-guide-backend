src/ (源码目录)
main.py: 这是你的应用程序入口文件。它负责创建 FastAPI 实例，并包含所有顶层路由。通常，你会在这里导入并注册你在 routers/ 目录中定义的子路由。

**init**.py: 使 app 目录成为一个 Python 包，以便你可以从其他地方导入其中的模块。

config.py: 存放所有配置信息，例如数据库连接字符串、API 密钥、环境变量等。使用 pydantic.BaseSettings 可以很方便地从环境变量中加载这些配置。

models.py: 定义你的数据库模型。如果你使用 ORM（如 SQLAlchemy、SQLModel），这些模型会定义你的数据表结构。

schemas/: 存放所有 Pydantic 模型。这些模型用于定义 API 的请求体和响应数据结构，与数据库模型 models.py 分开，可以更好地隔离业务逻辑和数据表示。

routers/: 用于组织你的路由。你应该根据功能模块将路由拆分到不同的文件中，每个文件都使用 fastapi.APIRouter 来创建子路由。例如，items.py 负责处理所有与商品相关的 API。

dependencies/: (可选) 存放所有依赖注入的函数。例如，用于获取数据库会话、进行身份验证等。

tests/ (测试目录)
test_main.py: 存放你的单元测试和集成测试代码。使用 pytest 配合 TestClient 可以轻松测试你的 API 端点。

项目根目录文件解析
.env: 存放环境变量。在开发环境中，你可以将数据库密码等敏感信息放在这里。在生产环境中，你会通过 Docker 或其他部署工具注入这些环境变量。

.gitignore: 指定 Git 在版本控制中忽略的文件和目录，例如 .env、**pycache** 等。

Dockerfile: 如果你打算使用 Docker 容器化部署，这个文件是必需的，它定义了如何构建你的应用程序镜像。

requirements.txt 或 pyproject.toml:

requirements.txt: 存放所有项目依赖。这是传统方式。

pyproject.toml: 如果你使用 Poetry 或 Poetry 来管理依赖，这是更现代、更推荐的方式。它包含依赖信息和项目元数据。

README.md: 包含项目说明、安装和运行指南、API 文档链接等。
