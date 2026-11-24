# CS373 - Assignment a6

## Purpose

In `REF`, nothing stops a program from adding 1 to a procedure, and you find
out only when the program reaches the bad operation. `TYPE1` checks the types
of the whole program first, and runs it only if it passes. In this assignment
you work out types by hand the way the checker does, and then write the type
checker for a construct that does not have one: a `for` loop.

Two skills matter here. The first is finding the type of an expression from
its text, without running it. The second is turning a typing rule, stated in
English, into an `evalType` method.

### Reading

From the [course textbook](https://ourplcc.github.io/course-materials-ng/dev/):
[Types](https://ourplcc.github.io/course-materials-ng/dev/18-type/) and
[TYPE1](https://ourplcc.github.io/course-materials-ng/dev/20-type1/).

As in the previous assignment, questions here use languages in defined in the
language repository. You can clone this repository with the command:

```
git clone https://github.com/ourPLCC/languages-ng.git
```

### What you will be able to do

1. **Find types.** Give the type of an expression, or say which check fails.
   Annotate a `proc` with the types it needs.

2. **Explain a rejection.** Find the line of `TYPE1` that rejects a program,
   and say why the language rejects it even when it would have run fine.

3. **Write a type checker.** State the typing rule for a new construct, write
   its `evalType`, and say what goes wrong when the rule is wrong.

### The core concepts

The Correctness criterion looks at these concepts. Details may get a comment
from me but cost you no points.

- **Every well-typed expression has a type, found from the text without
  running it.** The checker checks every expression, including ones that will
  never run: both branches of an `if`, and the body of a `proc` nobody calls.

- **A `proc`'s type comes from its annotations**, the types written after its
  parameters and before its body. `proc(x : int) : bool ...` has type
  `[ int => bool ]`. Its body is checked once, where the `proc` appears, and
  must have the declared return type.

- **A variable's type is its declaration's type**, found by static scope in a
  **type environment**. A type environment binds names to types, the way an
  environment binds names to values.

- **Applying a procedure checks three things:** that it has a proc type, that
  the number of arguments matches, and that each argument's type matches its
  parameter's. The application has the procedure's return type. Applying a
  primitive, like `+(1, 2)`, is checked the same way, except that a
  primitive's type is fixed: `+` is `[ int, int => int ]`, `zero?` is
  `[ int => bool ]`.

- **Types are equal by structure.** `int` equals `int`. Two proc types are
  equal when their parameter types and return types are. Parameter names do
  not count.

- **`TYPE1` is strongly and statically typed.** In a program that passes the
  checker, no operation gets a value of the wrong type when it runs. Other
  errors, such as dividing by zero, can still happen. The cost is that some
  programs that would run fine are rejected.

## How to do this assignment

**Your answers go in this file.** Every question has one or more `ANSWER`
blocks that look like this:

````
```
Replace this line with your answer.
```
````

Replace that line with your answer and leave the fences around it alone.

**Predict first, then run.** Write the prediction down before you run
anything. Then run it and say whether you were right. The prediction is where
the learning is. The run is only the check. A wrong prediction followed by an
honest correction is a complete answer.

To run a program in a language from the cloned language repository:

```bash
cd .../languages/TYPE1/python
echo 'let x = 42 in add1(x)' | plcc-rep
```

or run `plcc-rep` with no input and type or paste programs. Ctrl-D ends it. A
type error does not end it, but a parse error does.

Scoring is the same as in A1 to A5: [grading.md](../../grading.md), three
criteria, nine points. Correctness looks at the **core concepts** listed
above. There are no drawings in this assignment.

## QUESTION 1 — Types and type errors

Use `TYPE1` (`.../languages/TYPE1/python`) for this whole question.

**(a)** For each expression, write its type, or say that it has a type error
and which check fails. Do all five by hand first.

```
(1)  proc(f : [ int => bool ], n : int) : int if .f(n) then n else 0
(2)  .proc(n : int) : [ int => int ] proc(m : int) : int +(n, m) (3)
(3)  let f = proc(x : int) : bool zero?(x) in if true then f else proc(n : int) : bool true
(4)  let f = proc(x : int) : bool zero?(x) in +(1, .f(0))
(5)  proc(g : [ int => int ]) : int g
```

Then check each one. A `define` prints the name and the type of its right-hand
side, so `define a1 = ` followed by expression (1) prints (1)'s type. Use a
new name for each, because a name cannot be defined twice.

For (3), say why the two branches of the `if` have the same type.

### ANSWER — (a)

```
Replace this line with your answer.
```

**(b)** In `REF`, this procedure takes two procedures and returns their
composition:

```
proc(f, g) proc(x) .f(.g(x))
```

Write it in `TYPE1` with every annotation filled in, where `g` takes an `int`
and returns an `int`, and `f` takes an `int` and returns a `bool`. Give the
type of the whole thing. Then replace `COMPOSE` in this program with yours and
run it:

```
let c = COMPOSE in ..c(proc(n : int) : bool zero?(n), proc(n : int) : int sub1(n))(1)
```

(`.c(...)` returns a procedure, and the other `.` applies that procedure to
`1`.)

### ANSWER — (b)

```
Replace this line with your answer.
```

**(c)** `TYPE1` rejects both of these. Without type checking, the first would
give `3` and the second would give `4`.

```
(1)  let d = 0 in if zero?(d) then 3 else .d(1)
(2)  let x = 3 in { set x = zero?(x) ; 4 }
```

For **each** one:

- predict the message, then run it;
- find the `evalType` method in `.../languages/TYPE1/python/spec.plcc` whose
  check fails, name its class, and quote the line that makes the check;
- say why `TYPE1` rejects the program, even though it would run fine.

### ANSWER — (c)

```
Replace this line with your answer.
```


## QUESTION 2 — A type checker for `for`

`FOR/`, in this directory, is `TYPE1` with a `for` loop added. The tokens, the
grammar rule, and `eval` are written. The type checking is not.

```
<Exp:ForExp> ::= FOR <SYMBOL> EQUALS <Exp:loExp> TO <Exp:hiExp> DO <Exp:bodyExp>
```

**What `for` means.** Evaluate both bounds once, in the environment where the
loop appears. Then run the body once for each integer from the low bound to
the high bound, counting both. Each time, the body runs in a new node that
binds the loop variable to that integer. If the low bound is greater than the
high bound, the body never runs. **The value of the whole loop is the number
of times the body ran.** The body's own value is ignored, so it can be
anything.

For example, this prints `10`, because the loop adds 1, 2, 3, and 4 to `s`:

```
let s = 0 in { for i = 1 to 4 do set s = +(s, i) ; s }
```

**All your changes go in `FOR/python/spec.plcc`.** Do not change
`FOR/grammar.plcc`, `FOR/check.py`, or `Env/`. To run it:

```bash
cd FOR/python
echo '+(1, 2)' | plcc-rep
```

Everything in `TYPE1` still works. Until you write `evalType`, every `for`
program stops with `Specification error: NotImplementedError`, because
checking comes before running.

**(a)** Before you write any code, state the typing rule for `for` in English.
Say what must be checked, in which type environment each of the three
expressions is typed, and what the type of the whole loop is.

### ANSWER — (a)

```
Replace this line with your answer.
```

**(b)** In the `ForExp` section of `FOR/python/spec.plcc`, replace the line
`# Write evalType here.` with your `evalType`. The imports it needs are already
there. Three methods in the same file show you how to do the pieces:

- `IfExp.evalType` checks that an expression has a particular type.
- `LetDecls.addTypeBindings` extends a type environment, and `LetExp.evalType`
  types a body in it. `[self.symbol]` is a list holding just the loop
  variable.
- `LitExp.evalType` returns a type.

Use the `check...` methods that `Type` already has to report type errors. Do
not write your own messages.

Then run the tests:

```bash
cd FOR
python3 check.py
```

They check every part of the rule, with programs your checker must accept and
programs it must reject. A test that says `rejects` passes only when your
checker refuses the program with the right message. A crash does not count,
and neither does an error that shows up only when the program runs. Run them
as often as you like, and keep going until they all pass.

Now predict, run, and explain each of these. Say which part of your rule
decides each one.

```
(1)  let i = true in for i = 1 to i do 3
(2)  for i = 1 to 0 do add1(true)
(3)  add1(for i = 1 to 3 do zero?(i))
```

### ANSWER — (b)

```
Replace this line with your answer.
```

**(c)** Now break it on purpose. Change your `evalType` so that the type of
the whole loop is the **body's** type, and change nothing else. Run the tests
again, and run this program, which your checker from (b) rejects:

```
if for i = 1 to 0 do zero?(i) then 1 else 2
```

- What does it print now, and **when** is the error found: while the program
  is being checked, or while it is running?
- `TYPE1` is strongly and statically typed. Why can you no longer say that
  about `FOR`?
- The broken checker also rejects some good programs. Pick one test that now
  fails because a good program is rejected, and explain why it is rejected.

Then **change it back** and run the tests once more. The `spec.plcc` you
submit should pass all of them.

### ANSWER — (c)

```
Replace this line with your answer.
```

## Before you run `save`

- [ ] Every `ANSWER` block has an answer in it. An unanswered block reads as
      skipped work under **Completeness**.
- [ ] Question 1(c) has all three pieces for **both** programs.
- [ ] `FOR/python/spec.plcc` has your `evalType` from Question 2(b), **not**
      the broken one from (c), and `python3 check.py` passes.

`plcc-ng/` directories are build caches. Leaving them in place costs you
nothing.
