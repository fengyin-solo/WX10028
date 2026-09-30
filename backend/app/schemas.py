"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class BridgeEntry(BaseModel):
    """桥梁明细结构。"""

    field_0: str | None = None  # 桥梁编号
    field_1: str | None = None  # 桥梁名称
    field_2: str | None = None  # 所在线路
    field_3: str | None = None  # 桥梁类型
    field_4: str | None = None  # 跨径组合
    field_5: str | None = None  # 建成通车年份
    field_6: str | None = None  # 设计荷载等级
    field_7: str | None = None  # 运营状态

class SensorEntry(BaseModel):
    """传感器明细结构。"""

    field_0: str | None = None  # 传感器编号
    field_1: str | None = None  # 传感器类型
    field_2: str | None = None  # 安装位置
    field_3: str | None = None  # 所属桥梁
    field_4: str | None = None  # 安装日期
    field_5: str | None = None  # 标定日期
    field_6: str | None = None  # 量程范围
    field_7: str | None = None  # 运行状态

class StrainEntry(BaseModel):
    """应变记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 传感器编号
    field_2: str | None = None  # 所属桥梁
    field_3: str | None = None  # 测点位置
    field_4: str | None = None  # 应变值
    field_5: str | None = None  # 阈值上限
    field_6: str | None = None  # 采集时间
    field_7: str | None = None  # 数据状态

class VibrationEntry(BaseModel):
    """振动记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 传感器编号
    field_2: str | None = None  # 所属桥梁
    field_3: str | None = None  # 测点位置
    field_4: str | None = None  # 振动频率
    field_5: str | None = None  # 振幅峰值
    field_6: str | None = None  # 采集时间
    field_7: str | None = None  # 评定结果

class CableForceEntry(BaseModel):
    """索力记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 索编号
    field_2: str | None = None  # 所属桥梁
    field_3: str | None = None  # 索类型
    field_4: str | None = None  # 索力值
    field_5: str | None = None  # 设计索力
    field_6: str | None = None  # 偏差率
    field_7: str | None = None  # 评定结果

class DeflectionEntry(BaseModel):
    """挠度记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 测点位置
    field_3: str | None = None  # 挠度值
    field_4: str | None = None  # 阈值上限
    field_5: str | None = None  # 采集时间
    field_6: str | None = None  # 温度补偿值
    field_7: str | None = None  # 评定结果

class CrackEntry(BaseModel):
    """裂缝记录明细结构。"""

    field_0: str | None = None  # 裂缝编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 裂缝位置
    field_3: str | None = None  # 裂缝长度
    field_4: str | None = None  # 裂缝宽度
    field_5: str | None = None  # 发现日期
    field_6: str | None = None  # 发展趋势
    field_7: str | None = None  # 记录状态

class CorrosionEntry(BaseModel):
    """锈蚀记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 检测部位
    field_3: str | None = None  # 锈蚀等级
    field_4: str | None = None  # 影响面积
    field_5: str | None = None  # 检测日期
    field_6: str | None = None  # 检测方法
    field_7: str | None = None  # 处置建议

class RoutineCheckEntry(BaseModel):
    """检测任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 检测类型
    field_3: str | None = None  # 检测单位
    field_4: str | None = None  # 计划日期
    field_5: str | None = None  # 实际日期
    field_6: str | None = None  # 检测负责人
    field_7: str | None = None  # 任务状态

class AssessmentEntry(BaseModel):
    """评定报告明细结构。"""

    field_0: str | None = None  # 报告编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 评定等级
    field_3: str | None = None  # 评定日期
    field_4: str | None = None  # 评定单位
    field_5: str | None = None  # 评定依据
    field_6: str | None = None  # 主要病害
    field_7: str | None = None  # 报告状态

class RepairEntry(BaseModel):
    """维修项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 所属桥梁
    field_3: str | None = None  # 维修部位
    field_4: str | None = None  # 维修方案
    field_5: str | None = None  # 承建单位
    field_6: str | None = None  # 预算金额
    field_7: str | None = None  # 项目状态

class BearingEntry(BaseModel):
    """桥梁支座明细结构。"""

    field_0: str | None = None  # 支座编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 支座类型
    field_3: str | None = None  # 安装位置
    field_4: str | None = None  # 安装日期
    field_5: str | None = None  # 上次检查日期
    field_6: str | None = None  # 位移量
    field_7: str | None = None  # 支座状态

class AnchorEntry(BaseModel):
    """锚碇锚固明细结构。"""

    field_0: str | None = None  # 锚碇编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 锚碇类型
    field_3: str | None = None  # 设计锚固力
    field_4: str | None = None  # 上次检测力值
    field_5: str | None = None  # 检测日期
    field_6: str | None = None  # 锚固力衰减率
    field_7: str | None = None  # 运行状态

class TrafficMonitorEntry(BaseModel):
    """荷载监测记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 车流量
    field_3: str | None = None  # 重车比例
    field_4: str | None = None  # 最大轴重
    field_5: str | None = None  # 监测时段
    field_6: str | None = None  # 超标车辆数
    field_7: str | None = None  # 评定结果

class TendonEntry(BaseModel):
    """预应力记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 预应力束编号
    field_3: str | None = None  # 设计张拉力
    field_4: str | None = None  # 实测有效力
    field_5: str | None = None  # 损失率
    field_6: str | None = None  # 检测日期
    field_7: str | None = None  # 评定结果

class EmergencyEntry(BaseModel):
    """应急事件明细结构。"""

    field_0: str | None = None  # 事件编号
    field_1: str | None = None  # 所属桥梁
    field_2: str | None = None  # 事件类型
    field_3: str | None = None  # 发生时间
    field_4: str | None = None  # 事件等级
    field_5: str | None = None  # 影响车道数
    field_6: str | None = None  # 处置单位
    field_7: str | None = None  # 事件状态
