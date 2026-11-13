# Review for midterm #2

## When

Wednesday, November 18, 13:50–14:50 pm.

The review session is Monday, November 16. Bring your questions.

## What it covers

Assignments A4 and A5, and the readings behind them: V5, V6, SET, REF, NAME, and
NEED. Copy-in, copy-out (CICO) is not in the textbook. What you need is what A5
Question 2 taught.

Aliasing and order of evaluation, from class, are also on it, with less weight
than the homework material.

Terminology and concepts from those textbook chapters are fair game, even where
the homework did not ask about them.

TYPE0 and TYPE1 are not on this exam. They are on the final.

## What it looks like

* Around 20 points. Most questions are selected response, such as multiple
  choice, and are worth 1 point each.

* One or two written questions, worth 3 points each. These might ask you to draw
  an environment on paper, in the notation from A4 and A5, or to explain in your
  own words what a program prints and why.

* Written answers are scored 3, 2, 1, or 0. A 3 is effectively correct, and a
  small slip does not cost you the 3 when it is clear you understand the idea. A
  1 means the idea is not there. A 2 is anything in between, and a 0 is blank.

The exam is meant to be finished well inside the hour. Most questions ask you to
work something out by hand: what a program prints, in one language or in two,
and why. Very few ask you to recall a fact. Many questions name the language the
program runs in. Read that first: the same program can print different things in
SET, REF, NAME, NEED, and CICO.

## What you should be able to do

### Recursion: V5 and V6 (A4)

* Say what a `letrec` program prints, or why it fails. Know that `letrec`
  evaluates its right-hand sides **in order, in the new node**, and that a
  `proc` delays its body: a name in the body is looked up when the function is
  **called**.

* Say why `let` cannot recurse: in which node `let` evaluates its right-hand
  sides, and in which node `letrec` does.

* Trace a sequence of `defines`. Know that a closure that saved `Program.env`
  sees a later define, and one that saved another node does not.

* Trace V5 and V6 programs from the environment chain, which has no refs, as in
  A3.

### Refs and side effects: SET (A4)

* Draw each binding as name → ref → value, and show what a `set` changes.

* Know which constructs make a new ref: `let`, application, `letrec`, and
  `define`. So `let y = x` copies, and a later `set x` does not reach `y`.

* Know what set does, what it returns, and why it can never make a new variable.

* Explain how a procedure remembers something from one call to the next.

### Call by value and call by reference: REF (A4)

* Predict one program in SET and in REF, and explain the difference from the
  refs.

* Know what a formal gets in REF when the argument is a variable, and when it is
  anything else.

* Point to the code in the REF interpreter that decides what a formal gets, and
  say why it treats a variable differently from every other argument.

### Delayed arguments: NAME and NEED (A5)

* Say which arguments become thunks, and what a thunk holds: the expression and
  the **caller**'s environment.

* Say how many times a thunk is evaluated in NAME and in NEED, and what that
  does to a program with a set in an argument.

* Know which formals are read-only in NEED, and what happens when one is set.

### Copy-in, copy-out (A5)

* Trace a CICO call: what the formal holds after the copy in, after each set,
  and what the copy out puts back.

* Explain the code you added in A5 Question 2: what each change does, and when
  it runs.
  
### Comparing them (A5 and class)

* Fill in the table from class from memory: one row per language, including
  CICO, and one column per kind of argument. Use it to predict a program in any
  of the five.

* Recognize aliasing, one ref reachable by two names, and say what it does in
  REF and in CICO.

* Say how the order in which things are evaluated can change what a program with
  sets in it prints, in each of the five languages.

### How to study

* **Redo the predict-first questions from A4 and A5 without running anything.**
  Then check yourself against the run and the feedback on your graded work. The
  exam asks the same kind of questions, with no tool to check against.

* **Draw refs.** Cover the drawings you handed in for A4 and A5, draw each one
  again, then compare. This is the single best use of your time for the drawing
  question.

* **Run one program in all five languages.** Write down your five predictions
  first, then run them with language discussed and your CICO. Check your CICO
  first with the test program in A5 Question 2(c). Where a prediction is wrong,
  say which ref or thunk you got wrong.

* **Reread the readings** (V5, V6, SET, REF, NAME, and NEED) and the core
  concepts listed in A4’s and A5’s Purpose sections.

* Come to the review session with whatever surprised you along the way.

## What is not on the exam

* TYPE0 and TYPE1.

* Which real languages fix the order of evaluation, such as C, Java, and Python.

* Writing interpreter code from scratch.
