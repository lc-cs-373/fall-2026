#!/usr/bin/env python3
"""Check a FOR build.

    python3 check.py              check the build next to this file
    python3 check.py <directory>  check the build in another FOR directory

Each test runs one program. An `accepts` test passes when the program prints
the right value. A `rejects` test passes when the checker refuses the program
with the right message, so a crash, or an error that shows up only when the
program runs, does not count as a rejection.

Nothing here is submitted, and nothing here needs to change.
"""

import pathlib
import subprocess
import sys

OK, NO = "accepts", "rejects"

# A bound's mismatch may be reported either way around: both are correct.
BOOL_BOUND = ("type mismatch: bool != int", "type mismatch: int != bool")
PROC_BOUND = ("type mismatch: [int=>int] != int", "type mismatch: int != [int=>int]")

LOW = "Low bound is int"
HIGH = "High bound is int"
OUTER = "Bounds use the outer environment"
VAR = "Loop variable is int in the body"
LOCAL = "Loop variable is local to the body"
SEES = "Body sees outer variables"
ANY = "Body can have any type"
ALWAYS = "Body is always checked"
WHOLE = "Whole loop is int"
NEST = "Nesting"
REST = "Rest of TYPE1 still works"

# (row, accepts or rejects, program, expected: a string, or several that will do)
TESTS = [
    (REST, OK, "+(2, 3)", "5"),
    (REST, OK, "let f = proc(x : int) : bool zero?(x) in if .f(0) then 1 else 2", "1"),
    (REST, OK, "letrec f = proc(n : int) : int if zero?(n) then 1 else"
               " *(n, .f(sub1(n))) in .f(5)", "120"),
    (REST, OK, "let total = 1 done = 2 format = 3 in +(total, +(done, format))", "6"),
    (REST, NO, "add1(true)", "type mismatch: bool != int"),
    (REST, NO, "if true then 3 else false", "type mismatch: bool != int"),
    (REST, NO, "let x = 3 in set x = true", "type mismatch: bool != int"),
    (REST, NO, ".proc(t : int) : int t (true)", "type mismatch: bool != int"),
    (REST, NO, "let x = 3 in .x(4)", "int: attempt to apply a non-procedure"),

    (LOW, OK, "for k = 1 to 4 do k", "4"),
    (LOW, OK, "let n = 3 in for k = n to 4 do k", "2"),
    (LOW, OK, "for k = +(1, 1) to 4 do k", "3"),
    (LOW, NO, "for k = false to 4 do k", BOOL_BOUND),
    (LOW, NO, "for k = proc(x : int) : int x to 4 do 7", PROC_BOUND),

    (HIGH, OK, "let n = 5 in for k = 1 to n do k", "5"),
    (HIGH, OK, "for k = 1 to *(2, 3) do k", "6"),
    (HIGH, NO, "for k = 1 to <?(1, 2) do k", BOOL_BOUND),
    (HIGH, NO, "for k = 1 to proc(x : int) : int x do 7", PROC_BOUND),

    (OUTER, OK, "let k = 3 in for k = k to 5 do k", "3"),
    (OUTER, OK, "let k = 3 in for k = 1 to k do k", "3"),
    (OUTER, NO, "let k = false in for k = k to 5 do 7", BOOL_BOUND),
    (OUTER, NO, "let k = false in for k = 1 to k do 7", BOOL_BOUND),
    (OUTER, NO, "for k = k to 5 do 7", "no type binding for k"),
    (OUTER, NO, "for k = 1 to add1(k) do 7", "no type binding for k"),

    (VAR, OK, "for k = 1 to 2 do sub1(k)", "2"),
    (VAR, OK, "let k = false in for k = 1 to 2 do sub1(k)", "2"),
    (VAR, NO, "for k = 1 to 2 do not(k)", "type mismatch: int != bool"),
    (VAR, NO, "for k = 1 to 2 do set k = false", "type mismatch: bool != int"),

    (LOCAL, OK, "let k = false in { for k = 1 to 2 do k ; not(k) }", "true"),
    (LOCAL, OK, "let k = false in { for j = 1 to 2 do k ; not(k) }", "true"),
    (LOCAL, NO, "{ for k = 1 to 2 do k ; k }", "no type binding for k"),
    (LOCAL, NO, "let k = false in { for k = 1 to 2 do k ; add1(k) }",
     "type mismatch: bool != int"),

    (SEES, OK, "let p = 1 in { for k = 1 to 5 do set p = *(p, k) ; p }", "120"),
    (SEES, OK, "let b = true in { for k = 1 to 3 do set b = not(b) ; b }", "false"),
    (SEES, NO, "let p = 1 in { for k = 1 to 5 do set p = <?(p, k) ; p }",
     "type mismatch: bool != int"),
    (SEES, NO, "for k = 1 to 5 do +(k, z)", "no type binding for z"),

    (ANY, OK, "for k = 1 to 2 do 9", "2"),
    (ANY, OK, "for k = 1 to 2 do <?(k, 2)", "2"),
    (ANY, OK, "for k = 1 to 2 do proc(x : int) : bool <?(x, k)", "2"),

    (ALWAYS, OK, "for k = 3 to 2 do sub1(k)", "0"),
    (ALWAYS, NO, "for k = 3 to 2 do sub1(false)", "type mismatch: bool != int"),
    (ALWAYS, NO, "for k = 3 to 2 do .k(1)", "int: attempt to apply a non-procedure"),
    (ALWAYS, NO, "for k = 1 to 2 do if true then k else false",
     "type mismatch: bool != int"),

    (WHOLE, OK, "*(10, for k = 1 to 3 do k)", "30"),
    (WHOLE, OK, "*(10, for k = 1 to 3 do <?(k, 2))", "30"),
    (WHOLE, OK, "let f = proc(n : int) : int for k = 1 to n do k in .f(3)", "3"),
    (WHOLE, NO, "if for k = 1 to 3 do <?(k, 2) then 1 else 2",
     "type mismatch: int != bool"),
    (WHOLE, NO, "proc(n : int) : bool for k = 1 to n do <?(k, 2)",
     "type mismatch: int != bool"),

    (NEST, OK, "let s = 0 in { for j = 1 to 3 do for k = 1 to j do set s = add1(s) ; s }",
     "6"),
    (NEST, OK, "for j = 1 to 2 do for j = j to 3 do j", "2"),
    (NEST, OK, "+(1, for j = 1 to 2 do for k = 1 to j do <?(j, k))", "3"),
    (NEST, OK, "let f = proc(n : int) : int { for k = 1 to n do set n = add1(n) ; n }"
               " in .f(3)", "6"),
    (NEST, NO, "for j = 1 to 2 do for k = 1 to j do and(j, k)",
     "type mismatch: int != bool"),
    (NEST, NO, "for j = 1 to 2 do for k = 1 to not(true) do 7", BOOL_BOUND),
    (NEST, NO, "for j = 1 to 2 do if for k = 1 to j do <?(j, k) then 1 else 2",
     "type mismatch: int != bool"),
]

