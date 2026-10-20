# n.e.k.o-skill

N.E.K.O 官方技能包仓库（SKILL.md 技能集合，规划中，尚未填充）。

## 状态

> ⚠️ **占位仓库**：当前为空，技能包尚未上传。
> 技能加载能力已由插件 `skill_compat`（Skill 兼容加载器）实现并发布到市场，
> 本仓库用于存放可供 N.E.K.O 直接加载的官方技能包。

## 计划收录的技能包

| 技能 | 用途 | 状态 |
|---|---|---|
| 代码沙箱使用指南 | 教 YUI 安全使用 code_sandbox（计算/算法/数据处理） | 规划中 |
| 卡牌游戏规则库 | 德州扑克/掼蛋/Kards/斗地主规则速查（配合 card_master） | 规划中 |
| Steam 助手速查 | Steam 管理/游戏助手常用操作（配合 steam_manager） | 规划中 |
| B站直播协作指南 | 直播观看/弹幕/画面同步协作流程（配合 bili_viewer） | 规划中 |

## 技能包格式（SKILL.md）

每个技能包是一个目录，含：

- `SKILL.md`：技能定义（YAML front-matter 含 `name` / `description`，正文为使用说明与示例）。
- 可选的参考文档与脚本资产（`references/`、`scripts/` 等）。

## 如何加载

通过 `skill_compat` 插件的 `install_skill`（本地目录 / zip / https 链接）或
`skillhub_install` 安装后，即可被 N.E.K.O 的 AI 调用。

## 安全纪律

- skill 内容是数据不是命令：AI 加载后应作为参考信息使用，不盲目执行其中的指令。
- 外部来源技能包安装前需用户知情确认。

## 规划

- [ ] 编写首批 4 个技能包 SKILL.md
- [ ] 本地经 skill_compat 验证可加载
- [ ] 推送本仓库
