"""验证 n.e.k.o-skill 仓库里的技能包可被 skill_compat 扫描加载。"""
import sys
sys.path.insert(0, r"C:\Users\jh\N.E.K.O")

import asyncio
import threading

from plugin.plugins.skill_compat import SkillCompatPlugin


def main():
    p = SkillCompatPlugin.__new__(SkillCompatPlugin)
    p._idx = {}
    p._lock = threading.Lock()
    p._skill_dirs = [r"C:\Users\jh\N.E.K.O\plugins_extra\n.e.k.o-skill\skills"]
    p._follow_symlinks = True
    p._scan_status = "未扫描"
    p._consent_given = True

    async def run():
        await p._ensure_scan()
        out = await p.list_skills(keyword="")
        return out

    out = asyncio.get_event_loop_policy().new_event_loop().run_until_complete(run())
    # list_skills 返回 Ok 包装（v0.1.26 后的 sdk 返回风格），解包 value
    data = out.value if hasattr(out, "value") else out
    print("scan_status:", p._scan_status)
    for s in data["skills"]:
        print(f"  - {s['name']}: {s['description'][:60]}")
    assert data["count"] >= 3, f"预期 ≥3 个技能，实际 {data['count']}"
    print(f"[OK] {data['count']} skills loadable")


if __name__ == "__main__":
    main()
