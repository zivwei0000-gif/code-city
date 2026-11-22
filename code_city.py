#!/usr/bin/env python3
"""程式之城 Code City - 以故事學 Python 的桌面遊戲（只用 Python 標準函式庫）。"""
import io, json, os, sys, tkinter as tk
from contextlib import redirect_stdout, redirect_stderr
from tkinter import font as tkfont

ICON_B64 = "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"
SAVE = os.path.join(os.path.expanduser("~"), ".code_city.json")
THEMES = {
    "scifi": dict(bg="#12161f", card="#1d2433", bd="#33405a", tx="#e8ecf3", sb="#9fb0cc", ac="#3ddc97", on="#0b1d14"),
    "toon": dict(bg="#fff7e6", card="#ffffff", bd="#f0b95a", tx="#2b2540", sb="#5d5578", ac="#ff7a59", on="#2b1208"),
    "calm": dict(bg="#f4f1ea", card="#ffffff", bd="#d8d2c4", tx="#26303b", sb="#55606d", ac="#2f7d6d", on="#ffffff"),
}
UI = {
    "zh": dict(game="程式之城", slogan="所有機器都失去了指令。只有你能用程式喚醒這座城市。", start="開始冒險", map="世界地圖",
               settings="設定", home="首頁", cont="繼續", skip="跳過劇情", run="執行", submit="送出", reset="重設",
               hint="看提示", output="輸出", task="任務", concept="概念", ok="通過", back="返回", next="下一關",
               replay="重玩此關", theme="色彩主題", lang="介面語言", size="字體大小", scifi="科幻深色", toon="卡通明亮",
               calm="護眼柔和", locked="尚未解鎖", cleared="機器甦醒了！", yours="你的解法", defaults="恢復預設",
               tests="測試", nohint="沒有更多提示了", speaker="小澪", tip="提示",
               retake="未達 2 星，需要重修才能進入下一關", retag="需重修"),
    "en": dict(game="Code City", slogan="Every machine has lost its instructions. Only you can wake the city with code.", start="Start", map="World map",
               settings="Settings", home="Home", cont="Continue", skip="Skip story", run="Run", submit="Submit", reset="Reset",
               hint="Hint", output="Output", task="Mission", concept="Concept", ok="Passed", back="Back", next="Next level",
               replay="Replay", theme="Color theme", lang="Language", size="Font size", scifi="Sci-fi dark", toon="Cartoon bright",
               calm="Soft calm", locked="Locked", cleared="The machine is awake!", yours="Your solution", defaults="Reset defaults",
               tests="Tests", nohint="No more hints", speaker="Mio", tip="Hint",
               retake="Under 2 stars: retake this level to move on", retag="Retake"),
}
LEVELS = [
    dict(title="指令與順序", title_en="Commands and order",
         story=["修復師小澪推開了甦醒區的大門。", "主控台一片漆黑，只有游標在閃爍。", "「先下指令吧。機器會一行一行、由上往下照順序執行。」"],
         task="依序印出兩行文字：第一行「啟動」，第二行「完成」。", concept="print(\"文字\") 會把文字顯示出來；程式從上到下依序執行。",
         start="# 在這裡寫程式\n", tests=[("", "啟動\n完成")],
         hints=["使用 print(\"文字\") 來顯示文字。", "寫兩行：print(\"啟動\") 然後 print(\"完成\")。"]),
    dict(title="變數與運算", title_en="Variables",
         story=["機器的記憶體被清空了。", "「它需要一個名字才能被叫醒。」小澪說。", "「變數就像貼了標籤的盒子，把名字放進去吧。」"],
         task="讓程式印出「喚醒：Aria」。你只需要修改變數 name。", concept="用 = 把值放進變數，例如 name = \"Aria\"。",
         start="name = \"\"\nprint(\"喚醒：\" + name)\n", tests=[("", "喚醒：Aria")],
         hints=["name 目前是空字串。", "把第一行改成 name = \"Aria\"。"]),
    dict(title="條件判斷", title_en="Conditions",
         story=["運轉區的發電機忽強忽弱。", "「能量不足就得充電，夠了就維持原狀。」", "「這就是『如果⋯就⋯』。」"],
         task="系統已設定好 energy。小於 5 印出「充電」，否則印出「正常」。", concept="if 條件: ... else: ... 讓程式依情況做不同的事。",
         start="# energy 已經由系統設定好了\n", tests=[("energy = 3", "充電"), ("energy = 8", "正常")],
         hints=["使用 if energy < 5: 再加 else:。", "冒號後的下一行要縮排 4 個空格。"]),
    dict(title="迴圈", title_en="Loops",
         story=["生產線上有三台機器等著啟動。", "「一台一台手動太慢了。」小澪笑著說。", "「讓迴圈替我們重複吧。」"],
         task="依序印出「啟動第1號」、「啟動第2號」、「啟動第3號」。", concept="for i in range(1, 4): 會讓縮排內的程式重複執行 3 次。",
         start="# 用 for 迴圈完成\n", tests=[("", "啟動第1號\n啟動第2號\n啟動第3號")],
         hints=["for i in range(1, 4): 會讓 i 變成 1、2、3。", "迴圈內寫 print(\"啟動第\" + str(i) + \"號\")。"]),
]


