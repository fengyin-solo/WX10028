# 桥梁健康监测管理平台

面向传感器布设、应变监测、振动监测、索力监测、裂缝巡检、定期检测、评定报告与维修加固的一体化桥梁健康监测管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 桥梁台账 | `bridge` | 桥梁 | 桥梁编号、桥梁名称、所在线路 |
| 传感器管理 | `sensor` | 传感器 | 传感器编号、传感器类型、安装位置 |
| 应变监测 | `strain` | 应变记录 | 记录编号、传感器编号、所属桥梁 |
| 振动监测 | `vibration` | 振动记录 | 记录编号、传感器编号、所属桥梁 |
| 索力监测 | `cable_force` | 索力记录 | 记录编号、索编号、所属桥梁 |
| 挠度监测 | `deflection` | 挠度记录 | 记录编号、所属桥梁、测点位置 |
| 裂缝巡检 | `crack` | 裂缝记录 | 裂缝编号、所属桥梁、裂缝位置 |
| 锈蚀检测 | `corrosion` | 锈蚀记录 | 记录编号、所属桥梁、检测部位 |
| 定期检测 | `routine_check` | 检测任务 | 任务编号、所属桥梁、检测类型 |
| 评定报告 | `assessment` | 评定报告 | 报告编号、所属桥梁、评定等级 |
| 维修加固 | `repair` | 维修项目 | 项目编号、项目名称、所属桥梁 |
| 支座管理 | `bearing` | 桥梁支座 | 支座编号、所属桥梁、支座类型 |
| 锚碇锚固管理 | `anchor` | 锚碇锚固 | 锚碇编号、所属桥梁、锚碇类型 |
| 交通荷载监测 | `traffic_monitor` | 荷载监测记录 | 记录编号、所属桥梁、车流量 |
| 预应力监测 | `tendon` | 预应力记录 | 记录编号、所属桥梁、预应力束编号 |
| 应急处置 | `emergency` | 应急事件 | 事件编号、所属桥梁、事件类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