CRASH = "Specification error"
MAX_CRASHES = 3     # each crash means starting plcc-rep again, which is slow


def rep(directory, text):
    """Run plcc-rep on text, in directory, and return what it printed."""
    try:
        p = subprocess.run(["plcc-rep"], input=text, cwd=directory, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           timeout=120)
    except FileNotFoundError:
        sys.exit("plcc-rep was not found. Run this in your Codespace.")
    except subprocess.TimeoutExpired:
        return "(timed out)"
    return p.stdout


def run_all(directory, programs):
    """What each program printed, in order.

    Every program is followed by a number that nothing else prints, so extra
    output, such as a debugging print, cannot be mistaken for the next
    program's result. If a program crashes plcc-rep, its number never comes
    out, and the run starts again at the program after it. After MAX_CRASHES
    crashes the rest are not run, and the list returned is short.
    """
    results = []
    crashes = 0
    while len(results) < len(programs) and crashes < MAX_CRASHES:
        todo = range(len(results), len(programs))
        out = rep(directory, "".join(f"{programs[i]}\n{70000000 + i}\n" for i in todo))
        lines = [line.rstrip() for line in out.splitlines() if line.strip()]
        for i in todo:
            mark = str(70000000 + i)
            if mark in lines:
                at = lines.index(mark)
                results.append(lines[at - 1] if at else "(nothing)")
                lines = lines[at + 1:]
            else:
                crash = [line for line in lines if line.startswith(CRASH)]
                results.append((crash or lines or ["(nothing)"])[0])
                crashes += 1
                break
    return results


def main():
    here = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else __file__).resolve()
    directory = (here if here.is_dir() else here.parent) / "python"
    if not (directory / "spec.plcc").is_file():
        sys.exit(f"There is no python/spec.plcc in {directory.parent}")

    # Before anything else: does the language build and run at all?
    out = rep(directory, "1\n")
    if out.strip() != "1":
        print("Your FOR does not build. plcc-rep said:\n")
        print(out)
        return 1

    results = run_all(directory, [program for _, _, program, _ in TESTS])

    failed = 0
    for (row, kind, program, expected), got in zip(TESTS, results):
        wanted = (expected,) if isinstance(expected, str) else expected
        good = got in wanted
        failed += not good
        print(f"{'PASS' if good else 'FAIL'}  {kind}  [{row}]  {program}")
        if not good:
            print(f"        expected: {' or '.join(wanted)}")
            print(f"        got:      {got}")

    print()
    unrun = len(TESTS) - len(results)
    if unrun:
        print(f"plcc-rep crashed {MAX_CRASHES} times, so {unrun} tests were not run.")
        print("If the crash is a NotImplementedError, ForExp has no evalType yet.")
    if failed:
        print(f"{len(results) - failed} of {len(TESTS)} passed, {failed} failed.")
        return 1
    print(f"All {len(TESTS)} passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
