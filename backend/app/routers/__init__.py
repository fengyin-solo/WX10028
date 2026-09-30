"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import bridge as router_bridge
from app.routers import sensor as router_sensor
from app.routers import strain as router_strain
from app.routers import vibration as router_vibration
from app.routers import cable_force as router_cable_force
from app.routers import deflection as router_deflection
from app.routers import crack as router_crack
from app.routers import corrosion as router_corrosion
from app.routers import routine_check as router_routine_check
from app.routers import assessment as router_assessment
from app.routers import repair as router_repair
from app.routers import bearing as router_bearing
from app.routers import anchor as router_anchor
from app.routers import traffic_monitor as router_traffic_monitor
from app.routers import tendon as router_tendon
from app.routers import emergency as router_emergency

ROUTERS = [router_bridge, router_sensor, router_strain, router_vibration, router_cable_force, router_deflection, router_crack, router_corrosion, router_routine_check, router_assessment, router_repair, router_bearing, router_anchor, router_traffic_monitor, router_tendon, router_emergency]
