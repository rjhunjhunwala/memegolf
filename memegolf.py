import re

regexs = list(map(lambda s: re.compile(r"^\s*%s\s*$" % s), [
        r"Outgolf Dennis by (\d+) bytes.",
        r"\^+",
        r"44",
        r"-15",
        r"Juice avocado for (\d+) minutes.",
        r"Yingluck",
        r'"use (\w+)";',
        r"Tim (\w+)",
        r"HE COMES",
]))

def outgolf(state, _, g):
        state["acc"] += int(g.group(1))
def carrot(state, l, _):
        if state["acc"]:
                state["i"] -= len(l) + 1
def p44(state, _, __):
        print(chr(state["acc"]), end="")
def m15(state, _, __):
        state["i"] += 1
def avocad(state, _, g):
        state["acc"] -= int(g.group(1))
def yingluck(state, _, __):
        # TODO: Implement a getch function
        state["acc"] = ord(input())
def use(state, _, g):
        state["vars"][g.group(1).upper()] = state["acc"]
def tim(state, _, g):
        state["acc"] = state["vars"][g.group(1).upper()]
def hecomes(state, _, __):
        state["c"] = False

funcs = [
        outgolf,
        carrot,
        p44,
        m15,
        avocad,
        yingluck,
        use,
        tim,
        hecomes,
]

def meme(s):
        lines = s.split("\n")
        state = {"i": 0, "acc": 0, "c": True, "vars": {}}
        while state["c"]:
                l = lines[state["i"]]
                state["i"] += 1
                for i, r in enumerate(regexs):
                        if r.search(l):
                                r.sub(lambda g: funcs[i](state, l, g), l)
                                break
                if state["i"] >= len(lines):
                        state["i"] = 0

def encodes(s):
        S = []
        acc = 0
        for c in s:
                diff = acc - ord(c)
                if diff < 0:
                        S.append("Outgolf Dennis by %d bytes." % -diff)
                        acc += -diff
                elif diff > 0:
                        S.append("Juice avocado for %d minutes." % diff)
                        acc -= diff
                l = c
                S.append("44")
        return "\n".join(S)

if __name__ == "__main__":
        import sys
        with open(sys.argv[1]) as f:
                t = f.read()
        meme(t)