def run_code(code, prefix="", limit=300000):
    """在目前程序執行玩家程式，回傳 (輸出, 錯誤訊息或None)；以行數上限防止無限迴圈。"""
    buf, steps = io.StringIO(), [0]
    shift = 1 if prefix else 0
    def tracer(frame, event, arg):
        if event == "line":
            steps[0] += 1
            if steps[0] > limit:
                raise TimeoutError("程式執行太久，可能有無限迴圈")
        return tracer
    err = None
    try:
        compiled = compile((prefix + "\n" if prefix else "") + code, "<你的程式>", "exec")
        sys.settrace(tracer)
        with redirect_stdout(buf), redirect_stderr(buf):
            exec(compiled, {"__name__": "__main__"})
    except BaseException as e:
        ln = getattr(e, "lineno", None)
        tb = e.__traceback__
        while tb is not None:
            if tb.tb_frame.f_code.co_filename == "<你的程式>":
                ln = tb.tb_lineno
            tb = tb.tb_next
        where = "第 %d 行：" % max(1, ln - shift) if ln else ""
        err = "%s%s: %s" % (where, type(e).__name__, getattr(e, "msg", None) or e)
    finally:
        sys.settrace(None)
    return buf.getvalue(), err


def pick(cands, fams, default):
    return next((c for c in cands if c in fams), default)


class App:
    def __init__(s):
        s.root = tk.Tk()
        s.root.title("程式之城 · Code City")
        s.root.geometry("1040x700")
        s.root.minsize(920, 620)
        try:
            s.icon = tk.PhotoImage(data=ICON_B64)
            s.root.iconphoto(True, s.icon)
        except Exception:
            pass
        s.data = dict(theme="scifi", lang="zh", size=15, stars={})
        try:
            with open(SAVE, encoding="utf-8") as f:
                s.data.update(json.load(f))
        except Exception:
            pass
        fams = set(tkfont.families())
        fam = pick(["Microsoft JhengHei UI", "Microsoft JhengHei", "PingFang TC", "Noto Sans CJK TC", "Noto Sans TC"], fams, "TkDefaultFont")
        mono = pick(["Menlo", "Consolas", "Cascadia Mono", "DejaVu Sans Mono"], fams, "TkFixedFont")
        s.F = {k: tkfont.Font(family=mono if k == "m" else fam, size=12, weight="bold" if k in "bht" else "normal") for k in "nbhtsm"}
        s.sync_fonts()
        s.box = tk.Frame(s.root)
        s.box.pack(fill="both", expand=True)
        s.go(s.p_home)

    # ---------- 基礎 ----------
    def C(s): return THEMES[s.data["theme"]]
    def T(s, k): return UI[s.data["lang"]][k]
    def title(s, i): return LEVELS[i]["title" if s.data["lang"] == "zh" else "title_en"]
    def save(s):
        try:
            with open(SAVE, "w", encoding="utf-8") as f:
                json.dump(s.data, f, ensure_ascii=False)
        except Exception:
            pass
    def sync_fonts(s):
        z = int(s.data["size"])
        for k, d in dict(n=0, b=0, h=6, t=22, s=-2, m=0).items():
            s.F[k].configure(size=z + d)
    def go(s, fn, *a):
        s.cur = (fn, a)
        s.render()
    def render(s):
        for w in s.box.winfo_children():
            w.destroy()
        s.box.configure(bg=s.C()["bg"])
        s.cur[0](*s.cur[1])
    def lbl(s, p, text, f="n", fg="tx", bg="bg", **k):
        c = s.C()
        return tk.Label(p, text=text, font=s.F[f], fg=c[fg], bg=c[bg], **k)
    def card(s, p, **k):
        c = s.C()
        return tk.Frame(p, bg=c["card"], highlightbackground=c["bd"], highlightthickness=1, padx=14, pady=12, **k)
    def btn(s, p, text, cmd, primary=False):
        c = s.C()
        b = tk.Label(p, text=text, font=s.F["b"], bg=c["ac"] if primary else c["card"], fg=c["on"] if primary else c["tx"],
                     padx=16, pady=8, cursor="hand2", highlightthickness=1, highlightbackground=c["ac"] if primary else c["bd"])
        b.bind("<Button-1>", lambda e: cmd())
        return b
    def click(s, w, cmd):
        w.bind("<Button-1>", lambda e: cmd())
        for ch in w.winfo_children():
            s.click(ch, cmd)
    def bar(s, text=""):
        c = s.C()
        f = tk.Frame(s.box, bg=c["bg"])
        f.pack(fill="x", padx=24, pady=(16, 6))
        s.lbl(f, text, "h").pack(side="left")
        s.btn(f, s.T("settings"), lambda: s.open_settings()).pack(side="right")
        s.btn(f, s.T("home"), lambda: s.go(s.p_home)).pack(side="right", padx=8)
    def open_settings(s):
        if s.cur[0] != s.p_settings:
            s.prev = s.cur
        s.go(s.p_settings)
    def skyline(s, p, w, h):
        c = s.C()
        cv = tk.Canvas(p, width=w, height=h, bg=c["card"], highlightthickness=1, highlightbackground=c["bd"])
        x = 12
        for bw, bh in [(46, .5), (34, .8), (52, .6), (40, .95), (30, .45), (56, .7), (38, .85), (44, .55), (36, .75), (50, .6)]:
            if x + bw > w - 8:
                break
            cv.create_rectangle(x, h - 8 - bh * (h - 30), x + bw, h - 8, fill=c["ac"] if bh > .9 else c["bd"], outline="")
            x += bw + 10
        return cv
    def next_level(s):
        st = s.data["stars"]
        return next((i for i in range(len(LEVELS)) if st.get(str(i), 0) < 2), 0)

    # ---------- 頁面 ----------
    def p_home(s):
        c = s.C()
        s.bar()
        m = tk.Frame(s.box, bg=c["bg"])
        m.pack(expand=True)
        s.lbl(m, s.T("game"), "t").pack(pady=(0, 8))
        s.lbl(m, s.T("slogan"), "n", fg="sb", wraplength=520).pack(pady=(0, 16))
        s.skyline(m, 520, 130).pack(pady=(0, 18))
        r = tk.Frame(m, bg=c["bg"])
        r.pack()
        s.btn(r, s.T("start"), lambda: s.go(s.p_story, s.next_level(), 0), True).pack(side="left", padx=6)
        s.btn(r, s.T("map"), lambda: s.go(s.p_map)).pack(side="left", padx=6)

    def p_map(s):
        c = s.C()
        s.bar(s.T("map"))
        g = tk.Frame(s.box, bg=c["bg"])
        g.pack(fill="both", expand=True, padx=24, pady=10)
        for i in range(len(LEVELS)):
            g.columnconfigure(i % 2, weight=1)
            open_ = i == 0 or s.data["stars"].get(str(i - 1), 0) >= 2
            cd = s.card(g)
            cd.grid(row=i // 2, column=i % 2, sticky="nsew", padx=8, pady=8)
            s.lbl(cd, "%d · %s" % (i + 1, s.title(i)), "h", bg="card").pack(anchor="w")
            n = s.data["stars"].get(str(i), 0)
            tag = ("★" * n + "☆" * (3 - n)) if open_ else s.T("locked")
            if open_ and 0 < n < 2:
                tag += "　" + s.T("retag")
            s.lbl(cd, tag, "n", fg="ac" if open_ else "sb", bg="card").pack(anchor="w", pady=(6, 0))
            if open_:
                cd.configure(cursor="hand2")
                s.click(cd, lambda i=i: s.go(s.p_story, i, 0))

    def p_story(s, i, k):
        c = s.C()
        lv = LEVELS[i]
        s.bar("%d · %s" % (i + 1, s.title(i)))
        s.skyline(s.box, 900, 200).pack(padx=24, pady=8, fill="x")
        d = s.card(s.box)
        d.pack(fill="x", padx=24, pady=8)
        s.lbl(d, s.T("speaker"), "h", fg="ac", bg="card").pack(anchor="w")
        s.lbl(d, lv["story"][k], "n", bg="card", wraplength=860, justify="left").pack(anchor="w", pady=10)
        r = tk.Frame(d, bg=c["card"])
        r.pack(fill="x")
        s.lbl(r, "%d / %d" % (k + 1, len(lv["story"])), "s", fg="sb", bg="card").pack(side="left")
        last = k + 1 >= len(lv["story"])
        s.btn(r, s.T("cont"), lambda: s.go(s.p_challenge, i) if last else s.go(s.p_story, i, k + 1), True).pack(side="right")
        s.btn(r, s.T("skip"), lambda: s.go(s.p_challenge, i)).pack(side="right", padx=8)

    def p_challenge(s, i):
        c = s.C()
        lv = LEVELS[i]
        s.bar("%d · %s" % (i + 1, s.title(i)))
        main = tk.Frame(s.box, bg=c["bg"])
        main.pack(fill="both", expand=True, padx=24, pady=6)
        main.columnconfigure(1, weight=3)
        main.columnconfigure(2, weight=2)
        main.rowconfigure(0, weight=1)
        used = [0]
        L = s.card(main)
        L.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        s.lbl(L, s.T("task"), "h", bg="card").pack(anchor="w")
        s.lbl(L, lv["task"], "n", bg="card", wraplength=240, justify="left").pack(anchor="w", pady=(4, 10))
        s.lbl(L, s.T("concept"), "b", fg="ac", bg="card").pack(anchor="w")
        s.lbl(L, lv["concept"], "n", fg="sb", bg="card", wraplength=240, justify="left").pack(anchor="w", pady=(4, 10))
        hl = s.lbl(L, "", "n", bg="card", wraplength=240, justify="left")
        def hint():
            if used[0] < len(lv["hints"]):
                hl.config(text="%s %d：%s" % (s.T("tip"), used[0] + 1, lv["hints"][used[0]]))
                used[0] += 1
            else:
                hl.config(text=s.T("nohint"))
        s.btn(L, s.T("hint"), hint).pack(anchor="w")
        hl.pack(anchor="w", pady=8)
        M = s.card(main)
        M.grid(row=0, column=1, sticky="nsew", padx=4)
        ed = tk.Text(M, font=s.F["m"], bg=c["card"], fg=c["tx"], insertbackground=c["tx"], relief="flat", undo=True, wrap="none", padx=6, pady=6, tabs=("1c",))
        ed.pack(fill="both", expand=True)
        ed.insert("1.0", lv["start"])
        R = s.card(main)
        R.grid(row=0, column=2, sticky="nsew", padx=(8, 0))
        s.lbl(R, s.T("output"), "h", bg="card").pack(anchor="w")
        out = tk.Text(R, font=s.F["m"], bg=c["card"], fg=c["tx"], relief="flat", height=8, state="disabled", wrap="word")
        out.pack(fill="both", expand=True, pady=6)
        st = s.lbl(R, "", "b", fg="ac", bg="card", wraplength=260, justify="left")
        st.pack(anchor="w")
        def show(text):
            out.config(state="normal")
            out.delete("1.0", "end")
            out.insert("1.0", text)
            out.config(state="disabled")
        def fmt(o, e):
            return o + (("\n" if o else "") + "⚠ " + e if e else "")
        def run():
            o, e = run_code(ed.get("1.0", "end"), lv["tests"][0][0])
            show(fmt(o, e))
            st.config(text="", fg=c["ac"])
        def submit():
            code = ed.get("1.0", "end")
            res = [(run_code(code, pre), exp) for pre, exp in lv["tests"]]
            good = [(o.strip() == exp and not e) for ((o, e), exp) in res]
            bad = next((r for r, g in zip(res, good) if not g), res[0])
            show(fmt(*bad[0]))
            if all(good):
                stars = 3 - min(2, used[0])
                key = str(i)
                s.data["stars"][key] = max(stars, s.data["stars"].get(key, 0))
                s.save()
                s.go(s.p_result, i, stars, code.strip())
            else:
                st.config(text="%s %d / %d" % (s.T("tests"), sum(good), len(good)), fg=c["sb"])
        def reset():
            ed.delete("1.0", "end")
            ed.insert("1.0", lv["start"])
        B = tk.Frame(s.box, bg=c["bg"])
        B.pack(fill="x", padx=24, pady=(6, 16))
        s.btn(B, s.T("submit"), submit, True).pack(side="right")
        s.btn(B, s.T("run"), run).pack(side="right", padx=8)
        s.btn(B, s.T("reset"), reset).pack(side="right")

    def p_result(s, i, stars, code):
        c = s.C()
        s.bar()
        m = tk.Frame(s.box, bg=c["bg"])
        m.pack(expand=True)
        s.lbl(m, s.T("cleared"), "t").pack()
        if stars < 2:
            s.lbl(m, s.T("retake"), "b", fg="ac").pack(pady=(8, 0))
        s.lbl(m, "★" * stars + "☆" * (3 - stars), "t", fg="ac").pack(pady=8)
        s.lbl(m, LEVELS[i]["concept"], "n", fg="sb", wraplength=600).pack(pady=8)
        cd = s.card(m)
        cd.pack(pady=8)
        s.lbl(cd, s.T("yours"), "b", fg="ac", bg="card").pack(anchor="w")
        s.lbl(cd, code, "m", bg="card", justify="left").pack(anchor="w")
        r = tk.Frame(m, bg=c["bg"])
        r.pack(pady=12)
        nxt = (lambda: s.go(s.p_story, i + 1, 0)) if i + 1 < len(LEVELS) else (lambda: s.go(s.p_map))
        s.btn(r, s.T("replay"), lambda: s.go(s.p_challenge, i), stars < 2).pack(side="left", padx=6)
        s.btn(r, s.T("map"), lambda: s.go(s.p_map)).pack(side="left", padx=6)
        if stars >= 2:
            s.btn(r, s.T("next"), nxt, True).pack(side="left", padx=6)

    def p_settings(s):
        c = s.C()
        s.bar(s.T("settings"))
        cd = s.card(s.box)
        cd.pack(padx=24, pady=10, fill="x")
        def row(title):
            s.lbl(cd, title, "h", bg="card").pack(anchor="w", pady=(12, 6))
            f = tk.Frame(cd, bg=c["card"])
            f.pack(anchor="w")
            return f
        f = row(s.T("theme"))
        for k in THEMES:
            s.btn(f, s.T(k), lambda k=k: s.set("theme", k), s.data["theme"] == k).pack(side="left", padx=(0, 8))
        f = row(s.T("lang"))
        for k, name in (("zh", "繁體中文"), ("en", "English")):
            s.btn(f, name, lambda k=k: s.set("lang", k), s.data["lang"] == k).pack(side="left", padx=(0, 8))
        f = row(s.T("size"))
        sc = tk.Scale(f, from_=12, to=24, orient="horizontal", length=320, bg=c["card"], fg=c["tx"], troughcolor=c["bd"],
                      highlightthickness=0, font=s.F["s"], command=lambda v: s.set_size(v))
        sc.set(int(s.data["size"]))
        sc.pack()
        r = tk.Frame(cd, bg=c["card"])
        r.pack(fill="x", pady=(18, 0))
        s.btn(r, s.T("back"), lambda: s.go(*([s.prev[0]] + list(s.prev[1]))), True).pack(side="right")
        s.btn(r, s.T("defaults"), lambda: (s.data.update(theme="scifi", lang="zh", size=15), s.sync_fonts(), s.save(), s.render())).pack(side="right", padx=8)
    def set(s, k, v):
        s.data[k] = v
        s.save()
        s.render()
    def set_size(s, v):
        s.data["size"] = int(float(v))
        s.sync_fonts()
        s.save()


if __name__ == "__main__":
    App().root.mainloop()
